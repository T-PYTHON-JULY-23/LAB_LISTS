movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

for i in movies :
    j = sum(i[2])
    f = len(i[2])
    the_avarge_rate = j/f
    if the_avarge_rate > 6 :
        print(f"{i[0]} ({i[1]}) - Avergae rating : {round(the_avarge_rate,2)}★")