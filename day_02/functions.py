
def count_to_ten():
    for count in range(1, 11):
        print(count)

# print("call my function 1 time")
# count_to_ten()

# print("call my function another time")
# count_to_ten()

def count_to(number):
    for count in range(1, number + 1):
        print(count)

# count_to(6)

def count(number=10):
    for count in range(1, number + 1):
        print(count)

print("call count without an argument")
count()

print("call count with an arugment of 2")
count(2)