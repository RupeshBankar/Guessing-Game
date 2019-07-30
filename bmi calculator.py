name = input("What is your name?")
height_m = float(input("What's your height? (in metres!!!) "))
weight_kg = float(input("What's your weight? (in kilograms!!!) "))

bmi = weight_kg / (height_m ** 2)
print('bmi:')
print(bmi)


if bmi < 18.5:
    print(name + " is under weight")

elif bmi > 18.5 and bmi < 24.9:
    print(name + ' is healthy')

elif bmi > 25 and bmi < 30:
    print(name + " is overweight")

else:
    print(name + " is obese")