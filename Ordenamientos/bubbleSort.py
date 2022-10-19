array = [1,2,9,6,3,10,8,3]
for i in range (len(array)):
    for j in range (len(array)-1):
        if (array[j+1] < array[j]):
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print(array)