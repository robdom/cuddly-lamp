# Wrestling Nickame Generator

def wrestling_nickname_generator():

    nicknames = ["The Hammer", "The Dragon", "The Brooklyn Brawler", "The Anvil", "The Hitman", "Mr. Wonderful", "The Snake"]

    # Find a way to scrape: http://www.legacyofwrestling.com/Nicknames.html

    import random

    first = input("What's your first name? ")
    last = input("What's your last name? ")

    print("Your wrestling name is: {} ".format(first) + "'" + nicknames[random.randint(0, len(nicknames) + 1)] + "'" + " {}".format(last))


wrestling_nickname_generator()

# Challenge 1

for i in range(len("Camus")):
    print("Camus"[i])

# Challenge 2

category_of_writing = input("What did you write yesterday? ")
recipient = input("Who did you send it to? ")

print("Yesterday I wrote a {}. I sent it to {}!".format(category_of_writing, recipient))

# Challenge 3

sentence = "aldous Huxley was born in 1894."
split_sentence = sentence.split()
split_sentence[0]= "Aldous"
sentence = " ".join(split_sentence)
print(sentence)

# Challenge 4

string = "Where now? Who now? When now?"

# How do I create a list with three strings?
print(string.split("?"))


new_list = string.split("? ")
# print(new_list)
first_question = " ".join(new_list.slice(0, 2))
print(first_question)

lst = "Where now? Who now? When now?".split("?")
print(lst)
# Cory's solution is wrong!

# Challenge 5

fox_list = ["The", "fox", "jumped", "over", "the", "fence", "."]

fox_sentence = " ".join(fox_list)

print(fox_sentence)

# Challenge 6

print("A screaming comes across the sky.".replace("s", "$"))

# Challenge 7

print("Hemingway".index("m"))

# Challenge 8

# I didn't understand the question. Cory was trying to illustrate escaping a string.""

# Challenge 9

print("three " + "three " + "three")
print(("three " * 3).strip())

# Challenge 10

print("It was a bright cold day in April, and the clocks were striking thirteen."[0:33])
