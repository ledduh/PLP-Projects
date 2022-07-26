import math
hours = 1
minutes = 45

hours1 = 2
minutes2 = 60

class Time():
   
    
    def displayTime():
        print("The time is",hours,":",minutes)

    def displayMinute():
        v = minutes + (hours * 60)
        print(v,"minutes")

    def addTime(t1, t2):
        t1 = hours + hours1
        t2 = minutes + minutes2
        t3 = t1+math.ceil(t2/60)
        if t2 > 60:
            print(t3, "hours and ", (t2%60), "minutes.")
        else:
            print(t1, "hours and ", t2, "minutes.") 

Time.addTime(hours,minutes)
Time.displayTime()
Time.displayMinute()

SampleDictionary = {0: 10, 1: 20}

def adddictionary(n,x):
    SampleDictionary [n] = x
    print (SampleDictionary)

adddictionary(2,30)