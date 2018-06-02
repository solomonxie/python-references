"""
OOD: Vending Machine.
State machine (Idle -> HasMoney -> Dispensing) driving inventory and change.
"""
from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def insert_coin(self, machine, amount):
        ...

    @abstractmethod
    def select(self, machine, code):
        ...


class IdleState(State):
    def insert_coin(self, machine, amount):
        machine.balance += amount
        machine.state = HasMoneyState()

    def select(self, machine, code):
        print("Insert coins first")


class HasMoneyState(State):
    def insert_coin(self, machine, amount):
        machine.balance += amount

    def select(self, machine, code):
        item = machine.inventory.get(code)
        if not item:
            print("Invalid selection")
            return
        if item["stock"] <= 0:
            print(f"{item['name']} is sold out")
            return
        if machine.balance < item["price"]:
            print(f"Insufficient funds for {item['name']}")
            return
        change = machine.balance - item["price"]
        item["stock"] -= 1
        machine.balance = 0
        machine.state = IdleState()
        print(f"Dispensing {item['name']}, change: {change}")


class VendingMachine:
    def __init__(self):
        self.state = IdleState()
        self.balance = 0
        self.inventory = {
            "A1": {"name": "Soda", "price": 150, "stock": 2},
            "A2": {"name": "Chips", "price": 200, "stock": 0},
        }

    def insert_coin(self, amount):
        self.state.insert_coin(self, amount)

    def select(self, code):
        self.state.select(self, code)


if __name__ == "__main__":
    machine = VendingMachine()
    machine.select("A1")
    machine.insert_coin(100)
    machine.insert_coin(100)
    machine.select("A1")
    machine.insert_coin(200)
    machine.select("A2")
