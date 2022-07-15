mark = int(input("Enter average score: "))
if mark > 70 and mark <= 100: 
    print("A")
elif mark > 60 and mark<= 69:
    print("B")
elif mark > 50 and mark<= 59:
    print("C")
elif mark > 40 and mark<= 49:
    print("D")
elif mark > 0 and mark<= 39:
    print("E")
elif mark > 100:
    print("Invalid")
else:
    print("Fail")

