# Exercise 1

favorite_musicians = ["Sting", "Richard Marx", "Ariana Grande", "Daft Punk"]

# Exercise 2

phnom_penh = (11.55, 104.916667)
toronto = (43.65, -79.383333)
prague = (50.1, 14.433333)
cairo = (30.05, 31.25)
london = (1.5, -0.166667)
paris = (48.866667, 2.333333)
vienna = (48.2, 16.366667)
berlin = (52.533333, 13.416667)

cities_visited = (phnom_penh, toronto, prague, cairo, london, paris, vienna, berlin)

print(cities_visited)

# Exercise 3

robert = {"height": (62,), "eye_color": "brown", "birth_country": "USA",
    "favorite_book": "Sum"}

# Exercise 4

def ask_rob_anything(question):
    """
    Returns different values from robert dictionary based on user input.
    :question: string.
    Returns str or int based on user input.
    """
    if question == "How tall are you, in inches?"
        return robert["height"]
    elif question == "What color are your eyes?":
        return robert["eye_color"]
    elif question == "What country were you born in?":
        return robert["birth_country"]
    elif question == "What is your favorite book?":
        return robert["favorite_book"]
    else:
        return "Try asking a different question."

response = input("Ask a question. ")
print(ask_rob_anything(response))

# Exercise 5

favorite_musicians_and_songs = {"Sting": ["All This Time", "We'll Be Together", "Sister Moon"], "Richard Marx": ["Should've Known Better", "Right Here Waiting"], "Ariana Grande": ["Into You", "Side to Side"], "Daft Punk": ["One More Time"]}

# Exercise 6
# When would you use a set?

"""
A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference.

See: https://www.programiz.com/python-programming/set

"""



