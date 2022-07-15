books = int(input("Books: "))
if books == 0:
    print("Points: 0")
elif books == 1:
    print("Points: 6")
elif books == 2:
    print("Points: 16")
elif books == 3:
    print("Points: 32")
elif books >= 4:
    print("Points: 60")
else:
    print("Invalid")

