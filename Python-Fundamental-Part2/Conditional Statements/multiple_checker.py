num = int(input("Please enter the value of number: "))
divider = int(input("Please enter the value of divider: "))

if(num % divider == 0):
    print("Yes,", num, "is a multiple of", divider)
else:
    print("No,", num, "is not a multiple of", divider)
