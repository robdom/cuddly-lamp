import os

# os.path.join('Users', 'robertdomingo', 'stp', 'ch09.py')

# I could use pwd, but I guess this is to make sure that the path works on both
# Windows and Unix-like operating systems

with open("st.txt", "w") as f:
    f.write("Hi from Python!")

with open("st.txt", "r") as f:
    print(f.read())

import csv

with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

p = os.path.join('Users', 'robertdomingo', 'stp', 'st.txt')
print(p)

# Challenge 1

with open("st.txt", "r") as f:
    print(f.read())

# Challenge 2

favorite_movie_response = input("What's your favorite movie? ")

with open("favorite_movies.txt", "w") as f:
    f.write(favorite_movie_response)

with open("favorite_movies.txt", "r") as f:
    print(f.read())

# Challenge 3

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

# generate a CSV file
# each row in the CSV file is a list in the list of lists

# import csv

with open("movie_star_movies.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for imdb in movies:
        w.writerow(imdb)

with open("movie_star_movies.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
