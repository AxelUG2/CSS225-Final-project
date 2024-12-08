def room3(player):
    print("\nYou enter a dimly lit room. There's a glowing potion on a pedestal.")
    choice = input("Do you take the potion? (yes/no): ").lower()

    if choice == "yes":
        player.pick_item("Potion")
        print("You feel a sense of relief knowing you have a health potion.")
    elif choice == "no":
        print("You decided to leave the potion behind.")
    else:
        print("Invalid choice. The potion vanishes before your eyes.")
