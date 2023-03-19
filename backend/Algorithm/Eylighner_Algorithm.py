import cv2 
import mediapipe as mp
from shapely.geometry import Polygon, Point
import numpy as np
from shapely.geometry import Polygon
import matplotlib.pyplot as plt


def landmarks_list(im):
  mp_drawing = mp.solutions.drawing_utils
  mp_drawing_styles = mp.solutions.drawing_styles
  mp_face_mesh = mp.solutions.face_mesh

  drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1,color=(0,255,0))
  with mp_face_mesh.FaceMesh(
      static_image_mode=True,
      max_num_faces=1,
      refine_landmarks=True,
      min_detection_confidence=0.5) as face_mesh:

    #IMAGE_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    image = im
    #image_gray = IMAGE_gray.copy()
    
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    landmarks_points = []
    annotated_image = image.copy()
    #mask_mp = np.zeros_like(image_gray)

    for face_landmarks in results.multi_face_landmarks:
      for n in range(0, 468):
        x = int(face_landmarks.landmark[n].x * image.shape[1])
        y = int(face_landmarks.landmark[n].y * image.shape[0])
        landmarks_points.append((x, y))

      mp_drawing.draw_landmarks(
            image=annotated_image,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_tesselation_style())

  return [landmarks_points] #[landmarks_points ,annotated_image]

def get_landmarks(image):
  
    points = np.array(landmarks_list(image))
    points = np.asmatrix(points)
    points = points.reshape(468,2)

    return points

def automatic_brightness_and_contrast(image, clip_hist_percent=1):
    new_size = (1800, 1200) 
    image = cv2.resize(image, new_size)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])
    hist_size = len(hist)
    
    accumulator = []
    accumulator.append(float(hist[0]))
    for index in range(1, hist_size):
        accumulator.append(accumulator[index -1] + float(hist[index]))
    
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum/100.0)
    clip_hist_percent /= 2.0
    
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1
    
    maximum_gray = hist_size -1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1
    
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha

    auto_result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return auto_result

def read_im_and_landmarks(image):
    im = cv2.resize(image, (image.shape[1] * 1,
                         image.shape[0] * 1))
    s = get_landmarks(image)

    return image, s

def warp_im(im, M, dshape):
    output_im = np.zeros(dshape, dtype=im.dtype)
    cv2.warpPerspective(im,
                   M[:],
                   (dshape[1], dshape[0]),
                   dst=output_im,
                   flags=cv2.WARP_INVERSE_MAP)
    return output_im

def transform(image1, image2):
       
    auto_result1 = automatic_brightness_and_contrast(image1)
    auto_result2 = automatic_brightness_and_contrast(image2)

    im1 , points_X1 = read_im_and_landmarks(auto_result1)
    im2 , points_X2 = read_im_and_landmarks(auto_result2)

    homography, mask = cv2.findHomography(points_X1, points_X2, cv2.RANSAC)
                                   
    warped_im2 = warp_im(im2, homography, im1.shape)

    cv2.imwrite('output.jpg',warped_im2)
    image = cv2.imread('output.jpg')
    return image

def result(image1, image2):
       
    auto_result1 = automatic_brightness_and_contrast(image1)
    tf_1 = transform(image1, image2)

    return auto_result1, tf_1

##########################################################################################################
##########################################################################################################
########################################## Measurement ###################################################

faceModule = mp.solutions.face_mesh
face_mesh = faceModule.FaceMesh(static_image_mode=True)

def plot_landmark_oval(img):
    results = face_mesh.process(img)
    landmarks = results.multi_face_landmarks[0]
    relative_source_ls = []
    relative_target_ls = []
    FACE_OVAL_coordinate = list(faceModule.FACEMESH_FACE_OVAL)
    for source_idx, target_idx in FACE_OVAL_coordinate :
        source = landmarks.landmark[source_idx]
        target = landmarks.landmark[target_idx]

        relative_source = (int(img.shape[1] * source.x), int(img.shape[0] * source.y))
        relative_target = (int(img.shape[1] * target.x), int(img.shape[0] * target.y))
        
        relative_source_ls.append(relative_source)
        relative_target_ls.append(relative_target)

    return relative_source_ls, relative_target_ls

def plot_landmark_eye(config, img):
    results = face_mesh.process(img)
    landmarks = results.multi_face_landmarks[0]
    while True :
        if config.lower() == 'left' :
            side_of_data = faceModule.FACEMESH_LEFT_EYE
            break
        elif config.lower() == 'right':
            side_of_data = faceModule.FACEMESH_RIGHT_EYE
            break
        else :
            config = input('Enter left or right : ')

    for source_idx, target_idx in side_of_data :
        source = landmarks.landmark[source_idx]
        target = landmarks.landmark[target_idx]

        relative_source = (int(img.shape[1] * source.x), int(img.shape[0] * source.y))
        relative_target = (int(img.shape[1] * target.x), int(img.shape[0] * target.y))

        cv2.line(img, relative_source, relative_target, (255, 0, 0), thickness = 2)
         
    #plt.imshow(img)

    return img

def plot_landmark_eye_bw(config, img, plot=True):
    results = face_mesh.process(img)
    landmarks = results.multi_face_landmarks[0]
    while True :
        if config.lower() == 'left' :
            side_of_data = faceModule.FACEMESH_LEFT_EYE
            break
        elif config.lower() == 'right':
            side_of_data = faceModule.FACEMESH_RIGHT_EYE
            break
        else :
            config = input('Enter left or right : ')
            
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    
    for source_idx, target_idx in side_of_data:
        source = landmarks.landmark[source_idx]
        target = landmarks.landmark[target_idx]

        relative_source = (int(img.shape[1] * source.x), int(img.shape[0] * source.y))
        relative_target = (int(img.shape[1] * target.x), int(img.shape[0] * target.y))

        cv2.line(img, relative_source, relative_target, (255, 0, 0), thickness = 2)
        
    #if plot == True :
        #plt.imshow(img)

    return img

def plot_landmark_eyebrow(config, img):
    results = face_mesh.process(img)
    landmarks = results.multi_face_landmarks[0]
    while True :
        if config.lower() == 'left' :
            side_of_data = faceModule.FACEMESH_LEFT_EYEBROW
            break
        elif config.lower() == 'right':
            side_of_data = faceModule.FACEMESH_RIGHT_EYEBROW
            break
        else :
            config = input('Enter left or right : ')

    for source_idx, target_idx in side_of_data :
        source = landmarks.landmark[source_idx]
        target = landmarks.landmark[target_idx]

        relative_source = (int(img.shape[1] * source.x), int(img.shape[0] * source.y))
        relative_target = (int(img.shape[1] * target.x), int(img.shape[0] * target.y))

        cv2.line(img, relative_source, relative_target, (255, 0, 0), thickness = 2)
         
    #plt.imshow(img)

    return img


def plot_landmark_eyebrow_bw(config, img, plot=True):
    results = face_mesh.process(img)
    landmarks = results.multi_face_landmarks[0]
    while True :
        if config.lower() == 'left' :
            side_of_data = faceModule.FACEMESH_LEFT_EYEBROW
            break
        elif config.lower() == 'right':
            side_of_data = faceModule.FACEMESH_RIGHT_EYEBROW
            break
        else :
            config = input('Enter left or right : ')
            
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    
    for source_idx, target_idx in side_of_data:
        source = landmarks.landmark[source_idx]
        target = landmarks.landmark[target_idx]

        relative_source = (int(img.shape[1] * source.x), int(img.shape[0] * source.y))
        relative_target = (int(img.shape[1] * target.x), int(img.shape[0] * target.y))

        cv2.line(img, relative_source, relative_target, (255, 0, 0), thickness = 2)
        
    #if plot == True :
        #plt.imshow(img)

    return img

def draw_ROI(config, config2, img) :
    image = img
    
    while True :
        if config.lower() == 'left' :
            if config2.lower() == 'eye' :
                side_of_data = faceModule.FACEMESH_LEFT_EYE
                break
            elif config2.lower() == 'eyebrow' :
                side_of_data = faceModule.FACEMESH_LEFT_EYEBROW
                break
            else :
                print('Invalid input please input eye or eyebrow')
        elif config.lower() == 'right':
            if config2.lower() == 'eye' :
                side_of_data = faceModule.FACEMESH_RIGHT_EYE
                break
            elif config2.lower() == 'eyebrow' :
                side_of_data = faceModule.FACEMESH_RIGHT_EYEBROW
                break
            else :
                print('Invalid input please input eye or eyebrow')
        else :
            config = input('Enter left or right : ')
            config2 = input('Enter left or right : ')
            
    image_temp = plot_landmark_bw(side_of_data, image, plot=False)

    upper = np.array([255, 0, 0])
    lower = upper
    mask = cv2.inRange(image_temp, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]

    cv2.drawContours(image, [largest_contour], -1, color=(255, 0, 0), thickness=2)
    
    return image_temp, mask

def fill_ROI(img) :
    image = img
    
    for config in ['left', 'right'] :
        image_temp = plot_landmark_eye_bw(config, image, plot=False)

        upper = np.array([255, 0, 0])
        lower = upper
        mask = cv2.inRange(image_temp, lower, upper)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]

        cv2.drawContours(image, [largest_contour], -1, color=(255, 0, 0), thickness=cv2.FILLED)
    
    return image

def plot_landmark_bw(side_of_data, img, plot=True):
    results = face_mesh.process(img)
    landmarks = results.multi_face_landmarks[0]        
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, img) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    
    for source_idx, target_idx in side_of_data:
        source = landmarks.landmark[source_idx]
        target = landmarks.landmark[target_idx]

        relative_source = (int(img.shape[1] * source.x), int(img.shape[0] * source.y))
        relative_target = (int(img.shape[1] * target.x), int(img.shape[0] * target.y))

        cv2.line(img, relative_source, relative_target, (255, 0, 0), thickness = 2)
        
    #if plot == True :
        #plt.imshow(img)

    return img

################################################## OSA #####################################################
def OSA_Left_Eye(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI = img.copy()
  image_temp = plot_landmark_eye('left', image_ROI)
  image_temp = plot_landmark_eye('right', image_ROI)

  image_FILL_ROI = img.copy()
  image_FILL_ROI = fill_ROI(image_FILL_ROI)
  #plt.imshow(image_FILL_ROI)

  image_CALCULATE_ROI = img.copy()
  image_CALCULATE_ROI = plot_landmark_eye_bw('left',image_CALCULATE_ROI, plot=True) 

  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(image_CALCULATE_ROI, lower, upper)
  #plt.imshow(mask)

  contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  largest_contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
  final_result = np.zeros(image_temp.shape[:3]) # create a blank canvas to draw the final result
  final_result = cv2.drawContours(final_result, [largest_contour], -1, color=(255, 0, 0), thickness=cv2.FILLED)
  image_temp = cv2.drawContours(image_CALCULATE_ROI, [largest_contour], -1, color=(255, 0, 0), thickness=cv2.FILLED)
  #plt.imshow(image_CALCULATE_ROI)

  count_pixel_left_eye = np.count_nonzero(final_result)

  return count_pixel_left_eye

def OSA_Right_Eye(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI = img.copy()
  image_temp = plot_landmark_eye('left', image_ROI)
  image_temp = plot_landmark_eye('right', image_ROI)

  image_FILL_ROI = img.copy()
  image_FILL_ROI = fill_ROI(image_FILL_ROI)
  #plt.imshow(image_FILL_ROI)

  image_CALCULATE_ROI = img.copy()
  image_CALCULATE_ROI = plot_landmark_eye_bw('right',image_CALCULATE_ROI, plot=True)

  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(image_CALCULATE_ROI, lower, upper)
  #plt.imshow(mask)

  contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  largest_contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
  final_result = np.zeros(image_temp.shape[:3]) # create a blank canvas to draw the final result
  final_result = cv2.drawContours(final_result, [largest_contour], -1, color=(255, 0, 0), thickness=cv2.FILLED)
  image_temp = cv2.drawContours(image_CALCULATE_ROI, [largest_contour], -1, color=(255, 0, 0), thickness=cv2.FILLED)

  count_pixel_right_eye = np.count_nonzero(final_result)
  #print(count_pixel_right_eye)

  return count_pixel_right_eye

################################################## EBH #####################################################

def EBH(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_left_eye = draw_ROI('left', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_left_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_left_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_right_eye = draw_ROI('right', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_right_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_right_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  left_eye_point = sorted_contour_left_eye[0][0]
  right_eye_point = sorted_contour_right_eye[0][0]

  #image_ROI_to_Coordinate_Left
  image_ROI_to_Coordinate = img.copy()
  left_eye_brow_bw = plot_landmark_eyebrow_bw('left', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(left_eye_brow_bw, lower, upper)
  temp = left_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          left_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  left_eye_brow_bw = temp

  #image_ROI_to_Coordinate_Right
  image_ROI_to_Coordinate = img.copy()
  right_eye_brow_bw = plot_landmark_eyebrow_bw('right', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(right_eye_brow_bw, lower, upper)
  temp = right_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          right_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  right_eye_brow_bw = temp

  distance_left = int(left_eye_point[1]-left_eye_brow_point[1])
  distance_right = int(right_eye_point[1]-right_eye_brow_point[1])

  return distance_left, distance_right

def EBH_Left_Eye(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_left_eye = draw_ROI('left', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_left_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_left_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  left_eye_point = sorted_contour_left_eye[0][0]

  #image_ROI_to_Coordinate_Left
  image_ROI_to_Coordinate = img.copy()
  left_eye_brow_bw = plot_landmark_eyebrow_bw('left', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(left_eye_brow_bw, lower, upper)
  temp = left_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          left_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  left_eye_brow_bw = temp

  #Calculate Distance
  distance_left = int(left_eye_point[1]-left_eye_brow_point[1])

  return distance_left

def EBH_Right_Eye(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_right_eye = draw_ROI('right', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_right_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_right_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  right_eye_point = sorted_contour_right_eye[0][0]

  #image_ROI_to_Coordinate_Right
  image_ROI_to_Coordinate = img.copy()
  right_eye_brow_bw = plot_landmark_eyebrow_bw('right', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(right_eye_brow_bw, lower, upper)
  temp = right_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          right_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  right_eye_brow_bw = temp

  #Calculate Distance
  distance_right = int(right_eye_point[1]-right_eye_brow_point[1])

  return distance_right

##############################################################################################################
##############################################################################################################
################################################## Image #####################################################

################################################## Same Time #####################################################

def SameTime_Image_Open(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_left_eye = draw_ROI('left', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_left_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_left_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_right_eye = draw_ROI('right', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_right_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_right_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  left_eye_point = sorted_contour_left_eye[0][0]
  right_eye_point = sorted_contour_right_eye[0][0]

  #image_ROI_to_Coordinate_Left
  image_ROI_to_Coordinate = img.copy()
  left_eye_brow_bw = plot_landmark_eyebrow_bw('left', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(left_eye_brow_bw, lower, upper)
  temp = left_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          left_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  left_eye_brow_bw = temp

  #image_ROI_to_Coordinate_Right
  image_ROI_to_Coordinate = img.copy()
  right_eye_brow_bw = plot_landmark_eyebrow_bw('right', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(right_eye_brow_bw, lower, upper)
  temp = right_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          right_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  right_eye_brow_bw = temp
  
  #Draw Circle & Line
  red = [255,0,0]
  yellow = [255,255,0]
  blue = [0,0,255]
  img_test_color = img.copy()
  cv2.circle(img_test_color, left_eye_point, 5, red, -1)
  cv2.circle(img_test_color, left_eye_brow_point, 5, red, -1)
  cv2.circle(img_test_color, right_eye_point, 5, red, -1)
  cv2.circle(img_test_color, right_eye_brow_point, 5, red, -1)
  cv2.line(img_test_color, left_eye_point, left_eye_brow_point, red, thickness = 2)
  cv2.line(img_test_color, right_eye_point, right_eye_brow_point, red, thickness = 2)

  #Add ROI
  image_final = img_test_color.copy()
  image_final = plot_landmark_eye('left', image_final)
  image_final = plot_landmark_eye('right', image_final)

  #Add Text
  #R1
  font_right = cv2.FONT_HERSHEY_TRIPLEX #font
  org_right = (650, 530) #org
  fontScale_right = 0.8 #fontScale
  color_right = (0, 0, 0)
  thickness_right = 1
  image_final = cv2.putText(image_final,'R1', org_right, font_right, 
                    fontScale_right, color_right, thickness_right, cv2.LINE_AA)  # Using cv2.putText() method
  #L1
  font_left = cv2.FONT_HERSHEY_TRIPLEX #font
  org_left = (1100, 530) #org
  fontScale_left  = 0.8 #fontScale
  color_left  = (0, 0, 0)
  thickness_left  = 1
  image_final = cv2.putText(image_final,'L1', org_left , font_left , 
                    fontScale_left , color_left , thickness_left , cv2.LINE_AA)  # Using cv2.putText() method

  #Crop
  crop_image_final = image_final[200:1050, 500:1300] # Slicing to crop the image
  crop_image_final = cv2.cvtColor(crop_image_final, cv2.COLOR_RGB2BGR)

  return crop_image_final

def SameTime_Image_Close(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_left_eye = draw_ROI('left', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_left_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_left_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_right_eye = draw_ROI('right', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_right_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_right_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  left_eye_point = sorted_contour_left_eye[0][0]
  right_eye_point = sorted_contour_right_eye[0][0]

  #image_ROI_to_Coordinate_Left
  image_ROI_to_Coordinate = img.copy()
  left_eye_brow_bw = plot_landmark_eyebrow_bw('left', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(left_eye_brow_bw, lower, upper)
  temp = left_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          left_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  left_eye_brow_bw = temp

  #image_ROI_to_Coordinate_Right
  image_ROI_to_Coordinate = img.copy()
  right_eye_brow_bw = plot_landmark_eyebrow_bw('right', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(right_eye_brow_bw, lower, upper)
  temp = right_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          right_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  right_eye_brow_bw = temp
  
  #Draw Circle & Line
  red = [255,0,0]
  yellow = [255,255,0]
  img_test_color = img.copy()
  cv2.circle(img_test_color, left_eye_point, 5, red, -1)
  cv2.circle(img_test_color, left_eye_brow_point, 5, red, -1)
  cv2.circle(img_test_color, right_eye_point, 5, red, -1)
  cv2.circle(img_test_color, right_eye_brow_point, 5, red, -1)
  cv2.line(img_test_color, left_eye_point, left_eye_brow_point, red, thickness = 2)
  cv2.line(img_test_color, right_eye_point, right_eye_brow_point, red, thickness = 2)

 
  #Add Text
  image_final = img_test_color.copy()
  #R1
  font_right = cv2.FONT_HERSHEY_TRIPLEX #font
  org_right = (650, 530) #org
  fontScale_right = 0.8 #fontScale
  color_right = (0, 0, 0)
  thickness_right = 1
  image_final = cv2.putText(image_final,'R2', org_right, font_right, 
                    fontScale_right, color_right, thickness_right, cv2.LINE_AA)  # Using cv2.putText() method
  #L1
  font_left = cv2.FONT_HERSHEY_TRIPLEX #font
  org_left = (1100, 530) #org
  fontScale_left  = 0.8 #fontScale
  color_left  = (0, 0, 0)
  thickness_left  = 1
  image_final = cv2.putText(image_final,'L2', org_left , font_left , 
                    fontScale_left , color_left , thickness_left , cv2.LINE_AA)  # Using cv2.putText() method

  #Crop
  crop_image_final = image_final[200:1050, 500:1300] # Slicing to crop the image
  crop_image_final = cv2.cvtColor(crop_image_final, cv2.COLOR_RGB2BGR)

  return crop_image_final

##############################
def Same_Time_Op(img):
  if OSA_Left_Eye(img) >= 4000 and OSA_Right_Eye(img) >= 4000 :
    print(OSA_Left_Eye(img))
    print(OSA_Right_Eye(img))
    print(EBH_Left_Eye(img))
    print(EBH_Right_Eye(img))
    cv2.imshow("SameTime_Image_Open", SameTime_Image_Open(img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()  
  else:
    print('0')
    print('0')
    print(EBH_Left_Eye(img))
    print(EBH_Right_Eye(img))
    cv2.imshow("SameTime_Image_Close", SameTime_Image_Close(img))
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

################################################## Diff Time #####################################################
def DifTime_Image_1(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_left_eye = draw_ROI('left', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_left_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_left_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_right_eye = draw_ROI('right', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_right_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_right_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  left_eye_point = sorted_contour_left_eye[0][0]
  right_eye_point = sorted_contour_right_eye[0][0]

  #image_ROI_to_Coordinate_Left
  image_ROI_to_Coordinate = img.copy()
  left_eye_brow_bw = plot_landmark_eyebrow_bw('left', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(left_eye_brow_bw, lower, upper)
  temp = left_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          left_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  left_eye_brow_bw = temp

  #image_ROI_to_Coordinate_Right
  image_ROI_to_Coordinate = img.copy()
  right_eye_brow_bw = plot_landmark_eyebrow_bw('right', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(right_eye_brow_bw, lower, upper)
  temp = right_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          right_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  right_eye_brow_bw = temp
  
  #Draw Circle & Line
  red = [255,0,0]
  yellow = [255,255,0]
  img_test_color = img.copy()
  cv2.circle(img_test_color, left_eye_point, 5, red, -1)
  cv2.circle(img_test_color, left_eye_brow_point, 5, red, -1)
  cv2.circle(img_test_color, right_eye_point, 5, red, -1)
  cv2.circle(img_test_color, right_eye_brow_point, 5, red, -1)
  cv2.line(img_test_color, left_eye_point, left_eye_brow_point, red, thickness = 2)
  cv2.line(img_test_color, right_eye_point, right_eye_brow_point, red, thickness = 2)

  #Add ROI
  image_final = img_test_color.copy()
  image_final = plot_landmark_eye('left', image_final)
  image_final = plot_landmark_eye('right', image_final)

  #Add Text
  #R1
  font_right = cv2.FONT_HERSHEY_TRIPLEX #font
  org_right = (650, 530) #org
  fontScale_right = 0.8 #fontScale
  color_right = (0, 0, 0)
  thickness_right = 1
  image_final = cv2.putText(image_final,'R1', org_right, font_right, 
                    fontScale_right, color_right, thickness_right, cv2.LINE_AA)  # Using cv2.putText() method
  #L1
  font_left = cv2.FONT_HERSHEY_TRIPLEX #font
  org_left = (1100, 530) #org
  fontScale_left  = 0.8 #fontScale
  color_left  = (0, 0, 0)
  thickness_left  = 1
  image_final = cv2.putText(image_final,'L1', org_left , font_left , 
                    fontScale_left , color_left , thickness_left , cv2.LINE_AA)  # Using cv2.putText() method

  #Crop
  crop_image_final = image_final[300:700, 400:1400] # Slicing to crop the image
  crop_image_final = cv2.cvtColor(crop_image_final, cv2.COLOR_RGB2BGR)

  #plt.imshow(crop_image_final)

  return crop_image_final

def DifTime_Image_2(img):
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_left_eye = draw_ROI('left', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_left_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_left_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  image_ROI_to_Coordinate = img.copy()
  temp_image, mask_right_eye = draw_ROI('right', 'eye', image_ROI_to_Coordinate)
  contours, _ = cv2.findContours(mask_right_eye, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  sorted_contour_right_eye = sorted(contours, key=cv2.contourArea, reverse=True)[0]

  left_eye_point = sorted_contour_left_eye[0][0]
  right_eye_point = sorted_contour_right_eye[0][0]

  #image_ROI_to_Coordinate_Left
  image_ROI_to_Coordinate = img.copy()
  left_eye_brow_bw = plot_landmark_eyebrow_bw('left', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(left_eye_brow_bw, lower, upper)
  temp = left_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          left_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  left_eye_brow_bw = temp

  #image_ROI_to_Coordinate_Right
  image_ROI_to_Coordinate = img.copy()
  right_eye_brow_bw = plot_landmark_eyebrow_bw('right', image_ROI_to_Coordinate, plot=False)
  upper = np.array([255, 0, 0])
  lower = upper
  mask = cv2.inRange(right_eye_brow_bw, lower, upper)
  temp = right_eye_point.copy()
  while True :
      if temp[1] == 0 :
          break
      if tuple(temp) in zip(list(mask.nonzero())[1], list(mask.nonzero())[0]): 
          right_eye_brow_point = temp
          break
      else :
          temp[1] = temp[1]-1
  right_eye_brow_bw = temp
  
  #Draw Circle & Line
  red = [255,0,0]
  yellow = [255,255,0]
  img_test_color = img.copy()
  cv2.circle(img_test_color, left_eye_point, 5, red, -1)
  cv2.circle(img_test_color, left_eye_brow_point, 5, red, -1)
  cv2.circle(img_test_color, right_eye_point, 5, red, -1)
  cv2.circle(img_test_color, right_eye_brow_point, 5, red, -1)
  cv2.line(img_test_color, left_eye_point, left_eye_brow_point, red, thickness = 2)
  cv2.line(img_test_color, right_eye_point, right_eye_brow_point, red, thickness = 2)

  #Add ROI
  image_final = img_test_color.copy()
  image_final = plot_landmark_eye('left', image_final)
  image_final = plot_landmark_eye('right', image_final)

  #Add Text
  #R1
  font_right = cv2.FONT_HERSHEY_TRIPLEX #font
  org_right = (650, 530) #org
  fontScale_right = 0.8 #fontScale
  color_right = (0, 0, 0)
  thickness_right = 1
  image_final = cv2.putText(image_final,'R2', org_right, font_right, 
                    fontScale_right, color_right, thickness_right, cv2.LINE_AA)  # Using cv2.putText() method
  #L1
  font_left = cv2.FONT_HERSHEY_TRIPLEX #font
  org_left = (1100, 530) #org
  fontScale_left  = 0.8 #fontScale
  color_left  = (0, 0, 0)
  thickness_left  = 1
  image_final = cv2.putText(image_final,'L2', org_left , font_left , 
                    fontScale_left , color_left , thickness_left , cv2.LINE_AA)  # Using cv2.putText() method

  #Crop
  crop_image_final = image_final[300:700, 400:1400] # Slicing to crop the image
  crop_image_final = cv2.cvtColor(crop_image_final, cv2.COLOR_RGB2BGR)

  return crop_image_final

##############################
def Dif_Time_Op_1(img):
  print(OSA_Left_Eye(img))
  print(OSA_Right_Eye(img))
  print(EBH_Left_Eye(img))
  print(EBH_Right_Eye(img))
  cv2.imshow("DifTime_Image_1", (DifTime_Image_1(img)))
  cv2.waitKey(0)
  cv2.destroyAllWindows()  

def Dif_Time_Op_2(img):
  print(OSA_Left_Eye(img))
  print(OSA_Right_Eye(img))
  print(EBH_Left_Eye(img))
  print(EBH_Right_Eye(img))
  cv2.imshow("DifTime_Image_2", (DifTime_Image_2(img)))
  cv2.waitKey(0)
  cv2.destroyAllWindows()  
##########################################################################################################
##########################################################################################################
##########################################################################################################

#image_path_1 = cv2.imread('/Users/baitong/Documents/test1/2C4002EB-4AF6-446A-8834-5680E33B3801-15691-000002DD21D9B1EA.jpeg')
#image_path_2 = cv2.imread('/Users/baitong/Documents/test1/6C6BD02E-7D22-488A-A431-3C049F9CD9C8-15691-000002DD28A56769.jpeg')


########## Alignment ##############
#result1,result2 = result(image_path_1, image_path_2)

########## same time ##############
#Same_Time_Op(result1)
#Same_Time_Op(result2)
#ค่า1 คือ OSA Left, ค่า2 คือ OSA Right, ค่า3 คือ EBH Left, ค่า4 คือ EBH Right

########## Dif time ##############
#Dif_Time_Op_1(result3)
#Dif_Time_Op_2(result4)

