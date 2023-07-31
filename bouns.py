movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

movie=0
count=0
for tup in movies:
     count += 1
     for item in tup:
          movie = tup[2]
          sum =0 
          for i in movie:
                sum += i
          average=round(sum/len(movie),2)
     if average <6:
      break

     print(f"{count}. {tup[0]} - ({tup[1]}) - Average rating: {average} *")

        
    
       