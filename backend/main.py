#Server Side
from pyexpat import model
from flask import Flask
from flask_restful import Api,Resource,abort
from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
import pathlib
import numpy
import cv2 as cv
from models import Files
from PIL import Image
import time
import smtplib
import os
import re
import asyncio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from werkzeug.datastructures import ImmutableMultiDict,FileStorage

from Algorithm.Eylighner_Algorithm import Same_Time_Op, Dif_Time_Op_1, Dif_Time_Op_2
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

#Upload 
@app.route('/upload_files', methods=['GET', 'POST'])
def upload_file():
    # Get post method from frontend
    if request.method == 'POST':
        print("uploading...")
        print(list(request.form.items()))
        form_list = [Files(*item) for item in list(request.form.items())]
        # print(type(form_list))
        # file_list = [Files(*x) for x in form_list]
        
        # for i in range (len(form_list)):
            

        recieved_list = request.files.getlist('files')
        for i in range (1,len(recieved_list)):
            fileStorage = recieved_list[i]
            print(i,fileStorage)
            file_bytes = fileStorage.read()
            # print(file_bytes)

            #convert string data to numpy array
            file_bytes = numpy.frombuffer(file_bytes, numpy.uint8)
            # convert numpy array to image
            img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
            cv.imwrite(f"Image_{i}.jpg", img)


        # filtered_strings = [x for x in form_list if [int(match) for match in re.findall(r"\d+",  x.content)] <= 2]
        data = []
        for x in form_list:
            if 'files' in x.image_id :
                num = re.findall(r'\d+', x.content)
                status = True
                for i in num:
                    if int(i) > len(recieved_list):
                        status = False
                if status == True:
                    data.append(x)
                    file_id = x.image_id
                    if file_id == "files 1" or file_id == "files 3" or file_id == "files 6" or file_id == "files 10" or file_id == "files 12":
                        print(x.image_id ," --> Same time" )
                    else:
                        print(x.image_id ," --> Diff time" )

        # print("filtered_strings",filtered_strings)
        print("Filtered :",data)


        # while i < len(data):


        #     i = i+1

        openeye_image = request.files['f0_1']
        closeeye_image = request.files['f0_2']
        
        # Check if file not exist
        if 'open_image' not in request.files:
            return 'open_image is not exist'
        if 'close_image' not in request.files:
            return 'close_image is not exist'


        # Save file to givened directoery
        openeye_path = os.path.join(app.config['UPLOAD_FOLDER'], "open_eye.jpg")
        closeeye_path = os.path.join(app.config['UPLOAD_FOLDER'], "close_eye.jpg")
        openeye_image.save(openeye_path)
        closeeye_image.save(closeeye_path)
        print ("Save images")






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
    app.run()
    #127 = host='0.0.0.0'



          
