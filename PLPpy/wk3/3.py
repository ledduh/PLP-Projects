# Accept rate, principle and time to calculate, simple interest

# # arguements return interest



# Simple interest
def simple_interest(rate,principle,time_to_calculate_months):
    SI = principle*rate*time_to_calculate_months
    print(SI)

simple_interest(10/100, 10000, 24)

# Sum
def total(v,b):
    x = v + b
    if x in range(15,20):
        return 20
    else:
        return x

result = total(10,12)
print(result)

# Rectangle perimeter and area

def rect_per(d,e):
    area = d*e
    perimeter = 2 * (d+e)
    return area, perimeter

result1, result2 = rect_per(10,2)
print(result1, result2)