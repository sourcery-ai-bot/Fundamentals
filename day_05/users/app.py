
my_file = open('lol')

for line in my_file:
    print(line)

my_file = open('lol', 'w')
my_file.write("Here is a new line!")
