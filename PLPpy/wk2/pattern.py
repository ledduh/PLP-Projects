for i in range(4):
    for i in range(4):
        print("# ", end="")
    print()

n = int(input("Enter value: "))
for i in range(n):
    for i in range(i):
        print("* ", end="")
    print()

for i in range(n):
    for i in range(n-i):
        print("* ", end="")
    print()

n = int(input())
for i in range(n):
    for j in range(i-1):
        print("^",end=" ")
    print()
