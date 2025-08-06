def max_speed_excess(n, m, road_segments, driver_segments):
    # Initialize arrays for each mile
    road_limit = [0] * 100
    driver_speed = [0] * 100

    # Fill road speed limits
    idx = 0
    for length, speed in road_segments:
        for _ in range(length):
            road_limit[idx] = speed
            idx += 1

    # Fill driver speeds
    idx = 0
    for length, speed in driver_segments:
        for _ in range(length):
            driver_speed[idx] = speed
            idx += 1

    # Calculate max excess
    max_excess = 0
    for i in range(100):
        excess = driver_speed[i] - road_limit[i]
        if excess > max_excess:
            max_excess = excess

    return max_excess

# Sample Input
n, m = 3, 3
road_segments = [(40, 75), (50, 35), (10, 45)]
driver_segments = [(40, 76), (20, 30), (40, 40)]

# Compute and print output
print(max_speed_excess(n, m, road_segments, driver_segments))  # Output: 5
