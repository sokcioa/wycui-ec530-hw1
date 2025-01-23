from match_points import match_points


def main():

    # Example data
    array_a = [
        (52.5200, 13.4050),
        (48.8566, 2.3522),
        (51.5074, -0.1278),
        (40.7128, -74.0060),
        (34.0522, -118.2437)
    ]
    array_b = [
        (41.8781, -87.6298),
        (37.7749, -122.4194),
        (25.7617, -80.1918),
        (47.6062, -122.3321),
        (51.1657, 10.4515)
    ]

    # Match closest points
    closest_indices = match_points(array_a, array_b)

    # Output result
    print("Closest indices:", closest_indices)

if __name__ == "__main__":
    main()

