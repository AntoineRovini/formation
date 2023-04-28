numbers = input("Entrez une liste de nombres séparés par des virgules: ")
numbers_list = [int(x) for x in numbers.split(",")]
average = sum(numbers_list) / len(numbers_list)
print("La moyenne est :", average)
