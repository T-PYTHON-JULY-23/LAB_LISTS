# *bonus* function to calculate average rating for a movie

def calculate_average_rating(ratings):
    return int(sum(ratings) / len(ratings))

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])]


filtered_movies = []
for movie in movies:
    title, release_year, ratings = movie
    avg_rating = calculate_average_rating(ratings)

    if avg_rating >= 6.0:
        filtered_movies.append((title, release_year, avg_rating))

for movie in filtered_movies:
    title, release_year, avg_rating = movie
    print(f"{title} ({release_year}): {avg_rating}")