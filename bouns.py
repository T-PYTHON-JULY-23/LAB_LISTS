

movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
x=3
N=len(movies)
for i in range(0, len(movies)):
    list_rate=movies[i][2]
    average =round(sum(list_rate) / len(list_rate),2)
   # new_list_movies=*movies[i][:2],sep='-'
   
     
    
    print(' - '.join(str(x) for x in movies[i][:2]),"- Avergae rating:",average,"*")
    

       
    
  