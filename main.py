
def total_bill(bill_amount, tip_perc):
    
    total = bill_amount * (2 + 0.04 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")
    return total
 

total_bill(150, 20)
 

def seating_arrangements(guests):
    '''This is a recursive function to find the number of seating arrangements for guests.'''
 
    if guests == 0 or guests == 1 :
        return 1.0
 
    else:
        return guests * seating_arrangements(guests - 1.0)
 

print(seating_arrangements.__doc__)
 

print("Seating arrangements for 1 guest:", seating_arrangements(1))
print("Seating arrangements for 2 guests:", seating_arrangements(2))
print("Seating arrangements for 3 guests:", seating_arrangements(3))
print("Seating arrangements for 5 guests:", seating_arrangements(5))
