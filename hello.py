from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
from werkzeug import secure_filename
import os

app = Flask(__name__, static_folder="")

def conv(input_path):
    col=Image.open(input_path)
    bw=col.convert('L')
    return bw

@app.route('/')
def ind():
    return render_template('index.html')

@app.route('/img', methods=["POST", "GET"])
def upl():
    upl_img = request.files['img']
    bw_img=conv(input_path=upl_img)
    bw_img.save('bw.jpg')
    return render_template("hello.html", image=bw_img)