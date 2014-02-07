"""
This script will read in numbers from a file, then calculate the mean
and variance.
Note the triple quotation marks around this text. This is the python
syntax for a long comment that read or executed by the interpretor.
"""

# Note the hashtag is the syntax for single line comments.

"""
Read in the file. Python has a native file reader function for reading
a file from disk. Read the description of the function in the Python
docs: http://docs.python.org/2/library/functions.html#open
"""

# The r tells python we are only going to read from the file
f = open('sample_data.txt', 'r')

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

# Note the indentation is finished, telling python the for loop is done

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

# Print function will write a message to the interpretor
print("Mean = ", mean)

"""
Now for the variance. We will loop through the numbers and calculate
the variance. (x-x_mean)^2 / N
"""
variance = 0 # We will add to this value in a loop

for i in numbers:

    # Operations follow typical BEDMAS
    variance += ((i - mean) * (i - mean))/N

print("Variance =", variance)
