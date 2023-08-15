import random

response = "y"

while response == "y":
    # Roll the dice (generate a random number between 1 and 6)
    dice_value = random.randint(1, 6)
    
    # Print the representation of the dice
    print("-----")
    if dice_value == 1:
        print("|   |")
        print("| o |")
        print("|   |")
    elif dice_value == 2:
        print("|o  |")
        print("|   |")
        print("|  o|")
    elif dice_value == 3:
        print("|o  |")
        print("| o |")
        print("|  o|")
    elif dice_value == 4:
        print("|o o|")
        print("|   |")
        print("|o o|")
    elif dice_value == 5:
        print("|o o|")
        print("| o |")
        print("|o o|")
    else:  # dice_value == 6
        print("|o o|")
        print("|o o|")
        print("|o o|")
    print("-----")
    
    # Ask the user if they want to roll again
    response = input("Roll again? (y/n): ").lower()

print("Goodbye!")