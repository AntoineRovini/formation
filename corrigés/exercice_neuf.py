import random

words = ["chat", "chien", "maison", "voiture", "ordinateur"]
word = random.choice(words)
guess = input("Devinez un mot: ")
while guess != word:
    if guess[0] == word[0]:
        print("La première lettre est correcte.")
    else:
        print("La première lettre est incorrecte.")
    guess = input("Essayez à nouveau: ")
print("Bravo!")
