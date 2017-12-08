"""
Quiz: Nearest Square

Implement the nearest_square function. The function takes an integer argument limit, and returns the largest square number that is less than limit. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

There's more than one way to write this code, but I suggest you use a while loop!

Here is a test case you can copy to test your code. Feel free to write additional tests too!
"""


def nearest_square(args):
    sum = 0
    iter = 0
    while sum < args:
        iter += 1
        sum = iter**2

    return (iter - 1)**2


test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))

headlines = [
    "Local Bear Eaten by Man", "Legislature Announces New Laws",
    "Peasant Discovers Violence Inherent in System",
    "Cat Rescues Fireman Stuck in Tree", "Brave Knight Runs Away",
    "Papperbok Review: Totally Triffic"
]

news_ticker = ""

# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs


def news_limith(args):
    myline = ""
    for elem in headlines:
        if (myline.__len__() + elem.__len__() + 1) >= args:
            break
        else:
            myline = myline + " " + elem
    return myline


news_ticker = news_limith(140)
print(news_ticker + " " + str(news_ticker.__len__()))

# Define the remove_duplicates function
countries = ['Angola', 'Maldives', 'India', 'United States', 'India']


def remove_duplicates(array):
    s = []
    for i in array:
        if i not in s:
            s.append(i)
    return s


print(remove_duplicates(countries))

population = {
    'Shanghai': 17.8,
    'Istanbul': 13.3,
    'Karachi': 13.0,
    'Mumbai': 12.5
}
population["Test"]=1231)
population['Shanghai']=123
print( population)
print( population.get("Shanghai"))
