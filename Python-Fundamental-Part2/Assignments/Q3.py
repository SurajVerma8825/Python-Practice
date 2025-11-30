

def digits(a):
  rev = 0
  while(a > 0):
       rem = a % 10
       rev = rev * 10 + rem
       a = a//10

  while(rev > 0):
       rem = rev % 10
       print(rem)
       rev = rev//10

num = int(input("Enter your number: "))

digits(num)
