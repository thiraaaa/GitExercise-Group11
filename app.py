from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Model to store image data
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    likes = db.Column(db.Integer, default=0)
    saved = db.Column(db.Boolean, default=False)

# Define routes and logic for image upload, display, and liking
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join('static/uploads', filename))
            new_image = Image(filename=filename)
            db.session.add(new_image)
            db.session.commit()
            return redirect(url_for('index'))
    images = Image.query.all()
    return render_template('index.html', images=images)

@app.route('/image/<int:image_id>', methods=['GET', 'POST'])
def view_image(image_id):
    image = Image.query.get_or_404(image_id)
    if request.method == 'POST':
        if 'like' in request.form:
            image.likes += 1
        elif 'save' in request.form:
            image.saved = True
        db.session.commit()
        return redirect(url_for('view_image', image_id=image.id))
    return render_template('view_images.html', image=image)

# Serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure this is inside the app context
    app.run(debug=True)
