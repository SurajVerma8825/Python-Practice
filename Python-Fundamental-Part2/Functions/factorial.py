def fact(a):
    ans = 1
    for i in range(1, a + 1):
        ans = ans * i
    return ans

num = int(input("Enter the number: "))
print("Factorial =", fact(num))
