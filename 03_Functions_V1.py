# Shape Checker

def shape_checker(question):
    while True:
        response = input(question).lower()

        if response == 'Circle':
            return 'Circle'
        elif response == 'Square':
            return 'Square'
        elif response == 'Rectangle':
            return 'Rectangle'
        elif response == 'Triangle':
            return 'Triangle'
        else:
            print("You need to chose a VALID Shape")


shape_question = shape_checker("What Shape do you Require?")
print("The shape you have chosen was: {}".format(shape_question))

if shape_question == "Circle":
    print("You chose Circle")
elif shape_question == "Square":
    print("You chose Square")
elif shape_question == "Rectangle":
    print("You chose Rectangle")
elif shape_question == "Triangle":
    print("You chose Triangle")
else:
    print("Unknown Shape!!!")
