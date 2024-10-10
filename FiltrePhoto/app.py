import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image
from PIL import Image
import itertools as tool
import math as m



UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.secret_key = 'agvreigajiorgeifraiougavuijhgreaigreujiha'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def red_image(link):
    image = Image.open("link")

@app.route('/upload_file', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect('/')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('/')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Fichier Uploadé !')
            return render_template('edit.html', image=filename)

@app.route('/')
def hello_world():
    return render_template('home.html')



def white_and_black():
    im = Image.open("./photo.jpg")
    for x, y in tool.product(range(im.width), range(im.height)):
        gray_rgb_value = round(
            (im.getpixel((x, y))[0] + im.getpixel((x, y))[1] + im.getpixel((x, y))[2])/3)
        im.putpixel((x, y), (m.floor(gray_rgb_value/128)*255,
                    m.floor(gray_rgb_value/128)*255, m.floor(gray_rgb_value/128)*255))
