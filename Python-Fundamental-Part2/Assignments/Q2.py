def odd_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)
    

num1 = int(input("Enter the number to start: "))
num2 = int(input("Enter the number to end: "))

print("Even Number is = ")
odd_even(num1, num2)
