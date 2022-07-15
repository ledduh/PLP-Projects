#  1 gallon = 115sqfeet = 8hrs labor
# 20$ per hour labor
# Enter sqfeet of wall space
# Price of paint per gallon

square_feet = int(input("Now: "))
# gallon = 1
# hourss = 8
# labor = 20
# def per_hour():
    # change gallons to litres 1gallon = 4.55
hours = 115/8
gallons = 115/4.55
labor = 20
paint_cost = 10
#     print(hours)
#     print(gallons)
# # per_hour()
# no_of_gallons = 0
# hours_of_labor = 0
# cost_of_paint = 0 
# cost_of_labor = 0
# total_cost = 1
# def paint():

no_of_gallons = (gallons * square_feet)/4.55
hours_of_labor = hours * square_feet
# Assume paint per gallon is $10
cost_of_paint = paint_cost * no_of_gallons
cost_of_labor = labor * hours_of_labor
total_cost = cost_of_labor + cost_of_paint


print("Paint required is: ", no_of_gallons, 
    "\nHours of labor required: ", hours_of_labor,
    "\nCost of the paint: ", cost_of_paint,
    "\nLabor charges: ", cost_of_labor,
    "\nTotal cost of paint job: ", total_cost)
# paint()