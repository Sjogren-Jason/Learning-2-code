secret_number = 4
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Correct!")
        break
    else:
        if guess_count == guess_limit:
            print("Guess limit has been reached. Thanks for playing.")
        else:
            print("Incorrect, please try again.")

