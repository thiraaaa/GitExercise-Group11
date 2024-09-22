from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def base():
    map = folium.Map(location=[2.9279623186421695, 101.64200330740373])
    return map._repr_html_()

@app.route("/map-marker")
def map_marker():
    map = folium.Map(location=[2.9279623186421695, 101.64200330740373], zoom_start=12)
    folium.Marker(location=[2.9279623186421695, 101.64200330740373], popup="<i>MMU Cyberjaya</i>", tooltip="Click Here").add_to(map)

    folium.Marker(location=[2.929632,101.641207], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'faculty_management\')">Faculty of Management</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.928741,101.640955], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'faculty_computing\')">Faculty of Computing & Informatics</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.928909,101.642034], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'DTC\')">Dewan Tun Chancellor</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.926398,101.641284], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'faculty_engineering\')">Faculty of Engineering</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.925953,101.642993], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'faculty_multimedia\')">Faculty of Creative Multimedia</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.927451,101.641672], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'SHDL\')">Siti Hasmah Digital Library</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.927943,101.642210], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'MPH\')">Multipurpose Hall</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.928828,101.642894], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'inst_postgraduate\')">Inst. Postgraduate</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.929965,101.642164], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'adm_int_office\')">Admission & International Office</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.925492,101.642163], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'SSC\')">Student Service Centre</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.927847,101.642989], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'starbees\')">MMU Starbees</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.925209,101.643949], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'hostel_HB3\')">MMU Hostel HB3</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.924669,101.645518], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'hostel_HB1\')">MMU Hostel HB1</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    folium.Marker(location=[2.924380,101.643015], tooltip="Click Here",popup=folium.Popup('<a href="#" onclick="loadAlbum(\'surau\')">Surau Al-Hidayah</a>', max_width=300, icon=folium.Icon(color='red'))).add_to(map)

    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)