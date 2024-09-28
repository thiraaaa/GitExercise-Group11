from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from models import db, Place, Photo
import os
import folium

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)

initialized = False

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.before_request
def create_tables():
    global initialized
    if not initialized:
        db.create_all()
        if not Place.query.first():  # Only add places if the database is empty
             sample_places = [
                 Place(name="Faculty of Management"),
                Place(name="Faculty of Computing & Informatics"),
                Place(name="Dewan Tun Chancellor"),
                Place(name="Faculty of Engineering"),
                Place(name="Faculty of Creative Multimedia"),
                Place(name="Siti Hasmah Digital Library"),
                Place(name="Multipurpose Hall"),
                Place(name="Inst. Postgraduate"),
                Place(name="Admission & International Office"),
                Place(name="Student Service Centre"),
                Place(name="MMU Starbees"),
                Place(name="MMU Hostel HB3"),
                Place(name="MMU Hostel HB1"),  
                Place(name="Surau Al-Hidayah MMU")
            ]  
        db.session.add_all(sample_places)
        db.session.commit()
    initialized = True

@app.route('/map-marker')
def map_marker():
    map = folium.Map(location=[2.9279623186421695, 101.64200330740373], zoom_start=12)
    folium.Marker(location=[2.9279623186421695, 101.64200330740373], popup="<i>MMU Cyberjaya</i>", tooltip="Click Here").add_to(map)

    places= Place.query.all()

    coordinates_list = [ [2.929632,101.641207], [2.928741,101.640955], [2.928909,101.642034], [2.926398,101.641284], [2.925953,101.642993], [2.927451,101.641672], [2.927943,101.642210], 
                   [2.928828,101.642894], [2.929965,101.642164], [2.925492,101.642163], [2.927847,101.642989], [2.925209,101.643949], [2.924669,101.645518], [2.924380,101.643015] ]
    
    for place, coordinates in zip(places, coordinates_list):
        folium.Marker(location=coordinates, popup=folium.Popup(f'<a href="/place/{place.id}">{place.name}</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
       
    return map._repr_html_()

@app.route('/place/<int:place_id>', methods=['GET'])
def place_data(place_id):
    place = Place.query.get_or_404(place_id)
    return render_template('album.html', place=place, place_id=place_id)
   
@app.route('/upload', methods=['POST'])
def upload_file():
    place_id = request.form['place_id']
    review = request.form['review']
    file = request.files.get('file')

    print(f"Place ID: {place_id}")

    place = Place.query.get_or_404(place_id)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_photo = Photo(filename=filename, review=review, place=place)
    else:
        new_photo = Photo(review=review, place=place)

    db.session.add(new_photo)
    db.session.commit()

    return redirect(url_for('place_data', place_id=place_id))

@app.route('/like_review', methods=['POST'])
def like_review():
    photo_id = request.form['photo_id']  
    photo = Photo.query.get_or_404(photo_id)
    
    photo.likes += 1
    db.session.commit()

    return redirect(url_for('place_data', place_id=photo.place_id))

@app.route('/')
def index():
    return render_template('mmu_map.html')

if __name__ == '__main__':
    app.run(debug=True)