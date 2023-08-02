def aop(question):
    do_check = ["area", "perimeter"]
    while True:
        response = input(question).lower()

        if response == "area":
            print("You Chose Area")
            return response
        elif response == "perimeter":
            print("You Chose Perimeter")
            return response
        else:
            print("Please enter Area or Perimeter")


area_perimeter = aop("----Please Enter Area or Perimeter----")
