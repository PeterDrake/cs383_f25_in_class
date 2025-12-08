from math import inf, sqrt

def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def brute_force_closest(points):
    result = None
    closest_distance = inf
    for i, a in enumerate(points):
        for b in points[i+1:]:
            d = distance(a, b)
            if d < closest_distance:
                result = [a, b]
                closest_distance = d
    return result

# import random
#
# points = [(random.random(), random.random()) for _ in range(100)]
# print(points)
# print(brute_force_closest(points))
