from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import folium

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

places_data = {
    "faculty_management": {
        "name": "Faculty of Management",
        "photos": [{"filename": "", "review": "", "likes": 0}],
    },
    "faculty_computing": {
        "name": "Faculty of Computing & Informatics",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "DTC": {
        "name": "Dewan Tun Chancellor",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "faculty_engineering": {
        "name": "Faculty of Engineering",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "faculty_multimedia": {
        "name": "Faculty of Creative Multimedia",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "SHDL": {
        "name": "Siti Hasmah Digital Library",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "MPH": {
        "name": "Multipurpose Hall",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "inst_postgraduate": {
        "name": "Inst. Postgraduate",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "adm_int_office": {
        "name": "Admission & International Office",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "SSC": {
        "name": "Student Service Centre",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "starbees": {
        "name": "MMU Starbees",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "hostel_HB3": {
        "name": "MMU Hostel HB3",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "hostel_HB4": {
        "name": "MMU Hostel HB1",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    },
    "surau": {
        "name": "Surau Al-Hidayah MMU",
        "photos":[{"filename": "", "review": "", "likes": 0}],
    }
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/map-marker')
def map_marker():
    map = folium.Map(location=[2.9279623186421695, 101.64200330740373], zoom_start=12)
    folium.Marker(location=[2.9279623186421695, 101.64200330740373], popup="<i>MMU Cyberjaya</i>", tooltip="Click Here").add_to(map)

    folium.Marker(location=[2.929632,101.641207], popup=folium.Popup('<a href="/place/faculty_management">Faculty of Management</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    folium.Marker(location=[2.928741,101.640955], popup=folium.Popup('<a href="/place/faculty_computing">Faculty of Computing & Informatics</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    folium.Marker(location=[2.928909,101.642034], popup=folium.Popup('<a href="/place/DTC">Dewan Tun Chancellor</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)

    folium.Marker(location=[2.926398,101.641284], popup=folium.Popup('<a href="/place/faculty_engineering">Faculty of Engineering</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)

    folium.Marker(location=[2.925953,101.642993], popup=folium.Popup('<a href="/place/faculty_multimedia">Faculty of Creative Multimedia</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    folium.Marker(location=[2.927451,101.641672], popup=folium.Popup('<a href="/place/SHDL">Siti Hasmah Digital Library</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)

    folium.Marker(location=[2.927943,101.642210], popup=folium.Popup('<a href="/place/MPH">Multipurpose Hall</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)

    folium.Marker(location=[2.928828,101.642894], popup=folium.Popup('<a href="/place/inst_postgraduate">Inst. Postgraduate</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    folium.Marker(location=[2.929965,101.642164], popup=folium.Popup('<a href="/place/adm_int_office">Admission & International Office</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    folium.Marker(location=[2.925492,101.642163], popup=folium.Popup('<a href="/place/SSC">Student Service Centre</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    folium.Marker(location=[2.927847,101.642989], popup=folium.Popup('<a href="/place/starbees">MMU Starbees</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    folium.Marker(location=[2.925209,101.643949], popup=folium.Popup('<a href="/place/hostel_HB3">MMU Hostel HB3</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    folium.Marker(location=[2.924669,101.645518],popup=folium.Popup('<a href="/place/hostel_HB4">MMU Hostel HB4</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    folium.Marker(location=[2.924380,101.643015], popup=folium.Popup('<a href="/place/surau">Surau Al-Hidayah</a>', max_width=300),
                  icon=folium.Icon(color='red'),
                  tooltip="Click Here").add_to(map)
    
    return map._repr_html_()

@app.route('/place/<place_id>', methods=['GET'])
def place_data(place_id):
    if place_id in places_data:
        return render_template('album.html', place=places_data[place_id], place_id=place_id)
    else:
        return render_template('error.html', message="Place not found"), 404

@app.route('/upload', methods=['POST'])
def upload_file():
    place_id = request.form['place_id']
    review = request.form['review']
    file = request.files.get('file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        places_data[place_id]['photos'].append({
            "filename": filename,
            "review": review,
            "likes": 0 
        })
    else:
         places_data[place_id]['photos'].append({
            "filename": "", 
            "review": review,
            "likes": 0 
        })

    return redirect(url_for('place_data', place_id=place_id))

@app.route('/like_review', methods=['POST'])
def like_review():
    place_id = request.form['place_id']  
    review_index = int(request.form['review_index'])  
    
    if place_id not in places_data:
        print(f"Error: place_id '{place_id}' not found")
        return f"Error: place_id '{place_id}' not found", 400

    if review_index >= len(places_data[place_id]['photos']):
        print(f"Error: review_index '{review_index}' out of range")
        return f"Error: review_index '{review_index}' out of range", 400

    if 'likes' not in places_data[place_id]['photos'][review_index]:
        print(f"Error: 'likes' field not initialized for this review")
        return "Error: 'likes' field not initialized for this review", 400

    places_data[place_id]['photos'][review_index]['likes'] += 1
    print(f"Updated likes for review {review_index} to {places_data[place_id]['photos'][review_index]['likes']}")

    return redirect(url_for('place_data', place_id=place_id))

@app.route('/')
def index():
    return render_template('mmu_map.html')

if __name__ == '__main__':
    app.run(debug=True)