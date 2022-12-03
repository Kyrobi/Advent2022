# 1 A X Rock
# 2 B Y Paper
# 3 C Z Scissor

# X lose
# Y draw
# Z win
file = open('input.txt', 'r')
totalScore = 0
pointsToGive = {"Z": 3, "Y": 2, "X": 1}
tableDraw = {"A": "X", "B": "Y", "C": "Z"}
tableWin = {"A": "Y", "B": "Z", "C": "X"}
tableLose = {"A": "Z", "B": "X", "C": "Y"}

for line in file:
    opponent = line[0] # The opponent's choice in the first column
    outcome = line[2] # outcome in the second column
        
    # Draw
    if outcome == "Y":
        # In a draw situation, we fetch from a dictonary to see which wee need to play to draw. Then we take the value and use
        # that as a key to find how many points to give.
        totalScore += (pointsToGive[tableDraw[opponent]] + 3)
    
    # Lose
    elif outcome == "X":
        totalScore += (pointsToGive[tableLose[opponent]])
    
    # Win    
    elif outcome == "Z":    
        totalScore += (pointsToGive[tableWin[opponent]] + 6)

print(totalScore)