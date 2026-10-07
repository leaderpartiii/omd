from statistics import mean
from collections import defaultdict
from typing import TypedDict


class Review(TypedDict):
    id: int
    product: str
    stars: int


reviews: list[Review] = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]
for review in reviews:
    review["product"] = review["product"].capitalize()

group = defaultdict(list)
for review in reviews:
    group[review["id"]].append(review)

stats = [(review_id[0]["product"],
          mean([review["stars"] for review in review_id]),
          len(review_id))
         for review_id in group.values()]
print(*[(name, avg) for (name, avg, count) in stats])

print(min(
    ((name, avg) for (name, avg, count) in stats if count >= 2),
    key=lambda pair: pair[1]))

low_stars = sum(1 for review in reviews if review["stars"] in (1, 2))
print(low_stars)

print(low_stars / len(reviews))
