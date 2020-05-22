# students = ['Emily', 'Jason', 'Jackson', 'Allan', 'Alex', 'Brandon']

# for item in students:
#     print(item)

# index = 0
# while index < len(students):
#     print(students[index])
#     index += 1

# student[0]
# len(students) # 6

# last_student = students[len(students)-1]

# my_range = range(10, 20)

# for item in my_range:
#     print(item)

# # Print integers from 1 to 100:

# for number in range(1, 101):
#     print(number)


# Write code that prints out the integers from 1 to 100,
# however if the number is divisible by 3, instead of the
# number, print "Fizz" - if it is divisible by 5, instead
# of the number print "Buzz" - if it is divisible by both
# 3 and 5, print "FizzBuzz"

# count = 1
# while count <= 100:
    #  - if count is divisuble by 3?
    #    print "Fizz"
    #  - is it divisible by 5?
    #    print "Buzz"
    #  - is it divisible by 3 & 5?
    #    print "FizzBuzz"
    #  - if none of that, just print count

# for num in range(1, 101):
    #  - if count is divisuble by 3?
    #    print "Fizz"
    #  - is it divisible by 5?
    #    print "Buzz"
    #  - is it divisible by 3 & 5?
    #    print "FizzBuzz"
    #  - if none of that, just print count


for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)