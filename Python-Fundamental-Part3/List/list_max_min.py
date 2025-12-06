list = [26 , 32 , 56 ,1 , 4 , -7 , 4 , 8 , 9 , 12]



min = list[0]
max = list[0]

for i in range(0 , len(list)):
    if(list[i] > max):
        max = list[i]
    elif(list[i] < min):
        min = list[i]


print("Maximum = " , max)
print("Minimu = ",min)
