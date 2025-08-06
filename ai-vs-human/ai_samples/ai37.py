def calculate_percentage(student, answer):
    total_questions = len(answer)
    score = 0

    for s, a in zip(student, answer):
        if s == a:
            score += 5
        else:
            score -= 1

    total_marks = total_questions * 5
    percentage = round((score / total_marks) * 100)
    return percentage

# Example usage
student = "AAAA"
answer = "ABCD"
print("Output:", calculate_percentage(student, answer))
