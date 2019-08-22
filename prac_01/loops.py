# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()
#

# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()

# todo: won't work
# for i in range(0, 21, -1):
#     print(i, end=' ')
# print()

# number_of_stars = int(input("how many stars?"))
# for i in range(number_of_stars):
#     print("*", end=" ")

number_of_stars = int(input("how many stars?"))
for i in range(number_of_stars):
    print((i+1) * "*", end="\n")
