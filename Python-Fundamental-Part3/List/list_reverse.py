list = [1 , 4 , 7 , 4 , 8 , 9 , 12]

i = 0
j = len(list) - 1

while(i < j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    i+=1
    j-=1

print(list)

