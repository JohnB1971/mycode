#!/usr/bin/env python3

# Student Letter Grade Calculations


message = "The letter grade for that numeric score is "

# wrap connection in a float() to accept decimals as numbers
grade = float(input("What is your numeric grade?"))

# if input value was higher or equal to 90
if grade >= 90:
    message = message + "A (90 to 100)."
# if input value was higher or equal to 80
elif grade >= 80:
    message = message + "B (80 to 89)."
# if input value was higher or equal to 70
elif grade >= 70:
    message = message + "C (70 to 79)."
# if input value was higher or equal to 60
elif grade >= 60:
    message = message + "D (60 to 69)."
else:
    message = message + "F (0 to 59) you must retake the class."

print(message)

