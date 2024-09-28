#from collections import namedtuple
#from itertools import combinations
#from math import sqrt
#
#
#Point = namedtuple('Point', 'x y')
#
#
#def distance_squared(first_point, second_point):
#    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2
#
#
#def minimum_distance_squared_naive(points):
#    min_distance_squared = float("inf")
#
#    for p, q in combinations(points, 2):
#        min_distance_squared = min(min_distance_squared,
#                                   distance_squared(p, q))
#
#    return min_distance_squared
#
#
#if __name__ == '__main__':
#    input_n = int(input())
#    input_points = []
#    for _ in range(input_n):
#        x, y = map(int, input().split())
#        input_point = Point(x, y)
#        input_points.append(input_point)
#
#    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))

from collections import namedtuple
from math import sqrt
import sys

Point = namedtuple('Point', 'x y')

def distance_squared(p1, p2):
    """Returns the squared distance between two points."""
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

def closest_pair_strip(strip, d):
    """Find the closest pair in the strip of points within distance d."""
    min_dist = d
    size = len(strip)
    
    # Compare every point in the strip with the next 7 points
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) ** 2 < min_dist:
            min_dist = min(min_dist, distance_squared(strip[i], strip[j]))
            j += 1
    
    return min_dist

def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
    """Find the closest pair of points using divide and conquer."""
    n = len(points_sorted_by_x)
    
    # Base case: when number of points is small, use brute force
    if n <= 3:
        return minimum_distance_squared_naive(points_sorted_by_x)
    
    # Divide the points into two halves
    mid = n // 2
    left_x = points_sorted_by_x[:mid]
    right_x = points_sorted_by_x[mid:]
    
    midpoint = points_sorted_by_x[mid].x
    
    left_y = list(filter(lambda p: p.x <= midpoint, points_sorted_by_y))
    right_y = list(filter(lambda p: p.x > midpoint, points_sorted_by_y))
    
    # Recursively find the smallest distance in both halves
    d1 = closest_pair_recursive(left_x, left_y)
    d2 = closest_pair_recursive(right_x, right_y)
    d = min(d1, d2)
    
    # Check the points in the strip
    strip = [p for p in points_sorted_by_y if abs(p.x - midpoint) ** 2 < d]
    d_strip = closest_pair_strip(strip, d)
    
    return min(d, d_strip)

def minimum_distance_squared_naive(points):
    """Calculate minimum distance in a naive way for small number of points."""
    min_distance_squared = float("inf")
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            min_distance_squared = min(min_distance_squared, distance_squared(points[i], points[j]))
    return min_distance_squared

def closest_pair(points):
    """Wrapper function to find closest pair."""
    points_sorted_by_x = sorted(points, key=lambda p: p.x)
    points_sorted_by_y = sorted(points, key=lambda p: p.y)
    return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    
    result = sqrt(closest_pair(input_points))
    print(f"{result:.9f}")
