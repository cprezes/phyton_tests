elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
            
#elements['hydrogen']={'number': 1, 'weight': 1.00794, 'symbol': 'H','is_noble_gas':False}
#elements['helium']={'number': 2, 'weight': 4.002602, 'symbol': 'He','is_noble_gas':True}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True


print(elements)     

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't



print(elements['hydrogen']['is_noble_gas'])
#False
print(elements['helium']['is_noble_gas'])
#True

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}




def total_takings0(yearly_record):
    sum=0
    for x in yearly_record:
               for x in yearly_record[x]:
                   sum +=x
    return sum

def total_takings(yearly_record):
    #total is used to sum up the monthly takings
    total = 0
    for month in yearly_record.keys():
        #I use the Python function sum to sum up over 
        #all the elements in a list
        total = total + sum(yearly_record[month])
    return total


print (total_takings(monthly_takings))