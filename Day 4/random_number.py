import random

random_integer = random.randint(1, 5)
print(random_integer)


random_float = random.random()
print(random_float)

random_n = float(random_integer) + random_float
print(str(random_n))

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")