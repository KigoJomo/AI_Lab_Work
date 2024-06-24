from collections import deque

def bfs_tsp(graph, city_names, start):
    n = len(graph)
    min_cost = float('inf')
    best_path = []

    # Queue to store the current path and its cost
    queue = deque([(start, [start], 0)])

    while queue:
        current_city, path, current_cost = queue.popleft()

        # Print the current path
        print(f"Visiting: {' -> '.join(city_names[city] for city in path)}")

        # If all cities have been visited and we can return to the start
        if len(path) == n:
            total_cost = current_cost + graph[current_city][start]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path + [start]
            continue

        # Explore all unvisited neighbors
        for next_city in range(n):
            if next_city not in path and graph[current_city][next_city] > 0:
                queue.append((next_city, path + [next_city], current_cost + graph[current_city][next_city]))

    return best_path, min_cost

# Example usage:
city_names = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Thika"]
# Adjacency matrix representing distances between cities
graph = [
    [0, 29, 20, 21, 17, 30],
    [29, 0, 15, 29, 28, 40],
    [20, 15, 0, 15, 14, 25],
    [21, 29, 15, 0, 14, 24],
    [17, 28, 14, 14, 0, 20],
    [30, 40, 25, 24, 20, 0]
]

start_city = 0  # Nairobi
best_path, min_cost = bfs_tsp(graph, city_names, start_city)
best_path_names = [city_names[city] for city in best_path]

print("\nBest path found:")
print(" -> ".join(best_path_names))
print(f"Minimum cost: {min_cost}")
