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

    folium.Marker(location=[2.929632,101.641207], popup="<h5>Faculty of Management</h5> <img src='FOM.jpg' width=150>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.928741,101.640955], popup="<h5>Faculty of Computing & Informatics</h5>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.928909,101.642034], popup="<i>Dewan Tun Chancellor</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.926398,101.641284], popup="<i>Faculty of Engineering</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.925953,101.642993], popup="<i>Faculty of Creative Multimedia/i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.927451,101.641672], popup="<i>Siti Hasmah Digital Library</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.927943,101.642210], popup="<i>Multipurpose Hall</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)