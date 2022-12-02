file = open('input.txt', 'r')
totalScore = 0
optionPoints = {"Z": 3, "Y": 2, "X": 1}

for line in file:
    opponent = line[0] # The opponent's choice in the first column
    you = line[2] # Your choice in the second column

    # Fetch to points for picking certain options
    totalScore += optionPoints[you]
        
    # All draw conditions
    if (opponent == "A" and you == "X") or (opponent == "B" and you == "Y") or (opponent == "C" and you == "Z"):
        totalScore += 3
        
    # All winning conditions
    elif (opponent == "A" and you == "Y") or (opponent == "B" and you == "Z") or (opponent == "C" and you == "X"):
        totalScore += 6

print(totalScore)