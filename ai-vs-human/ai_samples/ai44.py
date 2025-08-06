import math

def oranges_needed(crew, days):
    required = crew  # On the last day, we need 'crew' oranges

    for day in range(days, 0, -1):
        # Before spoilage, the number of oranges must be such that after spoilage,
        # we have 'required' oranges available
        spoilage_rate = 1 - (day / 100)
        if spoilage_rate <= 0:
            raise ValueError("Spoilage rate is 0% or worse. Can't satisfy crew.")
        
        # Reverse spoilage
        before_spoilage = required / spoilage_rate
        
        # Add what the crew will eat next morning
        required = math.ceil(before_spoilage + crew)
    
    return required

# Example input
crew = 25
days = 500
print("Oranges needed:", oranges_needed(crew, days))
