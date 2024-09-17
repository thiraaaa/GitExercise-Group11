import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Set the upload folder path for photos and videos
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS_PHOTO = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS_VIDEO = {'mp4'}

# Temporary storage for posts (can be replaced with a database later)
posts = []

# Check if file extension is allowed
def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/')
def index():
    return render_template('base.html', posts=posts)

@app.route('/add_content', methods=['GET', 'POST'])
def add_content():
    if request.method == 'POST':
        name = request.form['name']
        review = request.form['review']
        photo = request.files['photo']
        video = request.files['video']

        # Validate inputs
        if not name or not review:
            flash('Location name and review are required!', 'error')
            return redirect(url_for('add_content'))

        # Handle photo upload
        photo_filename = None
        if photo and allowed_file(photo.filename, ALLOWED_EXTENSIONS_PHOTO):
            photo_filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

        # Handle video upload
        video_filename = None
        if video and allowed_file(video.filename, ALLOWED_EXTENSIONS_VIDEO):
            video_filename = secure_filename(video.filename)
            video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))

        # Save the post
        posts.append({
            'name': name,
            'review': review,
            'photo': photo_filename,
            'video': video_filename
        })
        flash(f'Content for "{name}" posted successfully!', 'success')
        return redirect(url_for('base'))

    return render_template('post.html')

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)