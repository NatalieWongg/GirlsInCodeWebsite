def simulate_alomomofa_growth(n):
    alomomofa = 1          # Initial number of alomomofa
    alomomoja = 0          # Initial number of alomomoja
    breeding_rate = 3      # Each alomomofa breeds 3 per minute
    merge_threshold = 20   # 20 alomomofa merge into 1 alomomoja

    for _ in range(n):
        # Reproduction step
        alomomofa *= (1 + breeding_rate)
        
        # Merging step
        newly_merged = alomomofa // merge_threshold
        alomomoja += newly_merged
        alomomofa %= merge_threshold

    print(alomomofa)
    print(alomomoja)

# Example usage
simulate_alomomofa_growth(10000000)
