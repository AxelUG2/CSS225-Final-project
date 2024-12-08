def room5(player):
    print("\nYou enter a massive cavern. A dragon awakens and roars!")
    print("The dragon breathes fire toward you.")
    choice = input("Do you fight or run? (fight/run): ").lower()

    if choice == "fight":
        if "Sword" in player.inventory:
            print("You wield your sword and charge at the dragon.")
            print("After a fierce battle, you slay the dragon. You are victorious!")
        else:
            print("You have no weapon to fight with. The dragon defeats you.")
            player.take_damage(100)
    elif choice == "run":
        print("You try to run, but the dragon's fire engulfs you.")
        player.take_damage(100)
    else:
        print("You freeze in fear. The dragon attacks!")
        player.take_damage(100)
