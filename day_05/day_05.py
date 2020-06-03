def get_number(message="Give me a number: ", error_message="Please input an actual number!"):
    while True:
        try:    
            num = int(input(message))
            return num
        except ValueError:
            print(error_message)

num_1 = get_number()
num_2 = get_number("Give me another number: ")
num_3 = get_number("Give me one last number: ")

result = (num_1 + num_2) * num_3
print("({} + {}) * {} is equal to {}".format(num_1, num_2, num_3, result))