# divisible by 7 multiply between 1500 and 2700
x = 0
for i in range (1500,2701):
    if (i%7==0):
        print(i)


# Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

cel = int(input("Enter the temperature in celcius: "))
fahr = int(input("Enter the temperature in Fahrenheit: "))
c = (fahr-32)*5/9
f = (cel*9/5)+32

print("The temperature from Fahrenheit to celcius is:", c ,"\nThe temperature from celcius to Fahrenheit  is: ",f)
