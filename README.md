# GeoHackr
Display GeoGuessr locations from a Python notebook. Simply use this notebook in Google Colab to impress your friends, defeat your enemies, and arise victorious! (In GeoGuessr, at least.)

![How to use GeoHackr](./GeoHackr.gif)

_How does it work?_
- Calls to the Google Maps Stree View photos API return a response containing the photo's coordinates.
- These coordinates can be extracted out via regex and displayed in Folium.
