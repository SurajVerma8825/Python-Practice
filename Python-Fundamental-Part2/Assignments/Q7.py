while True:
    words = input("Enter a word -> ")

    match words:
        case "Quit":
            break

        case _:
            num = int(input("Enter a number: "))
            if num > 0:
                print("Positive")
            else:
                print("Negative")
