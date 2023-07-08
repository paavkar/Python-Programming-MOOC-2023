# Write your solution here
# Remember the import statement
from datetime import date

def list_years(dates: list):
    years = []
    for item in dates:
        years.append(item.year)
    sorted_years = sorted(years)
    return sorted_years