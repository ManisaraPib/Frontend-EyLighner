import cv2
import mediapipe as mp
from shapely.geometry import Polygon, Point
import numpy as np
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
from Algorithm.Eylighner_Algorithm import align_result, ms1, ms2, OSA_Left_Eye, OSA_Right_Eye,EBH_Right_Eye, EBH_Left_Eye, SameTime_Image_Open, SameTime_Image_Close, DifTime_Image_Open_1, DifTime_Image_Close_1, DifTime_Image_Open_2, DifTime_Image_Close_2


##########################################################################################
# function กรณีเวลาเดียวกัน จะครอปแบบ full face ขนาด 800x850 px
def Same_Time_Op(img):
  if OSA_Left_Eye(img) >= 4000 and OSA_Right_Eye(img) >= 4000 : #กรณีภาพลืมตา
    ms = ms1(img)
    img_dif = SameTime_Image_Open(img) #ภาพครอปเฉพาะตา และ คิ้ว กรณีลืมตา
  else: #กรณีภาพหลับตา --> ค่า OSA จะเป็น 0
    ms = ms2(img)
    img_dif = SameTime_Image_Close(img) #ภาพครอปเฉพาะตา และ คิ้ว  กรณีหลับตา
  return ms, img_dif


##########################################################################################
# function กรณีคนละเวลา จะครอปแบบเฉพาะตา และ คิ้ว ขนาด 1000x400 px
# และ Dif_Time_Op_1 ตรง 1 คือหมายถึง text ที่กำกับตาเป็น R1, L1
def Dif_Time_Op_1(img):
  if OSA_Left_Eye(img) >= 4000 and OSA_Right_Eye(img) >= 4000 : #กรณีภาพลืมตา
    ms = ms1(img)
    img_dif = DifTime_Image_Open_1(img) #ภาพครอปเฉพาะตา และ คิ้ว กรณีลืมตา
  else: #กรณีภาพหลับตา --> ค่า OSA จะเป็น 0
    ms = ms2(img)
    img_dif = DifTime_Image_Close_1(img) #ภาพครอปเฉพาะตา และ คิ้ว  กรณีหลับตา
  return ms, img_dif #จะ return ค่าทั้ง 4 และ ภาพออกมา

##########################################################################################
##########################################################################################

# function กรณีคนละเวลา จะครอปแบบเฉพาะตา และ คิ้ว ขนาด 1000x400 px
# และ Dif_Time_Op_2 ตรง 2 คือหมายถึง text ที่กำกับตาเป็น R2, L2
def Dif_Time_Op_2(img):
  if OSA_Left_Eye(img) >= 4000 and OSA_Right_Eye(img) >= 4000 : #กรณีภาพลืมตา
    ms = ms1(img)
    img_dif = DifTime_Image_Open_2(img) #ภาพครอปเฉพาะตา และ คิ้ว กรณีลืมตา
  else: #กรณีภาพหลับตา --> ค่า OSA จะเป็น 0
    ms = ms2(img)
    img_dif = DifTime_Image_Close_2(img) #ภาพครอปเฉพาะตา และ คิ้ว  กรณีหลับตา
  return ms, img_dif #จะ return ค่าทั้ง 4 และ ภาพออกมา


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

############################################ เวลาเรียกใช้งาน ###############################################
ติด ## ข้างล่างทั้งหมดก่อนที่จะรัน
เวลา import ใน back-end คือ
from Algorithm.caller import align_result, Same_Time_Op, Dif_Time_Op_1, Dif_Time_Op_2


# path ของภาพ อันนี้เขียนไว้ให้ดูเฉยๆ เวลา รับ 1 คู่ จะมี 2 ภาพ
image_path_1 = cv2.imread('')
image_path_2 = cv2.imread('')



##########################################################################################################
########## same time ##############
# กรณีเวลาเดียวกัน
# ครอปแบบ full face ขนาด 800x850 px
# คำสั้งคือ 3 บรรทัดนี้ 
result_align_1, result_align_2 = align_result(image_path_1, image_path_2) 
Same_Time_Op(result_align_1) #--> A,B = Same_Time_Op(result_align_1) :ผลลัพธ์  A = ค่า 4 ค่า , B = ภาพ
Same_Time_Op(result_align_2) #--> A,B = Same_Time_Op(result_align_2) :ผลลัพธ์  A = ค่า 4 ค่า , B = ภาพ



# ฮธิบายแบบละเอียด

# 1.) Aligment --> จัดสัดส่วนให้ทั้ง 2 ภาพเท่ากัน 
#     - เรียกใช้งาน : result_align_1, result_align_2 = align_result(image_path_1, image_path_2) 
#     - ชื่อของ function : align_result
#     - input จะใส่ไป 2 ภาพ : image_path_1, image_path_2
#     - output เป็นภาพที่ align แล้ว 2 ภาพ : result_align_1, result_align_2

# 2.) Measurement --> หาค่า EBH & OSA และ ขีดเส้นที่ตา + add text (R,L) ในภาพ 
#     - เรียกใช้งาน Same_Time_Op(result_align_1)  และ Same_Time_Op(result_align_2)
#     - ชื่อของ function : Same_Time_Op
#     - อันนี้ถ้าเวลาเดียวกันจะมีแค่ function นี้อันเดียวเลย *************
#     - input :  ภาพที่ได้จาก alignent 
#     - output : return ออกมา 4 ค่า และ 1 ภาพ ตามลำดับ
#                --> 4 ค่า เรียงลำดับคือ EHB Right, EBH Left, OSA Right, OSA Left
# ตรง function มีอธิบายไว้ เลื่อนขึ้นไปนิดหน่อย



##########################################################################################################
########## Dif time ##############
# กรณีคนละเวลา
# ครอปแบบเฉพาะตา และ คิ้ว ขนาด 1000x400 px
# คำสั้งคือ 3 บรรทัดนี้ 
result_align_1, result_align_2 = align_result(image_path_1, image_path_2) 
Dif_Time_Op_1(result_align_1) #--> A,B = Dif_Time_Op_1(result_align_1) :ผลลัพธ์ A = ค่า 4 ค่า , B = ภาพ
Dif_Time_Op_2(result_align_2) #--> A,B = Dif_Time_Op_2(result_align_2) :ผลลัพธ์ A = ค่า 4 ค่า , B = ภาพ

# อธิบายแบบละเอียด

# 1.) Aligment --> จัดสัดส่วนให้ทั้ง 2 ภาพเท่ากัน 
#     - เรียกใช้งาน : result_align_1, result_align_2 = align_result(image_path_1, image_path_2) 
#     - ชื่อของ function : align_result
#     - input จะใส่ไป 2 ภาพ : image_path_1, image_path_2
#     - output เป็นภาพที่ align แล้ว 2 ภาพ : result_align_1, result_align_2

# 2.) Measurement --> หาค่า EBH & OSA และ ขีดเส้นที่ตา + add text (R,L) ในภาพ 
#     - เรียกใช้งาน Dif_Time_Op_1(result_align_1)  และ Dif_Time_Op_2(result_align_2)
#     - ชื่อของ function : Dif_Time_Op_1 และ Dif_Time_Op_2
#                        ----> Dif_Time_Op_1 : text จะเป็น R1, L1
#                        ----> Dif_Time_Op_2 : text จะเป็น R2, L2
#     - อันนี้จะมี 2 function ต่างกับเวลาเดียวกัน **********
#     - input :  ภาพที่ได้จาก alignent 
#     - output : return ออกมา 4 ค่า และ 1 ภาพ ตามลำดับ
#                --> 4 ค่า เรียงลำดับคือ EHB Right, EBH Left, OSA Right, OSA Left
# ตรง function มีอธิบายไว้ เลื่อนขึ้นไปนิดหน่อย


##########################################################################################################
# อธิบายชื่อ function เพิ่มเติม 
# 1. Alignment : align_result

# 2. Measurement
#       - output ออกมาเฉพาะค่า
#             -----> EBH
#                        - EBH ตาขวา : EBH_Right_Eye
#                        - EBH ตาซ้าย : EBH_Left_Eye
#             -----> OSA
#                        - OSA ตาขวา : OSA_Right_Eye
#                        - OSA ตาซ้าย : OSA_Left_Eye
#       - output ออกมาเฉพาะรูปภาพ
#             -----> เวลาเดียวกัน (จะครอปแบบ full face ขนาด 800x850 px)
#                        - ภาพลืมตา : SameTime_Image_Open
#                                    << จะมีเส้น EBH (เส้นลากจากตาบนไปท้องคิ้ว), เส้นลากรอบดวงตา, text(R1, L1) >>
#                        - ภาพหลับตา : SameTime_Image_Close
#                                    << จะมีเส้น EBH (เส้นลากจากตาบนไปท้องคิ้ว), text(R2, L2) >>
#             -----> คนละเวลา(จะครอปแบบเฉพาะตา และ คิ้ว ขนาด 1000x400 px)
#                        - ภาพลืมตา 
#                              o Text R1, L1 : DifTime_Image_Open_1
#                                    << จะมีเส้น EBH (เส้นลากจากตาบนไปท้องคิ้ว), เส้นลากรอบดวงตา, text(R1, L1) >>
#                              o Text R2, L2 : DifTime_Image_Open_2
#                                    << จะมีเส้น EBH (เส้นลากจากตาบนไปท้องคิ้ว), เส้นลากรอบดวงตา, text(R2, L2) >>
#                        - ภาพหลับตา 
#                              o Text R1, L1 : DifTime_Image_Close_1
#                                    << จะมีเส้น EBH (เส้นลากจากตาบนไปท้องคิ้ว), text(R1, L1) >>
#                              o Text R2, L2 : DifTime_Image_Close_2
#                                    << จะมีเส้น EBH (เส้นลากจากตาบนไปท้องคิ้ว), text(R2, L2) >>
#       - output ออกมาทั้งค่าและรูปภาพ 
#             -----> เวลาเดียวกัน : Same_Time_Op 
#                         << จะ return ออกมา 4 ค่า คือ EHB Right, EBH Left, OSA Right, OSA Left และ 1 ภาพ >>
#             -----> คนละเวลา
#                         - Text R1, L1 : Dif_Time_Op_1
#                         - Text R2, L2 : Dif_Time_Op_2
#                         << จะ return ออกมา 4 ค่า คือ EHB Right, EBH Left, OSA Right, OSA Left และ 1 ภาพ >>


RAM ที่ใช้ 1.3 GB


files 2 : 1 = Dif_Time_Op_1
          3 = Dif_Time_Op_2
files 4 : 1 = Dif_Time_Op_1
          5 = Dif_Time_Op_2
files 5 : 3 = Dif_Time_Op_1
          5 = Dif_Time_Op_2
files 7 : 1 = Dif_Time_Op_1
          7 = Dif_Time_Op_2
files 8 : 3 = Dif_Time_Op_1
          7 = Dif_Time_Op_2
files 9 : 5 = Dif_Time_Op_1
          7 = Dif_Time_Op_2
files 11 :  1 = Dif_Time_Op_1
            9 = Dif_Time_Op_2
files 12 :  3 = Dif_Time_Op_1
            9 = Dif_Time_Op_2
files 13 :  5 = Dif_Time_Op_1
            9 = Dif_Time_Op_2
files 14 :  7 = Dif_Time_Op_1
            9 = Dif_Time_Op_2