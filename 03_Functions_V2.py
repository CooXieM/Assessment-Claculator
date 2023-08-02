# Def Shape Checker and put a list
def Shape_check(question):
    to_check = ["square", "circle", "rectangle", "triangle"]

    Valid = False
    while not Valid:
        response = input(question).lower()

        for shape_chosen in to_check:
            if response == shape_chosen:
                return response
            elif response == shape_chosen[0]:
                return shape_chosen
        print("Please Enter a Valid Shape")


# Ask if instructions are needed -
shape_c1 = Shape_check("\n Please Pick a Valid Shape... (Square, Triangle, Rectangle or Circle)")
print("Chosen {}".format(shape_c1))


