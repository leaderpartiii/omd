from collections import Counter

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

print(len(queries))
counter = Counter(queries)
print(*list(counter.items()))
print(counter.most_common(1)[0][0])
print(counter.most_common(1)[0][1] / len(queries))
print(*[item for item, count in counter.items() if count == 1])
