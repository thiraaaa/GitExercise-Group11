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

    folium.Marker(location=[2.929632,101.641207], popup="<i>Faculty of Management</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.928741,101.640955], popup="<i>Faculty of Computing & Informatics</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.928909,101.642034], popup="<i>Dewan Tun Chancellor</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.926398,101.641284], popup="<i>Faculty of Engineering</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.925953,101.642993], popup="<i>Faculty of Creative Multimedia/i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.927451,101.641672], popup="<i>Siti Hasmah Digital Library</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.927943,101.642210], popup="<i>Multipurpose Hall</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.928828,101.642894], popup="<i>Inst. Postgraduate</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.929965,101.642164], popup="<i>Admission & International Office</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.925492,101.642163], popup="<i>Student Service Centre</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.927847,101.642989], popup="<i>MMU Starbees</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.925209,101.643949], popup="<i>MMU Hostel HB3</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.924669,101.645518], popup="<i>MMU Hostel HB1</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    folium.Marker(location=[2.924380,101.643015], popup="<i>Surau Al-Hidayah MMU</i>", tooltip="Click Here", icon=folium.Icon(color='red')).add_to(map)

    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)