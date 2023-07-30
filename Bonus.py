# Bonus

## Movie Ratings Analysis

movies = [
    ("What Happeend To Monday", 2017, [9, 7, 7, 9, 8, 9]),
    ("oppenheimer", 2023, [10, 9, 9, 10, 9, 10]),
    ("Blue Strak", 1999, [4, 3, 5, 6, 6, 5]),
    ("seven", 1995, [10, 9, 9, 8, 9, 10]),
    ("Identity", 2003, [8, 9, 9, 7, 6, 8]),
    ("Top Gun", 2022, [2, 4, 3, 6, 5, 3])
]
for i,movie in enumerate(movies):
    title , year , ratings = movie
    avg_rating = sum(ratings)/len(ratings)
    if avg_rating>= 6:
        print(f"{i+1}.{title}({ year})- Average rating:{round(avg_rating ,2)}★")