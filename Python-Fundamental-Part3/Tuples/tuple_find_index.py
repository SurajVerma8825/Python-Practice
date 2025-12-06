tuple = (1 , 4 , 4 , 7 , 7 , 4 , 8 , 9 , 12)

key = int(input("Enter the value: "))



if key in tuple:
    print("Index =", tuple.index(key))
else:
    print("Value not found in tuple")
