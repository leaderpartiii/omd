from typing import TypedDict


class Order(TypedDict):
    id: int
    buyer: str
    status: str
    amount: int


orders: list[Order] = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

print(sum([order["amount"]
           for order in orders if order["status"] == "returned"]))
print(*{order["buyer"]
        for order in orders if order["status"] == "returned"})
amounts = [order["amount"]
           for order in orders if order["status"] == "delivered"]
print(len(amounts))
print(sum(amounts) / len(amounts))
