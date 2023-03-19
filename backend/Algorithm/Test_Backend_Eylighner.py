import cv2
import mediapipe as mp
from shapely.geometry import Polygon, Point
import numpy as np
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from Test_Algorithm_Eylighner import result, Same_Time_Op, Dif_Time_Op_1, Dif_Time_Op_2


image_list = [] #ลำดับทั้งหมด
i = ... #ลำดับที่เลือก --> มี 2 ภาพ คือ image_path_1 และ image_path_2
image_path_1 = ... #ภาพที่ 1
image_path_2 = ... #ภาพที่ 2

if i in range(len(image_list)) == image_list[1] and image_list[3] and image_list[6] and image_list[10] and image_list[15] :
    result1,result2 = result(image_path_1, image_path_2)
    image1 = Same_Time_Op(result1)
    image2 = Same_Time_Op(result2)
    print(image1, image2)
else :
    result1,result2 = result(image_path_1, image_path_2)
    image1 = Dif_Time_Op_1(result1)
    image2 = Dif_Time_Op_2(result2)
    print(image1, image2)

#ค่า1 คือ OSA Left, ค่า2 คือ OSA Right, ค่า3 คือ EBH Left, ค่า4 คือ EBH Right



    







