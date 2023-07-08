# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def ratings_sort(item: dict):
        return item["rating"]
    return sorted(items, key=ratings_sort, reverse=True)