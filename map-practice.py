from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def base():
    map = folium.Map(location=[2.9279623186421695, 101.64200330740373])
    return map._repr_html_()

@app.route("/map.marker")
def map_marker():
     map = folium.Map(location=[2.9279623186421695, 101.64200330740373], tiles='Stamen Terrain', zoom_start=12)
    
    folium.Marker(location=[2.9279623186421695, 101.64200330740373], popup="<i>MMU Cyberjaya</i>", tooltip="Click Here").add_to(map)
    
    return map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)
