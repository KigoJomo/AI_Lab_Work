# similar to implementation2, but using mapbox API

import os
from itertools import permutations
from mapbox import DirectionsMatrix

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

os.environ['MAPBOX_ACCESS_TOKEN'] = os.getenv('MAPBOX_ACCESS_TOKEN')
service = DirectionsMatrix()

# Define the county headquarters
counties = {
    'Nyeri': 'Nyeri, Kenya',
    'Nakuru': 'Nakuru, Kenya',
    'Laikipia': 'Nanyuki, Kenya',  # Assuming Nanyuki is the headquarters
    'Nandi': 'Kapsabet, Kenya',
    'Meru': 'Meru, Kenya'
}

# Get coordinates for each county (use a geocoding API if needed)
county_coordinates = {
    'Nyeri': [36.949290, -0.427780],
    'Nakuru': [36.066180, -0.283330],
    'Laikipia': [37.071980, 0.010410],
    'Nandi': [35.104220, 0.202500],
    'Meru': [37.652390, 0.047960]
}

# Get the distance matrix


def get_distance_matrix(locations):
    coordinates = [county_coordinates[location] for location in locations]
    response = service.matrix(coordinates, profile='driving')
    if response.status_code == 200:
        matrix = response.json()['durations']
        distance_matrix = {}
        for i, start in enumerate(locations):
            for j, end in enumerate(locations):
                if start != end:
                    distance_matrix[(start, end)] = matrix[i][j]
        return distance_matrix
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
    optimal_route, min_distance = find_optimal_route(
        locations, distance_matrix)

    print("Optimal Route:")
    for location in optimal_route:
        print(location)
    print(f"Total Distance: {min_distance / 1000} km")

except Exception as e:
    print(f"An error occurred: {e}")
