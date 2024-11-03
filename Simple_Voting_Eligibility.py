print("A Program to determine if a user is eligible to vote or not. ")
# Initialize the minimum voting age 
votingAge = 18
# Accept user age 
userage = int(input("Enter your age:    "))
# conditions to check if user is eligible to vote or not 
if 0<= userage < 18:
    print(f"You are {userage} years old. \nYou are not eligible to vote. You must be at least {votingAge} years old")
elif 18 <= userage:
    print(f"You are {userage} years old. \nYou are eligible to vote. ")
    # condition to check if user enter invalid age
else:
    print("Enter a valid age.")