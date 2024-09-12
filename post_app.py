import os 
from flask import Flask, render_template
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, FileField

app = Flask(__name__)



@app.route('/')
def index():
    return'Ready'


