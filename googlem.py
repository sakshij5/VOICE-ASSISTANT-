import geopy
import geocoder
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder


def googlemaps(place):
     url_place= "https://www.google.com/maps/place/" + str(place)
     geolocater = Nominatim(user_agent= "myGeocoder")
     location = geolocater.geocode(place,addressdetails= True)
     target_latlon =location.latitude ,location.longitude
     location = location .raw['address']
     target = { city :location.get('city',''),
               state :location.get('state',''),
               country :location.get('country','')}
     current_loca =geocoder.ip('me')
     current_loca = current_loca.latlng
     distance = str(great_circle(current_latlon,target_latlon))
     distance = str(distance.split(' ',1)[0])
     distance = round(float(distance),2)
     web.open(url=url_place)
     speak(target)
     speak(f"maam ,{place} is {distance} kilometer away from you ")
     googlemaps('mumbai')