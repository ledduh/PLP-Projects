def play():
    print("H")
    print("P")

def add_sub(x,y):
    b = x+y
    c= x-y
    return b,c

result1, result2= add_sub(10,2)
print(result1, result2)


def update(x):
    x = 10
    print(x)
update(12)
# Pass/call by value it passes as a value not a variable // Not applicable in python
# Pass by reference it passes the address itself //Not applicable in python
# if id is same value will change