def count_digit(num):
    count = 0
    while(num > 0):
       num % 10
       count += 1
       num = num//10
    print("Total digits =", count)


num = int(input("Enter your number: "))

count_digit(num)
