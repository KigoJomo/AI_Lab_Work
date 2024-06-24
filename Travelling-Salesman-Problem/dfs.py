def dfs_tsp(graph, city_names, start):
    n = len(graph)
    visited = [False] * n
    best_path = []
    min_cost = float('inf')

    def dfs(current_city, current_cost, path, depth):
        nonlocal min_cost, best_path
        # Print the current path
        print(f"Visiting: {' -> '.join(city_names[city] for city in path)}")

        # Base case: All cities are visited, return to start
        if depth == n and graph[current_city][start] > 0:
            current_cost += graph[current_city][start]
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path + [start]
            return

        # Recursive case: Visit all unvisited neighbors
        for next_city in range(n):
            if not visited[next_city] and graph[current_city][next_city] > 0:
                visited[next_city] = True
                dfs(next_city, current_cost + graph[current_city][next_city], path + [next_city], depth + 1)
                visited[next_city] = False

    # Start DFS from the starting city
    visited[start] = True
    dfs(start, 0, [start], 1)

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
best_path, min_cost = dfs_tsp(graph, city_names, start_city)
best_path_names = [city_names[city] for city in best_path]

print("\nBest path found:")
print(" -> ".join(best_path_names))
print(f"Minimum cost: {min_cost}")
