def room4(player):
    print("\nYou find yourself in a maze filled with traps.")
    choice = input("Do you go left, right, or straight? (left/right/straight): ").lower()

    if choice == "left":
        print("A spike trap springs up! You barely escape but take some damage.")
        player.take_damage(20)
    elif choice == "right":
        print("You find a clear path through the maze.")
    elif choice == "straight":
        print("A pit opens beneath you! You fall and take heavy damage.")
        player.take_damage(40)
    else:
        print("You hesitate and a trap activates. You take damage.")
        player.take_damage(10)
