def room1(player):
    print("\nYou find yourself in a dark room. There's a key on a table.")
    choice = input("Do you pick up the key? (yes/no): ").lower()

    if choice == "yes":
        player.pick_item("Key")
    elif choice == "no":
        print("You decided to leave the key behind.")
    else:
        print("Invalid choice. You stand still, unsure of what to do.")

    player.show_inventory()

