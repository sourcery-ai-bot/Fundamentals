def FizzBuzz(first="Fizz", second="Buzz"):
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("{}{}".format(first,second))
        elif num % 3 == 0:
            print("{}".format(first))
        elif num % 5 == 0:
            print("{}".format(second))
        else:
            print(num)

FizzBuzz()
FizzBuzz("Cat","Dog")