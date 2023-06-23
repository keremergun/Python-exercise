import sys

two_point = int(sys.argv[1])
three_point = int(sys.argv[2])
single_point = int(sys.argv[3])

total_point = two_point*2 + three_point*3 + single_point

print(total_point)

def healthStatus(heigth, mass):
    bmi = float(mass) / float(heigth)**2
    
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 24.9:
        return "Healthy"
    elif bmi >=24.9 and bmi <30:
        return "Overweight"
    else:
        return "Obese"
    
