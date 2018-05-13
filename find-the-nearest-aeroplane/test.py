import urllib.request
import json
import math 

def get_flight_data():
	url  = "https://opensky-network.org/api/states/all"
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	return data["states"]


def euclidean_dist(p, q):
	return math.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)


def haversine_dist(p, q):
	# TBA
	return None


def distance(x, y):
	if (None in (x[0], x[1], y[0], y[1])): 
		return math.inf
	return euclidean_dist(x,y)


def find_nearest_plane(latitude, longitude):
	planes  = get_flight_data()
	nearest = min(planes, key = lambda plane: distance([latitude, longitude], [plane[6], plane[5]]))

	print("Geodesic distance:", euclidean_dist([latitude, longitude], [nearest[6], nearest[5]]))
	print("Callsign:", nearest[1])
	print("Latitude/Longitude:", nearest[6], ",", nearest[5])
	print("Geometric Altitude:", nearest[7])
	print("Country of origin:", nearest[2])
	print("ICA024 ID:", nearest[0])

	return nearest

# Eifel Tower
find_nearest_plane(48.8584, 2.2945)

# John F. Kennedy Airport
find_nearest_plane(40.6413, 73.7781)


#print_plane(find_nearest_plane(48.8584, 2.2945))
