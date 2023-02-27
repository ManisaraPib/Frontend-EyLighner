#Server Side
from pyexpat import model
from flask import Flask
from flask_restful import Api,Resource,abort
from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin
import pathlib
from PIL import Image
import time
import smtplib
import os
import asyncio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from zmq import Message
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
CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

#Flask run test page
@app.route("/test") # Define route of the function
def test_page():
    return "Flask run sucess"

#Upload 
@app.route('/input/', methods=['GET', 'POST'])
def upload_file():

    # Get post method from frontend
    if request.method == 'POST':
        # Check if file not exist
        if 'open_image' not in request.files:
            return 'open_image is not exist'
        if 'close_image' not in request.files:
            return 'close_image is not exist'

        # Step
        # rename images follow by image description (api topic)

        # Get request file from frontend
        number = request.form.get("number")
        openeye_image = request.files['open_image']
        closeeye_image = request.files['close_image']

        # Save file to givened directoery
        openeye_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{str(number)}open_eye.jpg")
        closeeye_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{str(number)}close_eye.jpg")
        openeye_image.save(openeye_path)
        closeeye_image.save(closeeye_path)
        return render_template(('input.html'))

    return render_template(('input.html'))

# @app.route('/get_image')
# def get_image():

#     image
#     # return send_file(filename, mimetype='image/gif')
#     return redirect(url_for(".home", image = image))

#Select Image from Folder
@app.route("/home/", methods = ["GET","POST"])
def home():
    if request.method == "POST":
        image_name = request.form.get("fname")
        print(image_name)
        if image_name == "1close_eye":
            file_name = "1close_eye"

        if image_name == "1open_eye":
            file_name = "1open_eye"

        image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_name}.jpg")
        print(image_path)

        # img = cv2.imread('./image_storage/1open_eye.jpg',0)
        # img = Image.open(image_path)
        # print(img)

        # return redirect(url_for(".home"))
        return send_file(image_path, mimetype='image/gif')


    return render_template("home.html")




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



          
