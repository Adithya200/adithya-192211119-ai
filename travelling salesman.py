import itertools

def calculate_distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5
def total_distance(path, cities):
    distance = 0
    for i in range(len(path) - 1):
        distance += calculate_distance(cities[path[i]], cities[path[i + 1]])
    distance += calculate_distance(cities[path[-1]], cities[path[0]])  # Return to the starting city
    return distance
def tsp(cities):
    num_cities = len(cities)
    min_distance = float('inf')
    min_path = None
    all_permutations = itertools.permutations(range(num_cities))
    for path in all_permutations:
        distance = total_distance(path, cities)
        if distance < min_distance:
            min_distance = distance
            min_path = path

    return min_path, min_distance
cities = [(0, 0), (1, 2), (3, 1), (5, 2)]
shortest_path, shortest_distance = tsp(cities)
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
