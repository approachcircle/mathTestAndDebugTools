# import :)
import os
import turtle
import traceback
import tkinter

# yes, i put this all in a try block
try:
    q1 = q2 = q3 = q4 = q5 = "" # question number variables
    menu = debugAns = testMethod = "" # other variables
    print("LOAD OK") # start menu
    print("Enter \"test\" or \"debug\".")
    print("debug- Shows debugging utilities availible")
    print("test- Brings you to the maths test.")
    menu = input("Option:")
    if menu == "test": # if user enters "test" then...
        os.system('cls')
        print("Please specify if you want the test to be completed automatically")
        print("or if you would like to do the test manually.")
        print("auto- Completes answers automatically")
        print("manual- Lets you answer the questions yourself.")
        testMethod = input("Option:")
        if testMethod  == "manual":
            os.system('cls') # clear text onscreen
            print("TEST OK") # begin the test
            print("Question 1/5")
            print("5 + 7")
            q1 = input("Answer:")
            if q1 == "12":
                print("Correct, the answer is 12.")
                input("Press enter to continue:")
            else:
                print("Incorrect, the answer is 12.")
                input("Press enter to continue:")
            os.system('cls')
            print("Question 2/5")
            print("3.14 + 2.42")
            q2 = input("Answer:")
            if q2 == "5.56":
                print("Correct, the answer is 5.56.")
                input("Press enter to continue:")
            else:
                print("Incorrect, the answer is 5.56.")
                input("Press enter to continue:")
            os.system('cls')
            print("Question 3/5")
            print("4.25 + 2.82")
            q3 = input("Answer:")
            if q3 == "7.07":
                print("Correct, the answer is " + q3 + ".")
                input("Press enter to continue:")
            else:
                print("Incorrect, the answer is 7.07.")
                input("Press enter to continue:")
            os.system('cls')
            print("Question 4/5")
            print("27 + 62")
            q4 = input("Answer:")
            if q4 == "89":
                print("Correct, the answer is " + q4 + ".")
                input("Press enter to continue:")
            else:
                print("Incorrect, the answer is 89.")
                input("Press enter to continue:")
            os.system('cls')
            print("Question 5/5")
            print("250 + 137")
            q5 = input("Answer:")
            if q5 == "387":
                print("Correct, the answer is " + q5 + ".")
                input("Press enter to continue:")
            os.system('cls')
            print("You finished the test! :)")
            input("Press enter to continue:")
        elif testMethod == "auto":
            os.system('cls') # clear text onscreen
            print("TEST OK") # begin the test
            print("Question 1/5")
            print("5 + 7")
            print("Answer: 12")
            input("Press enter to continue:")
            os.system('cls')
            print("Question 2/5")
            print("3.14 + 2.42")
            print("Answer: 5.56")
            input("Press enter to continue:")
            os.system('cls')
            print("Question 3/5")
            print("4.25 + 2.82")
            print("Answer: 7.07")
            input("Press enter to continue:")
            os.system('cls')
            print("Question 4/5")
            print("27 + 62")
            print("Answer: 89")
            input("Press enter to continue:")
            os.system('cls')
            print("Question 5/5")
            print("250 + 137")
            print("Answer: 387")
            input("Press enter to continue:")
            os.system('cls')
            print("You finished the test! :)")
            input("Press enter to continue:")
    elif menu == "debug": # elif the user enters "debug", then...
        os.system('cls') # clear onscreen text
        print("DEBUG OK") # begin debug
        print("exc- If this is typed, the code will raise an exception, and close.")
        print("turtle- This will run a python turtle demonstration")
        print("NOTICE: CLOSING THE TURTLE WINDOW WILL RAISE AN EXCEPTION") # notice
        debugAns = input("Option:") 
        if debugAns == "exc": # if the user enters "exc" then...
            raise Exception # THROW EXCEPTION
        elif debugAns == "turtle": # if the user enters "turtle" then...
            turtle.speed(10) # begin the turtle... mess
            for i in range(20):
                turtle.forward(50)
                turtle.left(100)

            turtle.penup()
            turtle.forward(100)
            turtle.pendown()
            for i in range(20):
                turtle.forward(50)
                turtle.left(100)

            turtle.penup()
            turtle.right(150)
            turtle.pendown()
            for i in range(20):
                turtle.forward(50)
                turtle.left(100)

            turtle.penup() # AAAAAAAAAAAAAAAAAAAAAAA
            turtle.right(150) # AAAAAAAAAAAAAAAAAAAAAAA
            turtle.pendown() # AAAAAAAAAAAAAAAAAAAAAAA
            for i in range(20): # AAAAAAAAAAAAAAAAAAAAAAA
                turtle.forward(50) # AAAAAAAAAAAAAAAAAAAAAAA
                turtle.left(100) # AAAAAAAAAAAAAAAAAAAAAAA
except Exception: # this catches any exceptions thrown
    input("oops, an exception occured :/ press enter for debug info...") # friendly exception notice
    traceback.print_exc() # print the exception
    input("Press enter to continue:")
print("-END-")
input("Press enter to terminate python job")
