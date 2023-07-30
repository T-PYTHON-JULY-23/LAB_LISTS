movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def Movie_Ratings_average(movie):
   rating_list = [lis[2] for lis in movie]
  
   sumTval=0
   averageTval=[]
   average=0.0

   for list_val in rating_list:
    lenT= len(list_val)

    countP=0

    for tuple_val in list_val:
         countP+=1
         sumTval+= tuple_val
         if countP>lenT-1 :
            average=sumTval/lenT
            averageTval.append(round(average,2))
            average=0.0
            sumTval =0
   return averageTval

MRaverage = []
MRaverage = Movie_Ratings_average(movies)

LMRaverage= len(MRaverage)
Movie_add_ave = []

for val in range(0,LMRaverage):
   if MRaverage[val]<6.0:
      del MRaverage[val]
      del movies[val]
   else:
      Movie_add_ave.append(movies[val])
      Movie_add_ave.append(MRaverage[val])
LMMovie_add_ave= len(Movie_add_ave)
for val in range(0,LMRaverage):
   print(f"{val+1}. {Movie_add_ave[0]} ({Movie_add_ave[1]}) - Avergae rating: {Movie_add_ave[3]} *")
print(Movie_add_ave)