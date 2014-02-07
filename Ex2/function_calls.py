"""
import additional functionality, the os module which has useful
functions for dealing with directory structures. Read more about
the os module in the PYDOCS:
http://docs.python.org/2/library/os.html
"""
import os

# Note the "as" You can rename modules to better suit your namespace
import AGS_functions as AGS


"""
This script will read in all files in a folder, calculate the mean
and variance, and keep the results in a dictionary
"""

"""
Read more on dictionaries in the PYDOCS:
http://docs.python.org/2/tutorial/datastructures.html#dictionaries
"""

directory = "all_sample_data"
# An empty dictionary
out = {}

# Use the power of the os module to make it easy
for f in os.listdir(directory):

    # Note the use of namespace to access our functions

    # os.path module makes it easy to make the full path
    data = AGS.file_to_list(os.path.join(directory,f))
    mean = AGS.mean(data)
    variance = AGS.variance(data, mean)

    # Note the syntax of adding elements to a dictionary
    out[f] = (mean, variance)

for i in out:
    print(i, out[i])
