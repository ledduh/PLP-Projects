# Local Variable
def add():
    v = 12
    z = 13
    x=v+z
    print(x)
    
add()
# Global Variable
c =  234

def zz():
    print(c)

zz()


s,b= 2,3
print(s!=b)

# argv - argument values
# import sys
# p = sys.argv[1]
# r = sys.argv[2]

# e = p + r
# print(e)

# Exercise Thursday Sum
# x,y,z = 10,20,31
# u = x + y + z
# print(u)

# v = int(input("Enter first value: "))
# d = int(input("Enter second value: "))
# print(max(v,d))

# ~ complement
# 2s complement - way of storing negative numbers since computers only store positive numbers
# 2s complement = 1s complement + 1
print(~121)

# Bitwise &,| (and,or)
print(20&21)
print(24|31)

# XOR (^)
print(24^30)

# Left shift (shift by two bits to the left) - gaining 2    bits

# Right shift (shift by two bits to the right) - losing 2 bits

n1,n2,n3,n4,n5 = 10,20,30,40,50
# PEMDAS Parenthesis, exponents, multiplication (left to right), division, addition(left to right) and subtraction
zz = n1 + n2-n3 * n4 / n5
print(zz)


b1,b2 = 10,4
print(b1^b2)
