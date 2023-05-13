import cv2
import os


def testModel(imagePath1:str, imagePath2:str):
    imagePath1 = os.path.join("..",imagePath1)
    imagePath2 = os.path.join("..",imagePath2)
    print(f"DEBUG|open image path: {imagePath1} , {imagePath2}")
    img1 = cv2.imread("/Users/sirakis/Documents/GitHub/Frontend-EyLighner/backend/files1.jpg",0)
    img2 = cv2.imread("/Users/sirakis/Documents/GitHub/Frontend-EyLighner/backend/files2.jpg",0)

    output_imageName1 = "testAlgo1.jpg"
    output_imageName2 = "testAlgo2.jpg"

    cv2.imwrite(output_imageName1, img1)
    cv2.imwrite(output_imageName2, img2)

    return(output_imageName1,output_imageName2)

