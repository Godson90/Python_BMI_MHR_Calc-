#! /usr/bin/env python3

# Adesola A
# April 11 2020
# BMI/MHR Calculator
# This program calculates and output the BMI of an individaul,exerscise intensive heart rate,and MHR


print("Please enter the following values.")
validInput = 0

while validInput>=0:
    try:
        height = int(input("Height in inches :"))
    except ValueError:
        print("Sorry, please you need to enter a whole number.")
        continue
    else:
        break
    
while validInput>=0:
    try:
        weight = int(input("Weight in pounds :"))
    except ValueError:
        print("Sorry, please you need to enter a whole number.")
        continue
    else:
        break
    
while validInput>=0:
    try:
        age = int(input("Current age :"))
    except ValueError:
        print("Sorry, please you need to enter a whole number.")
        continue
    else:
        break
    
while validInput>=0:
    try:
        restingRate = int(input("Resting heart rate :"))
    except ValueError:
        print("Sorry, please you need to enter a whole number.")
        continue
    else:
        break

    

# Body Mass Index Calculation 

def calcBmi(): 
    
    print("Results . . . ")
    bmi = float(round(((weight/2.2046 ) / (height * 0.0254)**2), 2))
    if bmi <= 18.5:
        print("Your BMI is :", bmi , "--", "Underweight")
    elif bmi <= 24.9:
        print("Your BMI is :", bmi , "--", "Normal weight")
    elif bmi <= 29.9:
        print("Your BMI is :", bmi , "--", "Overweight")
    else:
        print("Your BMI is :", bmi , "--", "Obesity")
    return bmi

print("   ")

bmi = calcBmi()

print("   ")

# Calculates Max heart rate(MHR)

def calcHeartRate():  
     print("Exersicse Intensity Heart Rate: ")
     print("Intensity \tMax Heart Rate")
     print("  ")
     for i in range(50,96,5):  # i equals the exersicse intensity in percentage
         i=i/100
         maxHeartRate = (((220 -age) - restingRate) * i) + restingRate
         print ("{0: .2f}           {1}" .format(i,int(maxHeartRate)))
    

calcHeartRate()

print(input('\n\nHit Enter to Close\n'))



    
            
            
    
    

  

        
