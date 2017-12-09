
def hours2days(sequence):
    modulo=sequence % 24

    return int(sequence/24), modulo


def hours2days1(input_hours): 
    days = input_hours // 24
    hours = input_hours % 24 
    return days, hours

#>>> hours2days(24) # 24 hours is one day and zero hours
print(hours2days(24))
#(1, 0)
#>>> hours2days(25) # 25 hours is one day and one hour
print( hours2days(25))
#(1, 1)
#>>> hours2days(10000)
print (hours2days(10000))
#(416, 16)