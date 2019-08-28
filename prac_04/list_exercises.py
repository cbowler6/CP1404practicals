# numbers = []
# for i in range(5):
#     data = int(input("enter  number: "))
#     numbers.append(data)
# average = sum(numbers)/len(numbers)
#
# print("the first number is {}".format(numbers[0]))
# print("the last number is {}".format(numbers[-1]))
# print("the smallest number is {}".format(min(numbers)))
# print("the largest number is {}".format(max(numbers)))
# print("the average of the numbers is {}".format(average))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("enter your username: ")
if username in usdaernames:
    print("access granted")
else:
    print("access denied")