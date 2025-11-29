num = input("Enter the value of number ")

# Split the number based on decimal point
parts = num.split(".")

# Integer part
numint = int(parts[0])
print("Integer part:", numint)

# Fractional part
fractional_part = "." + parts[1]
print("Fractional part:", fractional_part)
