array = [1,2,9,6,3,10,8,3]
for i in range (1,len(array)):
    current = array[i]
    cursor = i
    while cursor > 0 and array[cursor-1] > current:
        array[cursor] = array[cursor-1]
        cursor -= 1
    array[cursor] = current
print(array)