#BML calc
weight = 55
height = 1.50
bmi = weight/height**2
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
elif bmi >= 30 and bmi <= 34.9:
    print("Obese")
elif bmi >= 35 and bmi <= 39.9:
    print("Severely Obese")
else:
    print("Morbidly Obese")
