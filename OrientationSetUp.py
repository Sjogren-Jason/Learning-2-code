class Person:
        def __init__(self, name):
            self.name = name

        def greet(self):
            print(f"Hello, {self.name}, I'd like to setup an orientation with you on {orientation_start_day}. Does {orientation_start_time} work for you?")


names = []
maxLengthList = 3
loop = True
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
    orientation_start_day = input("What day? ")
    orientation_start_time = input("What time? ")

    new_hire1 = Person(names[0])
    new_hire1.greet()

    new_hire2 = Person(names[1])
    new_hire2.greet()

    new_hire3 = Person(names[2])
    new_hire3.greet()
else:
    print("That's too bad. Goodbye.")