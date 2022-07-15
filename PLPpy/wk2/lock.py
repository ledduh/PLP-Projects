# door lock
import datetime


passcode = "opensesame"
entered_password = input("Enter password: ")
def check():
    if entered_password != passcode:
        print("Wrong credentials re-enter password ")
    elif entered_password == passcode:
        print("The door is now open", datetime())
    elif entered_password == "close":
        print("The door is now locked")
    elif entered_password == "quit":
        print("You quit this door")
    else:
        print("Invalid input")
check()
# not done
