class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def sort_by_length(routes: list):
    def length_sort(item: ClimbingRoute):
        return item.length
    return sorted(routes, key=length_sort, reverse=True)

def sort_by_difficulty(routes: list):
    def difficulty_sort(item: ClimbingRoute):
        return item.grade, item.length
    return sorted(routes, key=difficulty_sort, reverse=True)