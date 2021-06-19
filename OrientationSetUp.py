class Person:
        def __init__(self, name):
            self.name = name

        def greet(self):
            print(f"Hello, {self.name}, I'd like to setup an orientation with you on {orientation_start_day}. Does {orientation_start_time} work for you?")


names = []
maxLengthList = 3
loop = True
loop1 = True
quit_loop = False
while quit_loop is False:
    while loop is True:
        while len(names) < maxLengthList:
            hires = input("Enter name of new hires: ")
            names.append(hires)
        correct = input("Is this correct? ").lower()
        if correct == "yes":
            print("Awesome!")
            print(f"You will be hiring {names[0]}, {names[1]}, and {names[2]}!")
            loop = False
        else:
            loop = True
            names = []

    orientation_setup = input("Would you like to setup orientation? ").lower()

    if orientation_setup == "yes":

        while loop1 is True:

            orientation_start_day = input("What day? ")
            orientation_start_time = input("What time? ")
            print(f"{orientation_start_day} at {orientation_start_time}")
            send = input("Is this correct and would like to send? ").lower()

            if send == "yes":
                print("Sending ...")
                new_hire1 = Person(names[0])
                new_hire2 = Person(names[1])
                new_hire3 = Person(names[2])
                new_hire1.greet()
                new_hire2.greet()
                new_hire3.greet()
                print("Sent!")
                loop1 = False
            elif send == "no":
                print("Let's try again...")
                quit_loop = True
                loop1 = True
            else:
                print("""
Sorry I don't understand.
Please give a Yes or NO
Restarting...
                """)
                loop1 = True

        loop2 = True
        while loop2 is True:
            continue_loop = input("Would you like to send more? ").lower()
            if continue_loop == "yes":
                print("Restarting process...")
                quit_loop = False
                loop = True
                loop1 = True
                loop2 = False
                names = []
            elif continue_loop == "no":
                print("Goodbye for now...")
                quit_loop = True
                loop2 = False
            else:
                print("Sorry I don't understand, please give a Yes or No.")
    elif orientation_setup == "no":
        print("Why open this app then?")
        quit_loop = True
    else:
        print("Sorry I don't understand, please give a Yes or No.")
