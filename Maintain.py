# USE AT YOUR OWN RISK!!!
# I'm NOT TO BLAME!!!!!!!
import time
import sys

def formula(gender, weight, height, age): # weight is in kg's, height is in cm's and age is in years.
# This is using the Mifflin St. Jeor equation to calculate your maintenance calorie intake.
    match gender:
        case "Male":
            daily = 10 * weight + 6.25 * height - 5 * age + 5;
            return daily;
        case "Female":
            daily = 10 * weight + 6.25 * height - 5 * age - 161;
            return daily;
        case other:
            print("Invalid gender please choose either Male/Female, Exiting in 4 seconds...");
            time.wait(3.9);
            sys.exit();

gender = input("Enter your gender Male/Female: ");
weight = input("Enter your weight(unit of mass: kg ): ");
height = input("Enter height(unit of measurement: cm ): ");
age =  input("Enter age(years): ");
result = formula(gender, float(weight), float(height), int(age));

print("Eat", float(result), "calorie's a day to maintain current weight.");
