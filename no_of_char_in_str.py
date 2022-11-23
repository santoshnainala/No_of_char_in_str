#No.of chars in string
count = 0

my_string = str(input("enter string : "))
my_char = str(input("enter char : "))

for i in my_string:
    if i == my_char:
        count += 1

print(count)
