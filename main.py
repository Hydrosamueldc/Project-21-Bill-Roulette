import random
users = (input("Enter everyone's name, separated by a coma: ")).split(",")
buyer = random.choice(users)
print(f"{buyer} is going to pay for the meal today!")
