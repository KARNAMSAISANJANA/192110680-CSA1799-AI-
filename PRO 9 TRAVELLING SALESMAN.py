import itertools

def tsp(cities):
    """
    Solve the traveling salesman problem using brute force.
    Cities is a list of tuples (x, y) representing the x and y coordinates of each city.
    """
        distances = [[
        ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5
        for c2 in cities
    ] for c1 in cities]

    permutations = list(itertools.permutations(range(len(cities))))

    paths = [
        sum(distances[perm[i]][perm[i+1]] for i in range(len(perm) - 1)) +
        distances[perm[-1]][perm[0]]
        for perm in permutations
    ]
    return min(paths)
