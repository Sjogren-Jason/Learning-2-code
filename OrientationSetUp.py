class Person:
        def __init__(self, name):
            self.name = name

        def greet(self):
            print(f"Hello,{self.name}, I'd like to setup an orientation with you. Please give me a call.")


names = ["Jason", "Nathan"]
new_hire = Person(names[1])
new_hire.greet()

