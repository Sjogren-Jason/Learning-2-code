class Person:
        def __init__(self, name):
            self.name = name

        def greet(self):
            print(f"Hello, {self.name}, I'd like to setup an orientation with you on {orientation_start_day}. Does {orientation_start_time} work for you?")


names = []
maxLengthList = 3
loop = True
loop1 = True

while loop is True:
    while len(names) < maxLengthList:
        hires = input("Enter name of new hires: ")
        names.append(hires)
    correct = input("Is this correct?").lower()
    if correct == "yes":
        print("Awesome!")
        loop = False
    else:
        loop = True
        names = []

print(f"{names[0]}, {names[1]}, and {names[2]}")
orientation_setup = input("Would you like to setup orientation? ").lower()
if orientation_setup == "yes":
    while loop1 is True:
        orientation_start_day = input("What day? ")
        orientation_start_time = input("What time? ")
        print(f"{orientation_start_day} at {orientation_start_time}")
        send = input("Is this correct?").lower()
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
        else:
            loop1 = True

else:
    print("That's too bad. Goodbye.")