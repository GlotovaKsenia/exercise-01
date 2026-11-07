from collections import deque
from typing import TypedDict
from itertools import combinations
class Item(TypedDict):
    name: str
    weight: int
    value: int

MAP: dict[str, list[str]] = {
    "Eingang": ["Archiv","Lab"],
    "Archiv":["Eingang","Bib"],
    "Lab":["Eingang","Bib","Serverraum"],
    "Bib":["Archiv","Lab","Ausgang"],
    "Serverraum":["Lab"],
    "Ausgang":["Bib"],
}

LOOT: list[Item] = [
    {"name": "daten", "weight": 1, "value": 6},
    {"name": "alg", "weight": 5, "value": 20},
    {"name": "gold", "weight": 5, "value": 19},
    {"name": "key", "weight": 2, "value": 4},
    {"name": "lat", "weight": 4, "value": 4},
]
def shortest_path(graph: dict[str, list[str]], start: str, goal: str) -> list[str] | None:
    if start==goal:
        return [start]

    queue = deque([start])
    woher_kam_ich = {start: None}
    while queue:
        aktueller_raum = queue.popleft()
        if aktueller_raum == goal:
            pfad = []
            while aktueller_raum is not None:
                pfad.append(aktueller_raum)
                aktueller_raum = woher_kam_ich[aktueller_raum]
            return pfad[::-1]
        for nachbar in graph[aktueller_raum]:
            if nachbar not in woher_kam_ich:
                woher_kam_ich[nachbar] = aktueller_raum
                queue.append(nachbar)
    return None

print(shortest_path(MAP, "Eingang", "Ausgang"))

def greedy_snack(items: list[Item], cap: int = 20) -> tuple[list[Item], int, int]:
    ratio = sorted(items, key=lambda item: item["value"] / item["weight"], reverse=True)
    chosen: list[Item] = []
    total_w = 0
    total_v = 0
    for item in ratio:
        if total_w + item["weight"] <= cap:
            chosen.append(item)
            total_w += item["weight"]
            total_v += item["value"]
    return chosen, total_w, total_v

gepackte_items, gewicht, wert = greedy_snack(LOOT, 20)

print("--- RUCKSACK INHALT ---")
for item in gepackte_items:
    print(f"• {item['name']} (Gewicht: {item['weight']}, Wert: {item['value']})")

print("-----------------------")
print(f"Gesamtgewicht: {gewicht} / 20")
print(f"Gesamtwert:    {wert}")