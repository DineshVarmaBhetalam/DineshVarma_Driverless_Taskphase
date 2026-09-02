ref_input = input("Enter reference point x and y (e.g., '0 0'): ").split()
ref_point = (float(ref_input[0]), float(ref_input[1]))

points = [(4, 5), (1, 1), (-1, -1), (10, 10), (2, 0)]

def squared_distance(point, reference):
    dx = point[0] - reference[0]
    dy = point[1] - reference[1]
    return (dx ** 2) + (dy ** 2)

sorted_points = sorted(points, key=lambda p: squared_distance(p, ref_point))

print(f"\nReference point: {ref_point}")
print("Points sorted by proximity:")
print(sorted_points)


