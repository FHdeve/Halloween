# Import the modules
def halloweenball():
    while(True):
        question = int(input("Enter a number: "))
        if question == 8:
            print("You got it right")
        if question == "":
            break
        elif question == 1:
            print("Keep outta here!")
        elif question == 2:
            print("Skeletons have a lot of calcium")
        elif question == 3:
            print("BOO!!!")
        elif question == 4:
            trickOrTreat = input("Trick or Treat?")
            if trickOrTreat == "trick":
                print("No, it is a treat!")
            elif trickOrTreat == "treat":
                print("You got it right, get outta here!")
        elif question == 5:
            print("Beware of Witches")
        elif question == 6:
            print("Watch out for edibles!")
        elif question == 7:
            print("Take one not all!!")
        elif question == 8:
            print("Don't cross a black cat!!!")
halloweenball()