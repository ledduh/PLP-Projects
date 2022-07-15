salary = int(input("Enter your current salary: "))
yearofservice = int(input("Enter your service years: "))

def employee():
    sal = salary * 5/100
    if yearofservice >=5:
        print (sal)
    else:
        print (salary)

employee()