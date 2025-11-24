def decode_egg_code(egg_code):
    # Define mappings
    farming_methods = {
        "0": 'Organic',
        "1": 'Free range',
        "2": 'Barn',
        "3": 'Cage'
    }

    countries = {
        'UK': 'United Kingdom',
        'NL': 'Netherlands',
        'FR': 'France',
        'BE': 'Belgium',
        'DE': 'Germany',
        'ES': 'Spain'
    }

    # Extract information from the egg code
    method_code = egg_code[0]
    country_code = egg_code[1:3]
    farm_id = egg_code[3:]

    # Decode information
    farming_method = farming_methods.get(method_code, 'Unknown farming method')
    country = countries.get(country_code, 'Unknown country')

    # Output the results
    print(f"Farming Method: {farming_method}")
    print(f"Country of Origin: {country}")
    print(f"Farm/Producer ID: {farm_id}")

if __name__ == "__main__":
    # Get input from the user
    egg_code = input("Enter the egg code: ")

    # Decode the egg code and print the results
    decode_egg_code(egg_code)

