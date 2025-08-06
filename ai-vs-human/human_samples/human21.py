road_details =input("Enter a, b, x, and y: ").split()
a=int(road_details[0])
b=int(road_details[1])
x=int(road_details[2])
y=int(road_details[3])
if b>a:
    max_distance = b - a
else:
    max_distance = a - b
if x>a:
    distance_using_teleporter = x - a
else:
    distance_using_teleporter = a - x

if y> b:
    distance_using_teleporter += y - b
else:
    distance_using_teleporter += b - y

if y > a:
    distance_using_teleporter2 = y - a
else:
    distance_using_teleporter2 = a - y

if x > b:
    distance_using_teleporter2 += x - b
else:
    distance_using_teleporter2 += b - x

min_distance = min(max_distance, distance_using_teleporter, distance_using_teleporter2)
print(min_distance)
