secret = 50

guess = int(input("Guess the number: "))

if guess > secret:
    print("Too high")
elif guess < secret:
    print("Too low")
else:
    print("Correct!")
