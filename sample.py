import random

print("🏰 Welcome to The Legend of Python!")
print("You are a brave adventurer exploring the Caves of Code.\n")

#Variables
health = 10
gold = 0

#Game Loop
while health > 0:
    print(f"\n health {health} | gold {gold}")
    print("You see two paths ahead:")
    print("1. Enter the dark cave")
    print("2. Walk down the bright path")
    print("3. Quit the adventure")
    
    choice = input("What do you do? (1/2/3): ")
    
    if choice == "1":
        print("\n🕷️ You enter the cave...")
        encounter = random.choice(["monster", "treasure", "trap"])
        if encounter == "monster":
            print("A wild monster appears!")
            action = input("Do you want to (1) fight or (2) flee? ")
            if action == "1":
                print("You bravely fight the monster!")
                health -= 5
                gold += 10
            else:
                print("You flee back to safety!")
        elif encounter == "treasure":
            print("You found a treasure chest!")
            gold += 20
        else:
            print("You fell into a trap!")
            health -= 10
    elif choice == "2":
        print("\n🌞 You walk down the bright path...")
        encounter = random.choice(["friendly animal", "hidden treasure", "nothing"])
        if encounter == "friendly animal":
            print("You encounter a friendly animal!")
            action = input("Do you want to (1) pet it or (2) ignore it? ")
            if action == "1":
                print("The animal gives you a gold coin!")
                gold += 1
            else:
                print("You walk past the animal.")
        elif encounter == "hidden treasure":
            print("You found a hidden treasure!")
            gold += 50
        else:
            print("You find nothing of interest.")
    elif choice == "3":
        print("Thank you for playing! Your adventure ends here.")
        break

    else:
        print("❌ Invalid choice, try again.")

# End of game
if health <= 0:
    print("\n💀 You collapsed in the caves... Game Over.")
else:
    print(f"\n🎉 Final Score: {gold} gold, {health} health left.")
    print("Thanks for playing!")     