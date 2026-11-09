import csv
from typing import Any
from pathlib import Path

CSV_PATH = Path(__file__).parent / "loot.csv"
class Item:
    def __init__(self, name, weight, value):
        self.n = name
        self.w = weight
        self.v = value
    def __repr__(self):
        return f"Item({self.n}, W:{self.w}, V:{self.v})"

def load_items(path: Path = CSV_PATH )-> list[Item]:
    with open(path, encoding="utf-8", newline="") as file:
        items: list[Item] = []
        for row in csv.DictReader(file):
            item = Item(
                name=row["name"],
                weight=float(row["weight"]),
                value=float(row["value"])
            )
            items.append(item)
        return items

class Room:
    def __init__(self, name, neigh: list["Room"] = None, items: list[Item] = None):
        self.name = name
        self.neigh = neigh
        self.items = items if items is not None else []

class Player:
    def __init__(self, name, current_room: Room, capacity: int=10):
        self.n = name
        self.cr = current_room
        self.c = capacity
        self.inventory: list[Item] = []
    def inventory_w(self):
        return sum(item.w for item in self.inventory)
    def inventory_v(self):
        return sum(item.v for item in self.inventory)

    def move(self, target_room: Room)-> bool:
        if target_room in self.cr.neigh:
            self.cr = target_room
            print(f"{self.n} hat sich in den Raum '{target_room.name}' bewegt.")
            return True
        print("Dorthin kommst du von hier aus nicht!")
        return False

    def pick_up(self, item:Item):
        if self.inventory_w() + item.w > self.c:
            raise ValueError(f"für {item.n} kein Platz")
        self.inventory.append(item)
        self.cr.items.remove(item)

def average(items: list[Item]):
    if not items:
        raise ValueError("Keine Beute")
    return round(sum(item.v for item in items) / len(items), 2)

def valuable(items: list[Item]):
    return max(items, key=lambda item: item.v)

if __name__=="__main__":
    loot = load_items()
    print("average value:", average(loot))
    print("most valuable item:", valuable(loot))

    entrance = Room("Eingang")
    archive = Room("Archiv")
    library = Room("Bib")
    lab = Room("Lab")
    extry = Room("Ausgang")
    entrance.neigh = [archive,lab]
    archive.neigh = [entrance, library]
    library.neigh = [archive,lab,extry]
    library.items = loot
    
    player = Player("Yuki", entrance)
    player.move(archive)
    player.move(library)

    for item in list(library.items):
        try:
            player.pick_up(item)
        except ValueError as error:
            print("not possible", error)

    print(player)
    print("backpack:", player.inventory_v())
