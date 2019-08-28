import random

MIN = 1
MAX = 45
NUM_RANDOM_NUMBERS = 6

num_quick_picks = int(input("how many quick picks:"))
for i in range(num_quick_picks):
    numbers = []
    for j in range(NUM_RANDOM_NUMBERS):
        number = random.randint(MIN, MAX)
        while number in numbers:
            number = random.randint(MIN, MAX)
        numbers.append(number)
        numbers.sort()
    print(numbers)

