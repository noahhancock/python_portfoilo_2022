#Noah Hancock
#midterm test taking code
#12/9/19
import sys

def open_file(file_name,mode):
    """ opens file in the given mode"""
    try:
        file= open(file_name,mode)
        return file
    except IOError as e:
        print("unable to open the file", file_name,"Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()

def next_line(the_file):
    """reads the next line in the file and formats it for our program"""
    line= the_file.readline()
    line= line.strip("\n")
    line= line.replace("/","\n")
    return line

def question_block(the_file):
    category= next_line(the_file)
    question= next_line(the_file)
    answers= []
    for i in range(4):
        answers.append(next_line(the_file))
    correct= next_line(the_file)
    if correct:
        correct= correct[0]
    explanation= next_line(the_file)
    return category,question,answers,correct,explanation

def welcome(title):
    """Welcome the player and get his/her name"""
    print("\t\tWelcome to my python test")
    print("\t\t This test was made by me", title,"\n")


def main():
    file_name= get_file_name()
    file= open_file(file_name,"r")
    title= next_line(file)
    name= input("Enter in your full name: ")
    questions= 0
    score= 0
    category,question,answers,correct,explanation= question_block(file)
    welcome(title)
    while category:
        print(category)
        print()
        print(question)
        print()
        for i in range(len(answers)):
            print("\t", i + 1, "-", answers[i])
        user_answer= input("What is your answer?: ")
        if user_answer == correct:
            score += 1
            questions += 1
            print("correct")
        else:
            questions += 1
            print("wrong")
        print()
        print(explanation)
        category,question,answers,correct,explanation= question_block(file)
        
    file.close()

    print("That was the final question!")
    report_card(name,questions,score) ##### you passed in question not questions

def get_file_name():
    while True:
        file= input("enter the test file name: ")
        if ".txt" in file and " " not in file:
            return file
        else:
            print("Thats not a good file name")
def report_card(name,questions,score):
    print("REPORT CARD")
    print("student name:",name)
    print("there was",questions,"number of questions")
    print("You got",score,"number of questions right")
    print("each question was worth 1 point")
    right= score/questions
    if right >= .90:
        letter= "A"
    elif right >= .80:
        letter= "B"
    elif right >= .70:
        letter= "C"
    elif right >= .60:
        letter= "D"
    else:
        letter= "F"
    print("you got",right,"percent your letter grade is",letter)
    input("press enter to close")
    write_score(name,right)

def write_score(name,score):
    file= open_file("others_score.txt","a+")
    pair= name+": "+str(score)+"\n"
    line= []
    line.append(pair)
    file.writelines(line)
    file.close()
    
main()
