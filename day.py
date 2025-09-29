
def start_game():
    print("🌞 Good morning! Welcome to your adventure: A Day in the Life.")
    name = input("First things first, what's your name? ")

    print(f"\nNice to meet you, {name}! Let's begin your day...")
    morning_routine(name)

def morning_routine(name):
    print("\n⏰ It's 7:00 AM. Your alarm is ringing.")
    print("1. Hit snooze and sleep more 😴")
    print("2. Get up and start your morning 🚿")

    choice = input("What do you want to do? (1/2): ")

    if choice == '1':
        print("\n You snoozed...Snoozed and now you're late for college")
        school_or_college(name, late=True)
    elif choice == '2':
        print("\nYou got up and feel refreshed!")
        school_or_college(name, late=False)
    else:
        print("Invalid choice. Please try again.")
        morning_routine(name)

def school_or_college(name, late):
    if late:
        print("\n🏫 You're late for college! You rush to get ready and leave the house.")
        print("1. Run and skip breakfast 🏃‍♂️")
        print("2. Take it slow and have breakfast 🍞")
    else:
        print("\n🏫 You have time to get ready and leave for college.")
        print("1. Have a healthy breakfast 🍳")
        print("2. Skip breakfast and leave early 🚶‍♂️")

    choice = input("What do you want to do? (1/2): ")
 
    if choice == "1":
        print("\nYou rush to class. The teacher notices your effort.")
        afternoon(name)
    elif choice == "2":
        print("\nYou enjoy a delicious breakfast. But you're a little late.")
        afternoon(name)
    else:
        print("Invalid choice. Try again.")
        school_or_college(name, late)
def afternoon(name):
    print("\n☀️ Afternoon arrives. You finished your morning classes.")
    print("What do you want to do now?")
    print("1. Go to the library 📚")
    print("2. Hang out with friends 🎉")
    print("3. Take a nap 🛏️")

    choice = input("Choose 1, 2, or 3: ")

    if choice == '1':
        print ("\n You study hard and ace your exams!")
    elif choice == '2':
        print("\nYou had a great time with your friends!")
    elif choice == '3':
        print("\nYou took a refreshing nap and feel energized!")
    else:
        print("Invalid choice. Please try again.")
        afternoon(name)
    evening(name)
def evening(name):
    print("\n🌆 Evening falls. Time to wind down.")
    print("1. Cook a nice dinner 🍲")
    print("2. Order takeout 🍕")
    print("3. Go for a walk 🚶‍♂️")

    choice = input("What do you want to do? (1/2/3): ")

    if choice == '1':
        print("\nYou cooked a delicious meal and feel accomplished!")
    elif choice == '2':
        print("\nYou enjoyed your takeout while watching your favorite show!")
    elif choice == '3':
        print("\nYou had a peaceful walk and enjoyed the evening breeze!")
    else:
        print("Invalid choice. Please try again.")
        evening(name)
    night(name) # This now correctly calls the top-level night function

# The night function is moved out of evening() and is now a top-level function
def night(name):
    print("\n🌙 It's night time. Time to reflect on your day.")
    print("1. Journal about your day 📓")
    print("2. Meditate and relax 🧘‍♂️")
    print("3. Read a book 📖")

    choice = input("What do you want to do? (1/2/3): ")

    if choice == '1':
        print("\nYou wrote in your journal and feel grateful for the day's experiences.")
    elif choice == '2':
        print("\nYou meditated and feel calm and centered.")
    elif choice == '3':
        print("\nYou read a fascinating book and learned something new!")
    else:
        print("Invalid choice. Please try again.")
        night(name)
        return # Stop the function here to avoid calling end_game on invalid input
    end_game(name) # Call the new end_game function

# We define the end_game function to properly handle the end of the game
def end_game(name):
    print(f"\n🌙 Good night, {name}! Thanks for playing your 'Day in the Life' adventure. ✨")

# Run the game
if __name__ == "__main__":
    start_game()
