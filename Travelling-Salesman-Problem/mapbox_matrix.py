# Brute-Force Search Implementation

import os
from itertools import permutations
from mapbox import DirectionsMatrix
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Use the Mapbox Directions Matrix API to retrieve travel durations (times) between specified locations

# Durations are later converted to distance taking into account an estimated average speed

os.environ['MAPBOX_ACCESS_TOKEN'] = os.getenv('MAPBOX_ACCESS_TOKEN')
service = DirectionsMatrix(access_token=os.getenv('MAPBOX_ACCESS_TOKEN'))

# Define the county headquarters
counties = {
    'Nyeri': 'Nyeri, Kenya',
    'Nakuru': 'Nakuru, Kenya',
    'Laikipia': 'Nanyuki, Kenya',  # Assuming Nanyuki is the headquarters
    'Nandi': 'Kapsabet, Kenya',
    'Meru': 'Meru, Kenya'
}

# Coordinates for each county
county_coordinates = {
    'Nyeri': [36.949290, -0.427780],
    'Nakuru': [36.066180, -0.283330],
    'Laikipia': [37.071980, 0.010410],
    'Nandi': [35.104220, 0.202500],
    'Meru': [37.652390, 0.047960]
}

# Average driving speed (in meters per second)
average_speed = 13

# Convert duration (in seconds) to distance (in kilometers)


def duration_to_distance(duration):
    return (duration * average_speed) / 1000  # Convert meters to kilometers

# Get the distance matrix


def get_distance_matrix(locations):
    coordinates = [county_coordinates[location] for location in locations]
    response = service.matrix(coordinates, profile='mapbox/driving')
    if response.status_code == 200:
        data = response.json()
        print(data)  # Print the entire response for debugging
        if 'durations' in data:
            matrix = data['durations']
            distance_matrix = {}
            for i, start in enumerate(locations):
                for j, end in enumerate(locations):
                    if start != end:
                        distance_matrix[(start, end)] = duration_to_distance(
                            matrix[i][j])
            return distance_matrix
        else:
            print("The 'durations' field is not in the response.")
            return {}
    else:
        print(f"Error: {response.status_code}")
        return {}

# Get the total distance for a specific route


def calculate_route_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[(route[i], route[i + 1])]
    # Return to the starting point
    total_distance += distance_matrix[(route[-1], route[0])]
    return total_distance

# Find the optimal route using brute-force (for simplicity)


def find_optimal_route(locations, distance_matrix):
    min_distance = float('inf')
    optimal_route = None
    for route in permutations(locations):
        distance = calculate_route_distance(route, distance_matrix)
        if distance < min_distance:
            min_distance = distance
            optimal_route = route
    return optimal_route, min_distance


# Main script
locations = list(counties.keys())

try:
    distance_matrix = get_distance_matrix(locations)
    if distance_matrix:
        optimal_route, min_distance = find_optimal_route(
            locations, distance_matrix)

        print("Optimal Route:")
        for location in optimal_route:
            print(location)
        print(f"Total Distance: {min_distance} km")
    else:
        print("Failed to retrieve the distance matrix.")

except Exception as e:
    print(f"An error occurred: {e}")
