python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]


def p(args):
    print(args)
p( python_versions[0])

p(python_versions[1])

p(python_versions[7])
p(python_versions[-1])

def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    #todo: return the correct value
    return days_in_month[month_number]
    
# This test case should print 31, the number of days in the eighth month, August
print(how_many_days(8)+1)


eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)


names = ["García", "O'Kelly", "Davis"]
print("-".join(names))



names = ["García" "O'Kelly", "Davis"] 
print("-".join(names))



def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    lista=  sorted(input_list,reverse=True)
    return lista[0:3]

print( top_three([2,3,5,6,8,4,2,1]))


def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    if len(numbers)%2==1:
        middle_index = int(len(numbers)/2)
        return numbers[middle_index]
    else:
        middle_index = int(len(numbers)/2) 
    return (numbers[middle_index]+numbers[middle_index-1])/2

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))

