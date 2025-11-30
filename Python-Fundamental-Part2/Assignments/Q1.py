salary = int(input("Enter your salary: "))

if salary <= 30000:
    cut = (salary * 5) / 100
    print(f"\nYour salary falls in the 5% deduction range.")
    print(f"Total Deduction: ₹{cut}")
    print(f"Salary After Deduction: ₹{salary - cut}")

elif 30000 < salary <= 70000:
    cut = (salary * 15) / 100
    print(f"\nYour salary falls in the 15% deduction range.")
    print(f"Total Deduction: ₹{cut}")
    print(f"Salary After Deduction: ₹{salary - cut}")

elif salary > 70000:
    cut = (salary * 25) / 100
    print(f"\nYour salary falls in the 25% deduction range.")
    print(f"Total Deduction: ₹{cut}")
    print(f"Salary After Deduction: ₹{salary - cut}")
