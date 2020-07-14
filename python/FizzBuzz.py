import sys

def print_FizzBuzz(number):
    print("-----------")
    for x in range(1, number+1):
        if(x%3==0 and x%5==0):
            print("FizzBuzz")
        elif(x%3==0):
            print("Fizz")
        elif(x%5==0):
            print("Buzz")
        else:
            print(x)

try:
    number = int(input("Please enter your number: "))
    print_FizzBuzz(number)
except:
    print("Oops!", sys.exc_info()[0])
