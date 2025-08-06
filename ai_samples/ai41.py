def count_points_on_line(a, b, coordinates):
    count = 0
    for x, y in coordinates:
        if y == a * x + b:
            count += 1
    return count

# Example usage
a = 2
b = 1
coordinates = [[0, 1], [2, 5], [3, 3]]
print("Output:", count_points_on_line(a, b, coordinates))