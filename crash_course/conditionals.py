# BMI Calculator

print("Hello there! Let's check up on your health, shall we?")
weight = float(input("What is your weight? (kg) "))
height = float(input("What is your height? (metres) "))
Bmi = weight/(height*height)

if(Bmi<18.5):
    print("Ooops!! Someone is underweight!!")
elif (Bmi>=18.5 and Bmi<=24.9):
    print("Looks like you've got some healthy weight !!")
elif(Bmi == 25.0 and Bmi <=29.5):
    print("You might wanna burn some calories ... you're a not overweight!")
else:
    print("Have you considered hitting the GYM? You seem to be obese!")

