# Shape Checker

def shape_checker(question):
    while True:
        response = input(question).lower()

        if response == 'Circle':
            response = 'you chose Circle'
            return response
        elif response == 'Square':
            response = 'you chose Square'
            return response
        elif response == 'Rectangle':
            response = "you chose Rectangle"
            return response
        elif response == 'Triangle':
            response = "you chose Triangle"
            return response
        else:
            print("You need to chose a Shape")


shape_question = shape_checker("What shape do you need?")
print("you chose {} as your shape")
