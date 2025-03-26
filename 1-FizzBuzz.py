
'''
Write a function that prints numbers from 1 to 50.

    If a number is divisible by 3, print "Fizz"

    If divisible by 5, print "Buzz"

    If divisible by both, print "FizzBuzz"
'''



def checkFizzBuzz():
    num = int(input('Enter a number: '))

    for num in range(1,51):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')

        elif num % 3 == 0:
            print('Fizz')

        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)


checkFizzBuzz()