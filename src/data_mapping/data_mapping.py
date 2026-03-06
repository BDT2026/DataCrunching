import json
from typing import List


class Item:

    def __init__(self, id: int, name: str, price: float, quantity: int):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

        if not isinstance(id, int):
            raise TypeError("id must be an integer")
        if not isinstance(name, str):
            raise TypeError("name must be an string")

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.price == other.price and self.quantity == other.quantity



def compute_total(items: List[Item]):
    total = 0
    for item in items:
        total += item.price
    return total

with open("data.json", "r") as f:
    raw_data = f.read()
    print(f"raw_data: {type(raw_data)}")
    data = json.loads(raw_data)
    print(type(data))
    print(data)

    item = Item(
        id=data["id"],
        name=data["name"],
        price=data["price"],
        quantity=data["quantity"]
    )

    print(item)