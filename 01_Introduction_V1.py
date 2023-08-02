# INTRODUCTION V1

# Def yes_no for the instructions
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please answer yes or no, Thank you!")


# The Instructions
while True:
    instructions = yes_no("Would you like to see the instructions?")

    if instructions == "yes":
        print("----- Instructions Goes here -----")
