import os
import turtle
import traceback
import tkinter
try:
    q1 = ""
    q2 = ""
    q3 = ""
    q4 = ""
    q5 = ""
    menu = ""
    debugAns = ""
    print("LOAD OK")
    print("Enter \"test\" or \"debug\".")
    print("debug- Shows debugging utilities availible")
    print("test- Brings you to the maths test.")
    menu = input("Option:")
    if menu == "test":
        os.system('cls')
        print("TEST OK")
        print("Question 1/5")
        print("5 + 7")
        q1 = input("Answer:")
        if q1 == "12":
            print("Correct, the answer is 12.")
            input()
        else:
            print("Incorrect, the answer is 12.")
            input()
    elif menu == "debug":
        os.system('cls')
        print("DEBUG OK")
        print("exc- If this is typed, the code will raise an exception, and close.")
        print("turtle- This will run a python turtle demonstration")
        print("(CLOSING THE TURTLE WINDOW WILL RAISE AN EXCEPTION)")
        debugAns = input("Option:")
        if debugAns == "exc":
            raise Exception
        elif debugAns == "turtle":
            PLACEHOLDER = ""
            for PLACEHOLDER in range(20):
                turtle.forward(50)
                turtle.left(100)
except Exception:
    input("oops, an exception occured :/ press enter for debug info.")
    traceback.print_exc()
    input("Press enter to continue.")
print("-END-")
input("Press enter to terminate.")