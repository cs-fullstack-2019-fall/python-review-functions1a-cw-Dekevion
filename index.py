
### Problem 1
#Create a ```printNumbers``` function to print integers from -25 to 20
# to the console (print in the function)

def printNumber():
    for x in range(-25, 21, 1):
        print(x)

printNumber()


### Problem 2
#Create a function called checkPassword.
# Send two string variables to the checkPassword function to check
# if the strings are equal.
# Return true if they are equal and false if they are not equal.
# Print the function's return value.

def checkPassword(a,b):
    if a == b:
        print("true")
    else: print('false')

checkPassword('abc','blah blah')


### Problem 3
#  function that determines if a number passed to it is odd or even.
# Pass a number of your choosing (using input a good idea)
# and then using the result from the function,
# print if the number was even or not.
#
# examples:
# ```
# The number 12 is an even number!
#
# The number 5 is an odd number!
# ```
#
def oddEven ():
    var_a = int(input('Enter number'))
    if var_a % 2 > 0:
        print('this is an odd number')
    else: print('this is even')

oddEven()

# ### Problem 4
#  Create a function for the challenge that you call from your ```main```
#  Create a *second* function that takes NO parameters
# * Create a *third* function that takes a single greeting parameter (ex. ```Howdy```)
# and returns a string using the passed in greeting
# and 'World' (ex. ```Howdy World!```)
# * From your *first* function,
# call the function(s) and print out the final result returned


def main():
    func2()

def func2():
    func3('Hello')

def func3(greeting):
     print(greeting + ' world')

# def func3(greeting):
#
#     greeting = 'world'

main()