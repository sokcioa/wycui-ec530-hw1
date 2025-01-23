# Functions
## 1. gps_distance
### Description: Calculates the great-circle distance (in kilometers) between two points on Earth using the Haversine formula.
### Input: Two tuples, each representing GPS coordinates in the format (latitude, longitude), where latitude is in the range [-90, 90] and longitude is in the range [-180, 180].
### Output: A float representing the distance between the two points in kilometers.

## 2. match_points
### Description: Matches each point in the first array of GPS coordinates to the closest point in the second array.
### Input:
array_a: A list of tuples, where each tuple represents a GPS coordinate (latitude, longitude).
array_b: A list of tuples, where each tuple represents a GPS coordinate (latitude, longitude).
### Output: A list of integers, where each integer corresponds to the index of the closest point in array_b for each point in array_a.

## 3. main
### Description: Demonstrates the usage of gps_distance and match_points by processing example GPS coordinate arrays.
### Output: Prints a list of indices representing the closest matches from one array to another.
