#Q1: Write a function that takes a list as a parameter, and then returns the sum of all the items in that list.

list1 = [2, 3, 4, 5, 15, 1, 43, 20]

def sum_oflist (list1):
    total = sum(list1)
    return total
print(f" sum of the element: {sum_oflist(list1)}")

 
#use list slicing to get a new list from the previous list (odd numbers list) starting from the start to the 5th element in the list.
nwe_list = list1[:6]
print(nwe_list)



#Write a function that takes a list as a parameter, and then returns the largest number from a list of numbers.
def max_list (list1):
    largest = max(list1)
    return largest 
print(f"the largest number: {max_list(list1)}")



# Create an odd numbers list from the elements of a range from 1200 to 2000 with steps of 125, using [ List Comprehension ].
odd_number_list = [number for number in range(1200,2000,125) if number%2!=0]
print(odd_number_list)


# Bonus

## Movie Ratings Analysis
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


#Calculates the average rating for each movie.


def analysis_movie(movies: list):
    count = 1
    for title, year, rating in movies:
        average = round(sum(rating) / len(rating),1)

        if average > 6:
            print(f"{title}({year}) average : {average} ")
            count +=1

analysis_movie(movies)





