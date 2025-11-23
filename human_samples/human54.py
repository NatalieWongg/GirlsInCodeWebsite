import random
name = ["James", "John", "Mark", "Rick"]
a = 0
while a == 0:
    for i in range (1,5):
        chosen = random.choice(name)
        print(chosen)
        question = input("Would you like to keep this name in the list or not? (type yes or no) : ")
        if question == "no":
            name.remove(chosen)
            continue
        elif question == "yes":
            continue
    