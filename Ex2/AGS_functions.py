"""
This file contains function definition for reading a file into a list,
calculating the mean, and calculating the variance.
"""

"""
Note the syntax for writing a function definition.

def name(args):

Read more about python functions in the Python docs

http://docs.python.org/release/1.5.1p1/tut/functions.html
"""
def file_to_list(filename):

    # Note the indentation of 4 spaces while we are inside a funciton.
    
    # The r tells python we are only going to read from the file
    f = open(filename, 'r')

    """
    Now that the file is open, we want to read all the numbers into a
    list. We will initialize an empty list, then append each value to it
    as we read in the file.
    """
    
    numbers = [] # An empty list

    
    """
    Pay attention to the syntax of this for loop. If you have written for
    loops in other languages, the python syntax will be new, and hopefully
    easier. It reads very intuitively, for every line in the file, we will
    do something.
    """
    for line in f.readlines():
        
        # When inside a for loop, lines need to be indented 4 spaces
        """
        txt files are read as strings, we need it to be a number. Python
        is a dynamic language, so we can deal with very easily and
        intuitively.
        """

        number = float(line)
        
        # We will add this to our list, using the append function.
        numbers.append(number)

        """
        Note the syntax with the '.'. The list type in python has several
        built in functions we can call, append being one of them. Check
        the python docs for about lists:
        http://docs.python.org/2/tutorial/datastructures.html
        """

    """
    The return value is what the user will receive when the
    function is called. We are returning the list of numbers.
    """
    return numbers



# You can put as many function definitions as you wish into a file

def mean(numbers):
    
    """
    To calculate the mean, we need to sum the numbers then divide by N
    """

    total = 0 # we will add to it
    for i in numbers:

        # The += is shorthand notation for total = total + i
        total += i

        """
        Get the number of elements in the sum, using the built in len()
        function. Check out all of pythons built in functions at:
        http://docs.python.org/2/library/functions.html
        """
    N = len(numbers)
        
    # Do the mean
    mean = total / N

    return mean

def variance(numbers, mean):
    
    """
    Now for the variance. We will loop through the numbers and calculate
    the variance. (x-x_mean)^2 / N
    """
    variance = 0 # We will add to this value in a loop
    N = len(numbers)
    
    for i in numbers:

        # Operations follow typical BEDMAS
        variance += ((i - mean) * (i - mean))/N
    
    return variance

