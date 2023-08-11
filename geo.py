from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="coordinates_finder")
location = geolocator.geocode("Puerto Morelos")
print(location.address)
print((location.latitude, location.longitude))