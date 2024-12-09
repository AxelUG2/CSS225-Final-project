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
        
def room3(player):
    print("\n--- Chapter 3: The Sword of Destiny ---")
    print("You enter a dimly lit cavern and see a shimmering sword embedded in a stone.")
    choice = input("Do you try to pull out the sword? (yes/no): ").strip().lower()
    if choice == "yes":
        print("With a mighty effort, you pull out the sword! It glows with a magical light.")
        player.pick_item("Sword")
    else:
        print("You decide to leave the sword behind. You might regret this decision later.")
    player.show_inventory()
