movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def Movie_Ratings_Analysis(movie):
    res = [lis[1] for lis in movie]
    print(str(res))
  
  
Movie_Ratings_Analysis(movies)
"""
    
    # Python3 code to demonstrate
# get nth tuple element from list
# using list comprehension

# initializing list of tuples
test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension to get names
res = [lis[1] for lis in test_list]
	
# printing result
print ("List with only nth tuple element (i.e names) : " + str(res))

    """