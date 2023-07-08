# Write your solution here
def formatted(numbers: list):
    result = []
    for item in numbers:
        result.append(f"{item:.2f}")
    return result