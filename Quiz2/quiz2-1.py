import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

number = a**b

while len(str(number)) > 1:
    total = 0
    for digit in str(number):
        total += int(digit)
    
    number = total

print(number)