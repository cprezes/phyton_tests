def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

print( cylinder_volume(10, 3))

def print_greeting():
    print('Hello World!')

print_greeting()


def population_density(x,y):
    return x/y
    

# Here are test cases to verify that your function works as expected:
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))


def print_testcase(expected_value, actual_value):
    print("expected value: {}, actual value: {}".format(expected_value, actual_value))
    
print_testcase(expected_result2,test2)

