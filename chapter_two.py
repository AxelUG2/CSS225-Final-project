def room2(player):
    """
    Second room of the game. The player chooses between two doors.
    """
    print("\nYou enter a new room with two doors: one on the left and one on the right.")
    choice = input("Do you go through the left door or the right door? (left/right): ").lower()

    if choice == "left":
        print("You step into a glittering room filled with treasure!")
        player.pick_item("Gold Coin")
        print("Congratulations, you found treasure and won the game!")
    elif choice == "right":
        print("You enter a dark room and suddenly fall into a pit. Game over!")
        exit()
    else:
        print("Invalid choice. You stand confused in the room.")
        room2(player)  # Repeat the choice if the input is invalid
