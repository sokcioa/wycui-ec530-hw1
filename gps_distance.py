import math

def gps_distance(coord1, coord2):

    # Earth's radius in kilometers
    EARTH_RADIUS_KM = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    # Calculate the differences
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Haversine formula
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = EARTH_RADIUS_KM * c
    return distance
