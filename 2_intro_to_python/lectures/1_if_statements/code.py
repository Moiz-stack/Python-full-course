# Initial greeting
friend = "Moiz"
user_name = input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
else:
    print("Hello, stranger!")

# -- Checking whether the if statement will run --

print(bool(user_name == friend))  # if this is True, the if statement will run

# -- Using the `in` keyword --

# Updated list of friends and family
friends = ["Moiz", "Sharjeel", "Nauman", "Ali Sheikh"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")
