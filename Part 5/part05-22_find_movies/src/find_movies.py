# Write your solution here
def find_movies(database: list, search_term: str):
    contains = []
    for movie in database:
        if (search_term.lower() in movie["name"].lower()):
            contains.append(movie)
    return contains