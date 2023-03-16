

with open('numbers.txt', 'r') as numbers:
    numbers = numbers.readlines()


for number in numbers:
    print("Nope")
    if "7" in number:
        print(number.rstrip())
