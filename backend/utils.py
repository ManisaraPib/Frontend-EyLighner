from Algorithm.Eylighner_Algorithm import Same_Time_Op, Dif_Time_Op_1, Dif_Time_Op_2, align_result


def handleHardCode(data:list, n:int, file_id:str):
    num = data[n].content.split(", ")
    num = [int(x) for x in num]
    image_path_1 = f"files{str(num[0])}.jpg"
    image_path_2 = f"files{str(num[1])}.jpg"

    if file_id == "files 2":
            Dif_Time_Op_1
            Dif_Time_Op_2
            
    if file_id == "files 4":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 5":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 7":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 8":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 9":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 10":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 11":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 12":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 13":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    if file_id == "files 14":
                        Dif_Time_Op_1
            Dif_Time_Op_2
    
                    # result_align_1, result_align_2 = align_result(image_path_1, image_path_2) 

                    # result_imagePath1,result_0 = Same_Time_Op(result_align_1)
                    # result_imagePath2, result_1 = Same_Time_Op(result_align_2)



    print("INFO| Same time op ==> ",image_path_1,image_path_2)
    result_imagePath1,result_imagePath2 = testModel(image_path_1,image_path_2)

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
