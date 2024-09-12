import os
import folium 
import pandas as pd
from flask import Flask

mmu = folium.Map(location=[2.9279623186421695, 101.64200330740373], zoo)

import os
import jwt
import datetime
import base64
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.utils import secure_filename
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.config["UPLOAD_PHOTO"] = os.path.join('static', 'image')
if not os.path.exists(app.config['UPLOAD_PHOTO']):
    os.makedirs(app.config['UPLOAD_PHOTO'])

app.secret_key = f"{os.urandom(32)}"
SECRET_KEY = app.secret_key

limiter_5 = Limiter ( get_remote_address, app= app, default_limits=["5 per minute"] )

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  
    if data['username'] == 'flaskApp' and data['password'] == 'App@123':
        token = jwt.encode({'user': data['username']}, SECRET_KEY, algorithm='HS256')
        print(token)
        return jsonify({'token': token})
    return jsonify({'message': 'Authentication failed'}), 401

@app.route('/protected', methods=['GET'])
@limiter_5.limit("5 per minute")    
def protected():
    token = request.headers.get('Authorization')
    try:
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'message': 'Access granted'})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

@app.route('/')
def upload():
    return render_template('upload_photo.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    error_message = None
    if 'image' not in request.files:
        error_message = 'image input is required in the form'
        print(error_message)
    else:
        file = request.files['image']
        
        if file.filename == '':
            error_message = 'image not selected'
            print(error_message)
        elif not allowed_images(file.filename):
            error_message = 'invalid image format, allowed formats are - png, jpg, jpeg, gif only'
            print(error_message)
        else:
            filename = secure_filename(file.filename)
            
            if os.path.exists(os.path.join(app.config['UPLOAD_PHOTO'], filename)):
                error_message = 'Image with the same name already exists.'
                print(error_message)
            else:
                file.save(os.path.join(app.config['UPLOAD_PHOTO'], filename))
                print('Image successfully uploaded')
                return redirect(url_for('image', filename=filename))
        return render_template('upload_photo.html', error_message=error_message)

@app.route('/image/<filename>')
def image(filename):
    if os.path.exists(os.path.join(app.config['UPLOAD_PHOTO'], filename)):
        return render_template('image.html', filename=filename)
    else:
        return render_template('notexist.html'), 404


def allowed_images(filename):
    if '.' not in filename:
        return False
    allowed_extensions = ('png', 'jpg', 'jpeg', 'gif')
    return filename.rsplit('.')[-1].lower() in allowed_extensions

@app.errorhandler(Exception)
def handle_error(error):
    print(error)
    return render_template('error.html'), 404

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_PHOTO'], exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=False)




basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MMU MAP'
app.config['UPLOAD_PHOTO_DEST'] =os.path.join(basedir, 'uploads')

photo = UploadSet('photo', IMAGES)
configure_uploads(app, photo)
patch_request_class(app)

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photo, 'Image only!'), FileRequired('File was empty!')])
    submit = SubmitField('Upload')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = photo.save(form.photo.data)
        file_url = photo.url(filename)
    else:
        file_url = None
    return render_template('upload_post.html', form=form, file_url=file_url)


if __name__ == '__main__':
    app.run()