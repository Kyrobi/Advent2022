# 1 A X Rock
# 2 B Y Paper
# 3 C Z Scissor

# X lose
# Y draw
# Z win sdfsdf
file = open('input.txt', 'r')
totalScore = 0
pointsToGive = {"Z": 3, "Y": 2, "X": 1}

tableDraw = {"A": "X", "B": "Y", "C": "Z"}
tableWin = {"A": "Y", "B": "Z", "C": "X"}
tableLose = {"A": "Z", "B":"X", "C": "Y"}

for line in file:
    opponent = line[0] # The opponent's choice in the first column
    outcome = line[2] # outcomer choice in the second column

        
    # Draw
    if outcome == "Y":
        if opponent == "A":
            totalScore += (pointsToGive["X"] + 3)
        elif opponent == "B":
            totalScore += (pointsToGive["Y"] + 3)
        elif opponent == "C":
            totalScore += (pointsToGive["Z"] + 3)
        continue
        
    # Lose
    elif outcome == "X":
        if opponent == "A":
            totalScore += (pointsToGive["Z"])
        elif opponent == "B":
            totalScore += (pointsToGive["X"])
        elif opponent == "C":
            totalScore += (pointsToGive["Y"])
        continue
    
    # Win    
    elif outcome == "Z":
        if opponent == "A":
            totalScore += (pointsToGive["Y"] + 6)
        elif opponent == "B":
            totalScore += (pointsToGive["Z"] + 6)
        elif opponent == "C":
            totalScore += (pointsToGive["X"] + 6)
        continue

print(totalScore)