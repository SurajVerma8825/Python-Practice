list = [1 , 4 , 4 , 7 , 7 , 4 , 8 , 9 , 12]


unique_list = []

for num in list:
    if num not in unique_list:
        unique_list.append(num)

print("Original List:", list)
print("Unique List:", unique_list)
