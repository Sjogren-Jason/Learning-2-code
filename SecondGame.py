command = ""
ignition = 0
while True:
    command = input("> ").lower()
    if command == "start":
        if ignition == 0:
            print("Car has started...")
            ignition = 1
        else:
            print("Car is already started...")
    elif command == "stop":
        if ignition == 1:
            print("Car has Stopped...")
            ignition = 0
        else:
            print("Car is already stopped")
    elif command == "help":
        print("""
Start - Start car
Stop - Stop car
Quit - Quit Game
        """)
    elif command == "quit":
        print("Goodbye")
        break
    else:
        print("Sorry I didn't understand that.")
