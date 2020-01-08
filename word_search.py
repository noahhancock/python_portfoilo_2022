#Noah hancock
questions= ["A _____ loop is based on a logical expression that evaluates to either True or False.",
"Every list element is assigned a numeric value called an ____.",
"A _____ is a type of variable that holds zero, one or more data values.",
"You can access a ____ of items by writing a starting and ending index, separated by a colon",
"Most of Python's date and time functions are kept in the _____ module.",
"To create a _____ in Python, start with a single hashtag ( # ).",
"A program will store specific data values in holding areas called ______.",
"An ____ is a data structure that stores values of same data type.",
"To create a set of values that is constant and cannot be changed, you can use a ____ instead of a list.",
"What happens when you write code that doesn't follow Python's syntax rules?",
"How you put other python libarys into your code.",
"However, your program may occasionally need to do something unexpected or ____.",
"You can call the ____() function to ask the user a question and get a string answer.",
"A  ____ is a set of statements that can be used over and over again from different places in your program.",
"allows you to run python on your computer. python ____",
"The function always starts with the ___ keyword",
"an example of this way of writing variables is 'myNumber'",
"variables that are in a functions and can't be used outside of function.",
"variables that are outside of functions that can be used anywhere.",
"when a piece of code repeats it ___ until the code it done or when it becomes false."]

PUZZLE="ESHUTHVAVRPYVIBWFUGWMTOVUTUFKRPGSRAFFJZCDCXFAINPUTLIHAJZDPYRRNVDVGBIDWDDAGZHMHLAGWILNAIRCHPFPNLMECVBOXONMYYEPCTYAXDVKZFXOWOWPJIJZYHQNWLAALBOQANQLPOELLSFJMWCZHBZKAXCLRSIUKGHPONPSYTLPKXFJVGRESEISWXKQYSITHQQOLOMVKZLLWRTQDUDGMEMFTUEMCLLTWGJPZEQRJNCASLJPOZJNQAWHJFXLGFLUPOOMTKPUNEVWMZLAHXNTILINEXGRIEBJULYMHFVCUHHXUSOFDXLXZSTNCHROFYVUROSWRPTBOLLUZRKIFWIUIMQOERAMMKLHATNUEOFXMVHMRMUVHSFENMUEVLIRLLEDFEPIPWCYVROAAQDEQHVQIPEQSKNRLOKCDZMMYFICONYEQFCBKRCCFERFEZBUGPDSHZMTNYTZQQWELUFTPBCAMELCASEVTRCIVTFUIXNGYRJCSEAIEYCLPMAWIBIFDWHCVUZCVMLHYITSQTWNMDUPNUNBTHGAKFOJSFPUYZTAGLIBVGDQHIDIYSPUKPUHRKOHPEWWVWGNEMOPENLJPZATVTOPLJHZNXHCEZXNJOFX"
##ROWS= 25
##COLO= 25
word_bank= ["while",
            "index",
            "list"
            "range",
            "datetime",
            "comment",
            "variable",
            "array",
            "tuple",
            "SyntaxErrors",
            "import",
            "random",
            "input",
            "function",
            "idle",
            "def",
            "camelcase",
            "local",
            "global",
            "loops"]
def display_grid(puzzle):
    minIndex = 0
    maxIndex = 25
    for i in range(25):
      	# Add spaces between letters
        for letter in puzzle[minIndex:maxIndex]:
            print(letter, end=" ")
        print()
        minIndex = minIndex + 25
        maxIndex = maxIndex + 25

        
used= []
def question_answer(word_bank,questions,used):
    import random
    grab= None
    while grab not in used:
        grab= random.randint(1,len(questions)-1)
        #print(grab)
        gword= word_bank[grab]
        gquestion= questions[grab]
        #print(gword)
        #print(gquestion)
        used.append(grab)
        return gword, gquestion

def create_word(puzzle):
    num=[]
    coordinate= ""
    find= input("please input your coordinates for the word your looking for\nmake sure you have a comma inbetween coordinates\n")
    for i in find:
        if i != ",":
            coordinate= coordinate + i
        else:
            if coordinate.isdigit():
                num.append(int(coordinate))
                coordinate= ""
    #print(coordinate)
    num.append(int(coordinate))
    #print(num)
    word= ""
    while num:
        x= num.pop(0)
##        y= num.pop(0)
        #add [y] to puzzle when if in a 2d form.
        word= word + puzzle[x]
    #print(word)
    return word
def game(puzzle,word_bank,questions,used):
    while len(used) < 20:
        display_grid(puzzle)
        gword,gquestion=question_answer(word_bank,questions,used)
        print(gquestion)
        word= ""
        while word != gword:
            word=create_word(puzzle)
            if word == gword:
                break
            else:
                print("try Again")
game(PUZZLE,word_bank,questions,used)
