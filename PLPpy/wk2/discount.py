purchased_quantity = int(input("Enter quantity of items: "))
item_cost = 0
per = 90/100
def item_costing(item_cost):
    if purchased_quantity > 1000:
        print(" The item cost is: ", (item_cost * per*purchased_quantity))
    elif purchased_quantity < 1000:
        print(" The item cost is: " , item_cost * purchased_quantity)
    else:
        print("Invalid")

item_costing(100)