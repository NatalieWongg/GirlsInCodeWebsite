def min_enemies_to_kill(A, B, enemies):
    enemies.sort()  # Sort the enemies by their power level in ascending order
    enemies_killed = 0  # Initialize the number of enemies killed
    while A < B:
        if not enemies:
            return -1  # Alice cannot reach B if no more enemies are available
        enemy_power = enemies.pop()
        A += enemy_power  # Increase Alice's power level
        enemies_killed += 1  # Increment the number of enemies killed
    return enemies_killed

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read input for each test case
    N, A, B = map(int, input().split())
    enemies = list(map(int, input().split()))

    result = min_enemies_to_kill(A, B, enemies)
    print(result)

