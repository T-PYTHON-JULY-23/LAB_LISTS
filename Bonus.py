movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def Movie_Ratings_average(movie):
    count = 1
    for title, year, rating in movie:
        average = round(sum(rating) / len(rating), 1)
        if average > 6:
            print(f"{count}. {title} ({year}) Average: {average} ★")
            count += 1



anayalze_movies(movies)

   
