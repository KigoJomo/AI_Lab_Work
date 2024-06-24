# Iterative Deepening Search

def ids_tsp(graph, city_names, start):
    n = len(graph)
    best_path = []
    min_cost = float('inf')

    def dls(current_city, current_cost, path, depth_limit):
        nonlocal min_cost, best_path

        if len(path) > depth_limit:
            return

        # Print the current path
        print(f"Visiting: {' -> '.join(city_names[city] for city in path)}")

        # Base case: If all cities are visited, return to start
        if len(path) == n and graph[current_city][start] > 0:
            total_cost = current_cost + graph[current_city][start]
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path + [start]
            return

        # Recursive case: Visit all unvisited neighbors within the depth limit
        for next_city in range(n):
            if next_city not in path and graph[current_city][next_city] > 0:
                dls(next_city, current_cost +
                    graph[current_city][next_city], path + [next_city], depth_limit)

    depth_limit = 0
    while True:
        print(f"\nDepth limit: {depth_limit}")
        dls(start, 0, [start], depth_limit)
        if best_path:
            break
        depth_limit += 1

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
best_path, min_cost = ids_tsp(graph, city_names, start_city)
best_path_names = [city_names[city] for city in best_path]

print("\nBest path found:")
print(" -> ".join(best_path_names))
print(f"Minimum cost: {min_cost}")
