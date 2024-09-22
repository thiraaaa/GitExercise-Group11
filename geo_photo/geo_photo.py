from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

places_data = {
    "faculty_management": {
        "name": "Faculty of Management",
        "photos": [{"filename": "", "review": ""}],
        "videos": []
    },
    "faculty_computing": {
        "name": "Faculty of Computing & Informatics",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "DTC": {
        "name": "Dewan Tun Chancellor",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "faculty_engineering": {
        "name": "Faculty of Engineering",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "faculty_multimedia": {
        "name": "Faculty of Creative Multimedia",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "SHDL": {
        "name": "Siti Hasmah Digital Library",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "MPH": {
        "name": "Multipurpose Hall",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "inst_postgraduate": {
        "name": "Inst. Postgraduate",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "adm_int_office": {
        "name": "Admission & International Office",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "SSC": {
        "name": "Student Service Centre",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "starbees": {
        "name": "MMU Starbees",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "hostel_HB3": {
        "name": "MMU Hostel HB3",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "hostel_HB4": {
        "name": "MMU Hostel HB1",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    },
    "surau": {
        "name": "Surau Al-Hidayah MMU",
        "photo":[{"filename": "", "review": ""}],
        "videos": []
    }
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/mmu-map')
def mmu_map():
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