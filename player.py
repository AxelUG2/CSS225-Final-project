class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100  # Initialize health with 100 points

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"You picked up: {item}")

    def show_inventory(self):
        if self.inventory:
            print("Your inventory contains:", ", ".join(self.inventory))
        else:
            print("Your inventory is empty.")

    def use_potion(self):
        if "Potion" in self.inventory:
            self.health += 20
            self.inventory.remove("Potion")
            print(f"You used a potion. Your health is now {self.health}.")
        else:
            print("You don't have any potions!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"You took {damage} damage. Your health is now {self.health}.")
        if self.health <= 0:
            print("You have died. Game over!")
            exit()
