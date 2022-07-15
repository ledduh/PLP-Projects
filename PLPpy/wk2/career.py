career = input("Your career: ")
questions = input("Do you think it is hard or easy? ")
careers = ["teacher", "coder", "builder"]
# print(careers)
careers_advice = ["Good career choice", "Bad career choice"]
careers_questions = ["hard", "easy"]

def all():
    if career in careers:
        
        if questions == careers_questions[0]:
            print(careers_advice[1])
        elif questions == careers_questions[1]:
            print(careers_advice[0])
    else: 
        print("Error in input")
    
all()

