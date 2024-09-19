from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

places_data = {
    "place_1": {
        "name": "Faculty of Management",
        "photos": [],
        "videos": []
    },
    "place_2": {
        "name": "Faculty of Computing & Informatics",
        "photo":[],
        "videos": []
    },
    "place_3": {
        "name": "Dewan Tun Chancellor",
        "photo":[],
        "videos": []
    },
    "place_4": {
        "name": "Faculty of Engineering",
        "photo":[],
        "videos": []
    },
    "place_5": {
        "name": "Faculty of Creative Multimedia",
        "photo":[],
        "videos": []
    },
    "place_6": {
        "name": "Siti Hasmah Digital Library",
        "photo":[],
        "videos": []
    },
    "place_7": {
        "name": "Multipurpose Hall",
        "photo":[],
        "videos": []
    },
    "place_8": {
        "name": "Inst. Postgraduate",
        "photo":[],
        "videos": []
    },
    "place_9": {
        "name": "Admission & International Office",
        "photo":[],
        "videos": []
    },
    "place_10": {
        "name": "Student Service Centre",
        "photo":[],
        "videos": []
    },
    "place_11": {
        "name": "MMU Starbees",
        "photo":[],
        "videos": []
    },
    "place_12": {
        "name": "MMU Hostel HB3",
        "photo":[],
        "videos": []
    },
    "place_13": {
        "name": "MMU Hostel HB1",
        "photo":[],
        "videos": []
    },
    "place_14": {
        "name": "Surau Al-Hidayah MMU",
        "photo":[],
        "videos": []
    }
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('mmu_map.html')

@app.route('/place/<place_id>', methods=['GET'])
def place_data(place_id):
    if place_id in places_data:
        return jsonify(places_data[place_id])
    return jsonify({"error": "Place not found"}), 404

@app.route('/upload', methods=['POST'])
def upload_file():
    place_id = request.form['place_id']
    review = request.form['review']
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Save file and review data
        if filename.split('.')[-1].lower() in {'mp4'}:
            places_data[place_id]['videos'].append(filename)
        else:
            places_data[place_id]['photos'].append({
                "filename": filename,
                "review": review
            })

        return redirect(url_for('index'))
    return 'File not allowed', 400

if __name__ == '__main__':
    app.run(debug=True)