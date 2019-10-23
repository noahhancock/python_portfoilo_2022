import random
HANGMAN = (
"""
--------
 1      1
 1      
 1    
 1    
 1  
 1  
 1 
------------
""",
"""
--------
 1      1
 1      o
 1
 1
 1
 1
 1
------------
""",
"""
--------
 1      1
 1      o
 1    /-+
 1
 1
 1
 1
------------
""",
"""
--------
 1      1
 1      o
 1    /-+-\\
 1  
 1  
 1 
 1 
------------
""",
"""
--------
 1      1
 1      o
 1    /-+-\\
 1      1
 1      1
 1 
 1 
------------
""",
"""
--------
 1      1
 1      o
 1    /-+-\\
 1      1
 1      1
 1     1 
 1     1  
------------
""",
"""
--------
 1      1
 1      o
 1    /-+-\\
 1      1
 1      1
 1     1  1
 1     1  1
------------
""")

MAX_WRONG= len(HANGMAN) -1
WORD_BANK=("PIE",
           "CLAM",
           "GUAM",
           "TIME",
           "PYTHON",
           "NOAH",
           "ADVENTURE",
           "GOOGLE",
           "ANALYSIS")

word = random.choice(WORD_BANK)
so_far="-" * len(word)

wrong= 0
used= []

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:

    print(HANGMAN[wrong])
    print("\nYouv'e used the following letters:\n", used)
    print("\nSo far the word is:\n", so_far)

    guess= input("\n\nEnter your guess: ")
    guess= guess.upper()

    while guess in used:
        print("You've alrady guessed the letter", guess)
        guess= input("\n\nEnter your guess: ")
        guess= guess.upper()
    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "is in the word!")
        new= ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far= new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong+= 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print( "\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was", word)
input("\n\nPress the enter key to exit.")
