from chapter_one import room1
from chapter_two import room2
from chapter_three import room3
from chapter_four import room4
from chapter_five import room5
from player import Player


def introduction():
    print("Welcome to the Adventure Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)
    print(f"Hello, {player.name}! Your adventure begins now.")
    return player

def main():
    player = introduction()
    room1(player)
    room2(player)
    room3(player)
    room4(player)
    room5(player)

if __name__ == "__main__":
    main()
