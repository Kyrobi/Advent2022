pointsPriority = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

set1 = set()
set2 = set()
set3 = set()

totalPoints = 0
lineCounter = 0

file = open('input.txt', 'r')

# Read the lines in the file
for lines in file:
    
    # Remove the random \n at the end of the string
    lines = lines.strip("\n")
    
    # Computes the first line
    if lineCounter == 0:
        for i in lines:
            set1.add(i)
            
        lineCounter += 1
        continue
        
    # Computes the second line
    if lineCounter == 1:
        for i in lines:
            set2.add(i)
            
        lineCounter += 1
        continue
        
    # Computes the third line
    if lineCounter == 2:
        for i in lines:
            set3.add(i)
            
        lineCounter += 1

        # Since this is the third line, we then calculate the
        # duplucates and clear the sets for the next 3 lines
        duplicate = set.intersection(set1, set2, set3)
        print("Duplicate ", duplicate)
        
        totalPoints += pointsPriority[duplicate.pop()]
        set1.clear()
        set2.clear()
        set3.clear()
        lineCounter = 0
    
print(f'{totalPoints}')
    


