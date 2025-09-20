print("Select your ride:")
print("1. Bike")
print("2. Car")
choice = int(input("Enter your choice 1 or 2:"))
if (choice == 1):
    print("What type of bike?")
    print("1. Scooty\n")
    print("2. Scooter\n")
    choice_2 = int(input("Enter your prefered type of bike:"))
    if(choice_2 == 1):
        print("You have chosen Scooty!")
    else:
        print("You have chosen Scooter!")
elif (choice == 2):
    print("What type of car?")
    print("Sedan")
    print("XUV")
    choice_3 = int(input("Ennter your prefered type of car:"))
    if(choice_3 == 1):
        print("You have chosen Sedan!")
    else:
        print("You have chosen XUV!")
else:
    print("Wrong answer!")