import math
from datetime import date

import pandas


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
    to_check = ["square", "circle", "rectangle", "triangle", "xxx", "s", "r", "c", "t"]

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
            elif response == "no":
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
    print("Input your desired Shape and the Dimensions\n"
          "The program will calculate the area and perimeter\n"
          "Type 'xxx' to end the program\n")

# Error message
error = "Please Try Again"

# Dictionary - - - - - - - - - - - - -
shapes = []
area_panda = []
perimeter_panda = []

calculator_dict = {
    "Shape:": shapes,
    "Area:": area_panda,
    "Perimeter:": perimeter_panda
}

# THIS FUNCTION DOES ALL THE CALCULATIONS
# IT HAS 2 SECTIONS DECIDED BY AREA OR PERIMETER
# THE FUNCTION ASK FOR THE LENGTHS TO FIND THE AREA / PERIMETER
while True:
    # Ask what shape the user desires
    shape_c1 = Shape_check("\nPlease Pick a Valid Shape... (Square, Triangle, Rectangle or Circle)\n"
                           "Else type 'xxx' to quit.\n").lower()

    # Gets Dimensions for the Square
    if shape_c1 == "square" or "s":
        side_length = num_check("Side Length: ")
        perimeter = side_length * 4
        area = side_length ** 2

        # Gets Dimensions for the Triangle
        # figure out how to ask the user if they want area and perimeter
    elif shape_c1 == "triangle" or "t":
        base = num_check("Side 1 Length: ")
        side = num_check("Side 2 Length: ")
        other_side = num_check("Other Side Length:")
        perimeter = base + side + other_side
        hp = perimeter / 2
        herons_law = math.sqrt(hp * (hp - base) * (hp - side) * (hp - other_side))
        area = herons_law

    # Gets Dimensions for the Circle
    elif shape_c1 == "circle" or "c":
        radius = num_check("Radius: ")
        # add pi
        perimeter = math.pi * math.sqrt(radius)
        area = 2 * math.pi * radius

    # Gets Dimensions for the Rectangle
    elif shape_c1 == "rectangle" or "r":
        base = num_check("Base Length: ")
        length = num_check("Height Length: ")
        perimeter = base * 2 + length * 2
        area = base * length

    elif shape_c1 == "xxx":
        break
    else:
        print(error)

    # Pandas ----
    shapes.append(shape_c1)
    area_panda.append(area)
    perimeter_panda.append(perimeter)
# Add Panda's and then you're done

calculator_frame = pandas.DataFrame(calculator_dict)

print(calculator_frame)
