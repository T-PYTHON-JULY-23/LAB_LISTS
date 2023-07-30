from lab import sum

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

while input("You want to add movie ? 'y'Yes or 'n'No :").lower() != 'n':
    title = input("please enter the movie title :")
    release_year =  input("please enter the release year :")
    user_ratings =  input("please enter the user ratings at least 6 with and seprate by ',' :")
    digit_user_ratings = []
    for rate in user_ratings:
        if rate.isdigit(): 
            digit_user_ratings.append(int(rate))
    movie = title, release_year, digit_user_ratings
    movies.append(movie)

# print(movies)
i= 1
for movie in movies:
    rating = round(sum(movie[-1])/6, 2)
    if rating >= 6:
        print(f"{i}. {movie[0]} ({movie[1]}) - Avergae rating: {rating} ★")
        i += 1