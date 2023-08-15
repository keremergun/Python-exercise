import sys

#kero

numbers = list()

for number in sys.argv[1:]:
    if int(number) < 0:
        continue
    numbers.append(number)


def luckyNumber(numbers):
    index = 1
    deleting = int(numbers[index])

    while deleting < len(numbers):
        del numbers[deleting-1::deleting]

        if str(deleting) in numbers:
            index += 1
            deleting = int(numbers[index])
        else:
            deleting = int(numbers[index])
    
    return numbers


printing = str()

luckies = luckyNumber(numbers)

index = 0
for lucky in luckies:
    if index == 0:
        printing = lucky
    else:
        printing += " " + lucky

    index += 1

print(printing)