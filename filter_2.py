people = [
    {"sex": "m", "age": 12},
    {"sex": "w", "age": 12},
    {"sex": "m", "age": 15},
    {"sex": "m", "age": 20},
    {"sex": "m", "age": 13},
    {"sex": "m", "age": 27},
    {"sex": "w", "age": 31},
    {"sex": "m", "age": 17},
    {"sex": "w", "age": 17},
    {"sex": "m", "age": 12},
    {"sex": "m", "age": 42},
    {"sex": "w", "age": 25}
]

def p(j):
    return j["sex"] == "m" and 20 <= j["age"] <= 30


my_people = list(filter(p, people))
print(my_people)
