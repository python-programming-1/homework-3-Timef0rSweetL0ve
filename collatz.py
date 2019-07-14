Homework 3

Write a Python program for the Collatz Conjecture.

def collatz(num):
    collatz_list = []
    while True:
        if num % 2 == 0 and num != 1:   # even integer
            num = num // 2
            collatz_list.append(num)    # catch num into the list
        if num % 2 == 1 and num != 1:   # odd integer
            num = 3 * num + 1
            collatz_list.append(num)    # catch num into the list
        if num != 1:                    # for integer different than 1
            continue
        else:
            break
    return collatz_list                 # retain the list value for use in global scope

print('Please type in an integer: ')
try:
    num = int(input())
    if num <= 1:                         # for a input that is less than or equal 1
        print('Integer must be bigger than 1!')
    else:                               # for a positive integer input
        result = collatz(num)
        print('Collatz conjecture from your input: ')
        for val in result:              # retrieve and display values from the list
            print(val)

except ValueError:                      # for a non-integer value input
            print('Oops! Invalid. Input must be an integer.')
