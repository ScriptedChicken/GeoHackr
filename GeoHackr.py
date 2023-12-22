import requests
import re
import folium


def return_clean_coordinates(match_str):
    match_list = match_str.replace("null", "").strip("][").split(",")
    return match_list[2:]


def return_coordinates(text):
    matches = re.findall(r"\[null[0-9a-z,.\- ]*\]", text)
    return [return_clean_coordinates(match_str) for match_str in matches]


def return_coordinate_address(coords):
    url = f"https://nominatim.openstreetmap.org/search.php?q={coords[0]},{coords[1]}&format=json"
    res = requests.get(url)
    coordinate_address = res.json()[0].get("display_name")
    return coordinate_address


url = input("Paste URL: ")
res = requests.get(url)
text = res.text
coordinates = return_coordinates(text)

folium_map = None
for coords in coordinates:
    try:
        folium_map = folium.Map(location=coords, zoom_start=15)
        folium.Marker(
            location=coords,
            fill_color="#43d9de",
            radius=8,
            popup=return_coordinate_address(coords),
        ).add_to(folium_map)
        break
    except:
        pass

folium_map
