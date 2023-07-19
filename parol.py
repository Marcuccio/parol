import random
import string

vocabulary = [line.strip() for line in open('vocabolario.txt', encoding="utf-8")]

M = 4
N = 4

permutations = 0

# binary search
def lookup(item):

    candidates = []
    low = 0
    high = len(vocabulary) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if vocabulary[mid] < item:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif vocabulary[mid] > item:
            high = mid - 1
 
        # means x is present at mid
        else:
            break
        
    if vocabulary[mid] == item:
        candidates.append(item)
    if mid < len(vocabulary):
        if vocabulary[mid+1].startswith(item):
            candidates.append(vocabulary[mid+1])
    
    return candidates   

def find_words_util(parol, visited, i, j, guess, found_words):
    # Mark current cell as visited and
    # append current character to guess
    visited[i][j] = True
    guess = guess + parol[i][j]

    global permutations
    permutations += 1
    
    candidates = lookup(guess)
    if len(candidates) > 0:

        if guess == candidates[0] and guess not in found_words and len(guess) > 3:
            found_words.add(guess)

        # Traverse adjacent cells
        row = i - 1
        while row <= i + 1 and row < M:
            col = j - 1
            while col <= j + 1 and col < N:
                if (row >= 0 and col >= 0 and not visited[row][col]):
                    find_words_util(parol, visited, row, col, guess, found_words)
                col+=1
            row+=1

    # Erase current character from guessing and
    # mark visited of current cell as false
    candidates = []
    guess = "" + guess[-1]
    visited[i][j] = False

# Prints all words present in vocabulary.
def find_words(parol):

    # Mark all characters as not visited
    visited = [[False for i in range(N)] for j in range(M)]    

    found_words = set()
    
    guess = ""
    
    # Consider every character and look for all words
    # lowing with this character
    for i in range(M):
        for j in range(N):
            find_words_util(parol, visited, i, j, guess, found_words)

    return found_words

parol = [[random.choice(string.ascii_uppercase) for i in range(N)] for j in range(M)]
#parol = [['P', 'O', 'Q', 'B'], ['I', 'T', 'A', 'S'], ['T', 'L', 'Y', 'S'], ['G', 'O', 'Y', 'L']]

print(parol) 

found_words = find_words(parol)

print("Found words: ")
for w in found_words:
    print(w)
print("Number of steps: ", permutations)