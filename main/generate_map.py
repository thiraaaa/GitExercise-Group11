import folium
import os

if not os.path.exists('templates'):
    os.makedirs('templates')

map = folium.Map(location=[2.9279623186421695, 101.64200330740373], zoom_start=15)

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

map.save('templates/map.html')