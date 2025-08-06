def evens_before_odds(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 != 0]
    return evens + odds