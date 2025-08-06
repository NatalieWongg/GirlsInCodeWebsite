def find_middle_entity(spectral_entities):
    # Sort by power level in descending order
    sorted_entities = sorted(spectral_entities, key=lambda x: x[1], reverse=True)

    # Find the middle index
    middle_index = len(sorted_entities) // 2

    # Return the name of the middle entity
    return sorted_entities[middle_index][0]

# Example usage
spectral_entities = [["Banshee", 5], ["Wraith", 8], ["Ghost", 3], ["Vampire", 7], ["Zombie", 4]]
result = find_middle_entity(spectral_entities)
print("Output:", result)
