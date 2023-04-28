import random

number = random.randint(1, 100)
guess = int(input("Devinez un nombre entre 1 et 100: "))
while guess != number:
    if guess < number:
        print("Le nombre est plus grand")
    else:
        print("Le nombre est plus petit")
    guess = int(input("Essayez à nouveau: "))
print("Bravo!")