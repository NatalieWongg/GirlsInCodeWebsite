N_M=input().split()
N=int(N_M[0])
M=int(N_M[1])
road_segments=[]
journey_segments=[]
road_index=0
journey_index=0
road_position=0
journey_position=0
max_violation =0
for _ in range(N):
    road_data= input().split()
    length=int(road_data[0])
    speed_limit=int(road_data[1])
    road_segments.append((length, speed_limit))
for _ in range(M):
    journey_data=input().split()
    length=int(journey_data[0])
    speed=int(journey_data[1])
    journey_segments.append((length, speed))
while road_index<N and journey_index<M:
    road_length,road_speed=road_segments[road_index]
    journey_length,journey_speed=journey_segments[journey_index]
    overlap=min(road_length-road_position,journey_length- journey_position)
    speed_difference=journey_speed-road_speed
    if speed_difference >max_violation:
        max_violation = speed_difference
    road_position+=overlap
    journey_position+= overlap
    if road_position>=road_length:
        road_index+=1
        road_position= 0
    if journey_position>=journey_length:
        journey_index+=1
        journey_position=0
print(max_violation)