# a = 9
# b = 8
# c = sum((a, b)) # built in function, ctrl+ Right click

def function1(a, b):
    print("Inside function1", a + b,"\n")


def function2(a, b):
    """This is a function which will calculate average of two numbers.
    Warning! this function doesnt work for three numbers"""

    average = (a + b) / 2
    # print(average)

    return average           # function Returns average because of return statement
                             # If not mentioned, it returns NONE
v = function2(5, 7)
print("Inside Function2",v)
function2(5,7)
print(function2.__doc__)        # To seee what the particular function do when there are
                                # too many function and different classes
function1(2,3)
