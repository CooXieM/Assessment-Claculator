import math


# Def Shape Checker and put a list
def Shape_check(question):
    to_check = ["square", "circle", "rectangle", "triangle"]

    while True:
        response = input(question).lower()

        for shape_chosen in to_check:
            if response == shape_chosen:
                return response


# Ask if instructions are needed -
shape_c1 = Shape_check("\n Please Pick a Valid Shape... (Square, Triangle, Rectangle or Circle)")

if shape_c1 == "square":
    print("Please enter your side lengths")
    side_length = float(input())
    area = side_length ** 2
    print("Your square's area is:", area)

elif shape_c1 == "triangle":
    print("Please enter base")
    base = float(input())
    print("Please enter height")
    height = float(input())
    area = 0.5 * base * height
    print("Your triangle area is:", area)

elif shape_c1 == "circle":
    print("Please enter The radius")
    radius = float(input())
    # add pi
    area = 2 * math.pi * radius
    print("Your Circle area is: ", area)

elif shape_c1 == "rectangle":
    print("Please enter your base")
    base = float(input())
    print("Please enter the length")
    length = float(input())
    area = base * length
    print("your rectangle area is:", area)
else:
    print("Please Try Again")


