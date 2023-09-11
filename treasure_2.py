print("Welcome to Treasure Island Game.")
print("Your task is to find the treasure. You have only 1 chance to find it. Good luck!")
direct = input("You are at a crossroad. Where do you want to go? Right or Left: ")
if direct=="Right":
    ad=input("There are two houses - Blue and Yellow. Where would you like to go? ")
    if ad=="Blue":
        print("Congratulations! You have found the treasure. You win!")
    elif ad=="Yellow":
        print("You entered the house of fire. Game Over. Sorry, try again.")
    else:
        print("Invalid choice. Game Over. Sorry, try again.")
elif direct=="Left":
    print("You fell into a deep hole. Game Over. Sorry, try again.")
else:
    print("Invalid choice. Game Over. Sorry, try again.")