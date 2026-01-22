def calculate_percentage(marks):
    return sum(marks) / len(marks)

def get_result(percentage):
    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Class"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Fail"

marks = [78, 82, 69, 74, 88]

percentage = calculate_percentage(marks)
result = get_result(percentage)

print("Percentage:", percentage)
print("Result:", result)
