tv_shows = ["Shark Tank", "The Profit", "Star Trek: The Next Generation", "Key and Peele", "American Ninja Warrior"]

for i, show in enumerate(tv_shows):
    new = tv_shows[i]
    new = new.upper()
    tv_shows[i] = new

print(tv_shows)

x = 10

while x > 0:
  print('{}'.format(x))
  x -= 1

print("Happy New Year!")

while True:
  print("It never ends!!!")


for i in range(0, 6):
    if i == 3:
        continue
    print(i)

# Challenge 1

tv = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for show in tv:
    print(show)

# Challenge 2

for i in range(25, 51):
    print(i)

# Challenge 3

for i, show in enumerate(tv):
    print(show, i)

# Challenge 4

"""
Write a program with an infinite loop (with the option to type q to quit) and a list of numbers. Each time through the loop ask the user to guess a number on the list and tell them whether or not they guessed correctly.
"""

print("Type q to exit")
nums = [1, 2, 3, 4, 5]
while True:
    response = input("Guess a number on the list. ")
    if response == "q":
        break
    elif int(response) in nums:
        print("You guesed right!")
    else:
        print("Try again.")

# Challenge 5

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i * j)

print(list3)
