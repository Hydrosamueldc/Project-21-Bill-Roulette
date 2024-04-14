import random
users = (input("Enter your names separated with coma: ")).split(",")
buyer = random.choice(users)
print(f"{buyer} is going to pay for the meal today!")
