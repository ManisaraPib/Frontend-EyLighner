import os
from flask import Flask, request,render_template,send_file,redirect,url_for
import cv2
from PIL import Image

UPLOAD_FOLDER = './image_storage'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

if __name__ == '__main__':
    app.run()