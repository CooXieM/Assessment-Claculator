import pandas as pd
import math
from datetime import date


# Functions -----
# Introduction -
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = '{} {} {}'.format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


# Def yes_no for the instructions
# Checkers user has answered yes / no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either Yes or No: \n")


# Def Shape Checker and put a list
def Shape_check(question):
    to_check = ["square", "circle", "rectangle", "triangle"]

    while True:
        response = input(question).lower()

        for shape_chosen in to_check:
            if response == shape_chosen:
                return response


# Ask the user if they want to find the area or perimeter
def aop(question):
    while True:
        response = input(question).lower()

        if response == "area":
            print("You Chose Area\n")
            return response
        elif response == "perimeter":
            print("You Chose Perimeter\n")
            return response
        elif response == "xxx":
            return response
        else:
            print("Please enter Area or Perimeter")


def num_check(question):
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print("Please enter a number bigger than 0")

        except ValueError:
            print("Please enter an integer")


# Date time at the start -
today = date.today()

day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")
heading = "{}/{}/{}".format(day, month, year)
print(heading)

# Statement generator
statement_generator("Shape Area / Perimeter Calculator", "=")

# Ask if instructions are needed -
want_instructions = yes_no("\n Would you like to see the Instructions to this program?")
if want_instructions == 'yes':
    print("Instructions goes here")
print()

# Ask if instructions are needed -
shape_c1 = Shape_check("Please Pick a Valid Shape... (Square, Triangle, Rectangle or Circle)\n")

# Ask user if they want area or perimeter
area_perimeter = aop("----Please Enter Area or Perimeter----")

# Error message
error = "Please Try Again"

# THIS FUNCTION DOES ALL THE CALCULATIONS
# IT HAS 2 SECTIONS DECIDED BY AREA OR PERIMETER
# THE FUNCTION ASK FOR THE LENGTHS TO FIND THE AREA / PERIMETER
while True:
    if area_perimeter == "xxx":
        break
    else:
        if area_perimeter == "area":
            # Gets Dimensions for the Square
            if shape_c1 == "square":
                side_length = num_check("Side Length: ")
                area = side_length ** 2
                print("Your area is: {}".format(area))

                # Gets Dimensions for the Triangle
            elif shape_c1 == "triangle":
                base = num_check("Base Length: ")
                height = num_check("Height Length: ")
                area = 0.5 * base * height
                print("Your triangle area is: {}".format(area))

            # Gets Dimensions for the Circle
            elif shape_c1 == "circle":
                radius = num_check("Radius: ")
                # add pi
                area = 2 * math.pi * radius
                print("Your Circle area is: {}".format(area))

            # Gets Dimensions for the Rectangle
            elif shape_c1 == "rectangle":
                base = num_check("Base Length: ")
                length = num_check("Height Length: ")
                area = base * length
                print("Your Rectangle Area is: {}".format(area))

            # THIS AREA IS THE PERIMETER CALCULATOR
            elif area_perimeter == "perimeter":
                pass
                # Gets dimensions for the Square
                if shape_c1 == "square":
                    p1 = num_check("Base Length: ")
                    perimeter = p1 * 4
                    print("Your Perimeter is: {:.2f}".format(perimeter))
                # Gets dimensions for the Triangle
                elif shape_c1 == "triangle":
                    l1 = num_check("First Length: ")
                    l2 = num_check("Second Length:")
                    l3 = num_check("Third Length: ")
                    perimeter = l1 + l2 + l3
                    print("Your Perimeter is: {:.2f}".format(perimeter))

                # Gets dimensions for the Circle
                elif shape_c1 == "circle":
                    r1 = num_check("Radius Length: ")
                    perimeter = 2 * math.pi * r1
                    print("Your Perimeter is: {:.2f}".format(perimeter))

                # Gets dimensions for the Rectangle
                elif shape_c1 == "rectangle":
                    re1 = num_check("Height Length: ")
                    re2 = num_check("Base Length: ")
                    perimeter = re1 * 2 + re2 * 2
                    print("Your Perimeter is: {:.2f}".format(perimeter))

                else:
                    print("Please enter a Number")
# Add Panda's and then you're done

my_dict = {
    "Shape": shape_c1,
    "A / P": area_perimeter,
    "Perimeter": perimeter,
    "Area": area,
}

variable_frame = pd.DataFrame(columns=[my_dict])
