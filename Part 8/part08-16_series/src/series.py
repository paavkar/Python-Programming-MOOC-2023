# Write your solution here:
class Series:

    def __init__(self, title: str, season_count: int, genres: list):
        self.title = title
        self.season_count = season_count
        self.genres = genres
        self.ratings = []

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if(len(self.ratings) > 0):
            grade = sum(self.ratings)/len(self.ratings)
            return(f"{self.title} ({self.season_count} seasons)\ngenres: {genre_string}\n{len(self.ratings)} ratings, average {grade:.1f} points")
        else:
            return(f"{self.title} ({self.season_count} seasons)\ngenres: {genre_string}\nno ratings")
    
    def rate(self, rating: int):
        self.ratings.append(rating)

def minimum_grade(rating: float, series_list: list):
    result = []
    for series in series_list:
        grade = sum(series.ratings)/len(series.ratings)
        if(grade >= rating):
            result.append(series)
    return result

def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        if(genre in series.genres):
            result.append(series)
    return result