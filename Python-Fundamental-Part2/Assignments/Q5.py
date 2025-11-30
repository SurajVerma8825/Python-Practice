def count_digit(num):
    sum = 0
    while(num > 0):
       rem= num % 10
       sum += rem
       num = num//10
    print("Total sum =", sum)


num = int(input("Enter your number: "))

count_digit(num)
