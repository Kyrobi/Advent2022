listOfValues = []
tempList = []
highest = 0

with open('input.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            listOfValues.append(tempList.copy())
            tempList.clear()
            break
        
        if line == "\n":
            listOfValues.append(tempList.copy())
            tempList.clear()
            continue;
        
        # Converts line to int
        tempList.append(int(line.strip()))
    
    for idx, i in enumerate(listOfValues):
        if sum(i) > highest:
            highest = sum(i)
        tempList.append(sum(listOfValues[idx]))
    
    print(tempList.sort(reverse=True))
    
    print(f'Elf with the highest calories: {highest}') 
    
    print("Sum of top 3 elves:", tempList[0] + tempList[1] + tempList[2])