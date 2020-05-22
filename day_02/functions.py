
def count_to_ten():
    count = 1
    while count <= 10:
        print(count)
        count += 1

# print("call my function 1 time")
# count_to_ten()

# print("call my function another time")
# count_to_ten()

def count_to(number):
    count = 1
    while count <= number:
        print(count)
        count += 1

# count_to(6)

def count(number=10):
    count = 1
    while count <= number:
        print(count)
        count += 1

print("call count without an argument")
count()

print("call count with an arugment of 2")
count(2)