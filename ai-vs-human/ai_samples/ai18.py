def simulate_pours(capacities, amounts):
    for i in range(100):
        from_bucket = i % 3
        to_bucket = (i + 1) % 3

        # Calculate how much we can pour
        space = capacities[to_bucket] - amounts[to_bucket]
        poured = min(amounts[from_bucket], space)

        # Update the buckets
        amounts[from_bucket] -= poured
        amounts[to_bucket] += poured

    return amounts

# Input: each line contains [capacity, initial_amount]
capacities = [10, 11, 12]
amounts = [3, 4, 5]

# Run simulation
final_amounts = simulate_pours(capacities, amounts)

# Output
for amount in final_amounts:
    print(amount)
