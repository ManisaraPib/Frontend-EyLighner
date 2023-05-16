#Server Side
from dataclasses import field
from pyexpat import model
from flask import Flask,send_file,send_from_directory
from flask_restful import Api,Resource,abort
from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
import pathlib
import socket
import numpy
import cv2 as cv
from models import Files
from PIL import Image
import time
import smtplib
import os
import re
import asyncio
import cv2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from werkzeug.datastructures import ImmutableMultiDict,FileStorage
from Algorithm.Eylighner_Algorithm import Same_Time_Op, Dif_Time_Op_1, Dif_Time_Op_2, align_result
#from Algorithm.testAlgo import testModel


# from zmq import Message
#from flask import send_file
#from urllib import response
#from flask_sqlalchemy import SQLAlchemy

# import model
#from __(model path)__ import __(model function name)__



# define image path
path = ""
#model = '__(model h5 file name)___.h5'

app = Flask(__name__)
api= Api(app)
UPLOAD_FOLDER = './image_storage'
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

def get_ip():
    host = request.host.split(':')[0]  # extract the hostname from request.host
    ip = socket.gethostbyname(host)    # get the IP address using socket.gethostbyname()
    return ip

@app.route('/', methods=['GET', 'POST'])
def test():
    return "eyeliner ai server"

#Upload 
@app.route('/upload_files/', methods=['GET', 'POST'])
def upload_file():

    data = []
    data_name = []
    model_result = {}
    ip = get_ip()
    # Get post method from frontend
    if request.method == 'POST':
        print("INFO| image uploading...")
        form_list = [Files(*item) for item in list(request.form.items())]
        form_list.pop(0)
        recieved_list = request.files.getlist('files')
        for i in range (0,len(recieved_list)):
            fileStorage = recieved_list[i]
            file_bytes = fileStorage.read()
            #convert string data to numpy array
            file_bytes = numpy.frombuffer(file_bytes, numpy.uint8)
            # convert numpy array to image
            img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
            path = f"files{i+1}.jpg"
            cv.imwrite(path, img)
        
        for x in form_list:
            # print("DEBUG| from_list item:",x)
            if 'type' in x.image_id:
                data_name.append(x)
            if 'files' in x.image_id :
                num = re.findall(r'\d+', x.content)
                status = True
                for i in num:
                    if int(i) > len(recieved_list):
                        status = False
                if status == True:
                    data.append(x)

        # print("data:",data)
        # print("form list:",form_list)
        for i in data_name:
            print("DEBUG| image name: ", i)

        image_num = 0
        for n in range(0,len(data)):
            print ("DEBUG|dataname: ",data_name[n].content)
            print("DEBUG: data:",data[n])
            if data[n].content == 'None':
                #print(f"INFO| SameTimeOp | return image : {result_imagePath1} , {result_imagePath2}")
           
                model_result[f'{image_num}'] = {
                    "url1" : "",
                    "url2" : "",
                    "0" : [],
                    "1" : [],
                    "name" : ""
                }
                image_num = image_num+1

            if data[n].content != 'None' and data[n].content != 'null':
                file_id = data[n].image_id
                if file_id == "files 1" or file_id == "files 3" or file_id == "files 6" or file_id == "files 10" or file_id == "files 15":
                    num = data[n].content.split(", ")
                    num = [int(x) for x in num]
                    image_path_1 = f"files{str(num[0])}.jpg"
                    image_path_2 = f"files{str(num[1])}.jpg"

                    print("INFO| Same time op ==> ",image_path_1,image_path_2)
                    # result_imagePath1,result_imagePath2 = testModel(image_path_1,image_path_2)
                    # print('check result1',image1,image2)
                    
                    result_align_1, result_align_2 = align_result(image_path_1, image_path_2) 
                    result_imagePath1,result_0 = Same_Time_Op(result_align_1)
                    assert result_imagePath1 != None, "ERROR| SameTimeOp | No image return"

                    result_imagePath2, result_1 = Same_Time_Op(result_align_2)
                    assert result_imagePath2 != None, "ERROR| SameTimeOp | No image return"
                    
                    print(f"INFO| SameTimeOp | return image : {result_imagePath1} , {result_imagePath2}")

                    model_result[f'{image_num}'] = {
                        'url1' : f"http://31.220.6.186:8443/image/{result_imagePath1}",
                        'url2' : f"http://31.220.6.186:8443/image/{result_imagePath2}",
                        '0' : result_0,
                        '1' : result_1,
                        'name' : data_name[n].content
                    }
                    image_num = image_num+1

                else:
                    num = data[n].content.split(", ")
                    num = [int(x) for x in num]
                    image_path_1 = f"files{str(num[0])}.jpg"
                    image_path_2 = f"files{str(num[1])}.jpg"

                    print("INFO| Same time op ==> ",image_path_1,image_path_2)
                    # result_imagePath1,result_imagePath2 = testModel(image_path_1,image_path_2)

                    result_align_1, result_align_2 = align_result(image_path_1, image_path_2) 
                    result_imagePath1,result_0 = Dif_Time_Op_1(result_align_1)
                    assert result_imagePath1 != None, "ERROR| DiffTimeOp | No image return"

                    result_imagePath2, result_1 = Dif_Time_Op_2(result_align_2)
                    assert result_imagePath2 != None, "ERROR| DiffTimeOp | No image return"

                    print(f"INFO| DiffTimeOp | return image : {result_imagePath1} , {result_imagePath2}")

                    model_result[f'{image_num}'] = {
                        'url1' : f"http://31.220.6.186:8443/image/{result_imagePath1}",
                        'url2' : f"http://31.220.6.186:8443/image/{result_imagePath2}",
                        '0' : result_0,
                        '1' : result_1,
                        'name' : data_name[n].content
                    }
                    image_num = image_num + 1
        json_string = json.dumps(model_result, indent=4)
        print("DEBUG| model result: ",json_string)
        return model_result


# test url : http://127.0.0.1:5000/image/IMG_5448.JPG
@app.route('/image/<imagePath>')
def get_image2(imagePath:str):
    print("DEBUG| get image : ", imagePath)
    return send_from_directory(".",imagePath)



#Select Image from Folder
# def select():
#     if request.method == "POST":
#         image_name = request.form.get("fname")
#         print(image_name)
#         if image_name == "1close_eye":
#             file_name = "1close_eye"

#         if image_name == "1open_eye":
#             file_name = "1open_eye"

#         image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_name}.jpg")
#         print(image_path)

# pass image file result to URL
# import requests
# @app.route('/image_url', methods=['GET'])
# def image_url():
#     try:
#         f = open('c:/tensorflow1/temp.jpg','wb')
#         image_url = request.args['image_url']  # get the image URL
#         f.write(requests.get(image_url).content)
#         f.close()
#         # Set an image confidence threshold value to limit returned data
#         threshold = request.form.get('threshold')
#         if threshold is None:
#             threshold = 0.5
#         else:
#             threshold = float(threshold)

#         # finally run the image through tensor flow object detection`
#         image_object = Image.open('c:/tensorflow1/temp.jpg')
#         objects = od_ws_api.get_objects(image_object, threshold)
#         return objects

#     except Exception as e:
#         print(e)
#         return 'error'
        
#Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("sending an email...")
        data = request.json

        print(data)
        name = data["name"]
        email = data["email"]
        message = data["message"]

# to clients
        mail_content = " Thank you. We have received your information. We will contact you back soon."
        #The mail addresses and password
        sender_address = 'powerpufffy@gmail.com'
        sender_pass = 'cpjlcidxhdvxeysc'
        receiver_address = str(email)
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Response email to '+ str(name)   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent to Eylighner user')

#to Staff
        mail_content = str(message)+ "customer email : " +  str(email)
        #The mail addresses and password
        sender_address = 'powerpufffy@gmail.com'
        sender_pass = 'cpjlcidxhdvxeysc'
        receiver_address = "gutto.juuung@gmail.com"
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Want to contact '+ str(name)   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent to Eyligner Developer')

        res = {"message" : "success"}
        
        print(res)
        return  jsonify(res)

#run Main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443, debug=True)
    #127 = host='0.0.0.0'