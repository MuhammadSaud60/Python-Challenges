'''
Write a function euclidean_distance(point1, point2) that:

    Takes two tuples point1 and point2 representing 2D coordinates (e.g., (x1, y1)).

    Returns the Euclidean distance between them, rounded to 2 decimal places.

'''

import math

def euclidean_distance(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    find_euclidean_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    find_euclidean_distance = round(find_euclidean_distance, 2)

    return find_euclidean_distance

point1 = (3, 4)
point2 = (6, 8)

result = euclidean_distance(point1, point2)
print(result)