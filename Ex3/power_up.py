import numpy as np
"""
matplotlib is pythons plotting library that behaves similarily to
matlab. Most of the plotting functions are called through the pyplot
namespace
"""
from matplotlib import pyplot as plt
import os

directory = "all_sample_data"
data = {}

# Use the power of the os module to make it easy
for f in os.listdir(directory):

    # Note the use of namespace to access our functions

    # numpy has already solved our problem!
    data[f] = np.loadtxt(os.path.join(directory,f))
    

"""
With numpy, we have a lot of power. For starters, we can use numpy to
calculate means, standard deviations, variances.
"""

# Do some calculations on data from the sample_22 file
mean_22 = np.mean(data["sample_22"])
var_22 = np.var(data["sample_22"])
std_22 = np.std(data["sample_22"])
print(mean_22, var_22)

"""
As a recap, the initial function you wrote, could be done in three
lines of code using scientific python:
data = np.loadtxt(file)
mean = np.mean(data)
variance = np.var(data)

Compare this to someone trying to do something similar in C:
http://cboard.cprogramming.com/cplusplus-programming/131759-calculating-standard-deviation-file-i-o.html

Most important, compare the syntax and human readability. This is one
of pythons strong points.
"""


"""
There is so much capability in numpy and scipy. Read some of the docs
and try out some of the functionality:
http://scipy.org/docs.html
"""

"""
Convolution is a fairly complicated mathematical operation that
requires nested loops and edge case handling. Fortunately, everything
is implemented for us. Read the docs:
http://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html
"""
conv_15_45 = np.convolve(data["sample_15"], data["sample_45"])

"""
Maybe we want to look at spectrum? Fourier transforms, already been
solved.

Think about the syntax on this one. In numpy, there is an fft
library with fourier related functions. From this library, we are
using the fft function. Try to read the docs and make sense of this:
http://docs.scipy.org/doc/numpy/reference/routines.fft.html
http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html#numpy.fft.fft
"""
fft_45 = np.fft.fft(data["sample_45"])


"""
======================================================================
We are now going to demonstrate some of the matplotlib functions.
Scientific computing usually consists of reading data, manipulating
data, then visualizing data. MPL will help us visualize. Check out
the webpage:
matplotlib.org/
"""

"""
An example of a basic plot
"""
fig1 = plt.figure() # Make a new figure window
plt.plot(data["sample_200"]) # Build the plot

"""
Lets do the same thing, but now plot the mean as well
"""
mean_200 = np.mean(data["sample_200"])

# The mean is one value, lets make it an array
mean = np.repeat(mean_200, len(data["sample_200"]))
plt.plot(mean, color="red") # add the series to the plot, in red

# Lets add some titles, and axis labels
plt.title("Sample 200")
plt.xlabel("sample")
plt.ylabel("value")

"""
See more things you can do in the pyplot docs:
http://matplotlib.org/api/pyplot_api.html
"""

plt.show() # Send the plot to the figure


"""
We will do some multiplots and build up some more examples of MPL.
There are many online examples and tutorials, so feel free to self
learn as much as you can.
"""

# Make a new figure
fig2 = plt.figure()

"""
Read the docs http://matplotlib.org/api/pyplot_api.html to
understand the syntax
"""

# First indicate the active plot. 2 rows, 2 columns, first cell
plt.subplot('221')

# Tighten the layout so everything fits
plt.tight_layout()

# Plot the raw data
plt.plot(data["sample_900"])

# Add titles etc.
plt.title("Sample 900")
plt.xlabel("sample")
plt.ylabel("value")

# Plot a histogram in the next cell. Again, check docs and explore
plt.subplot('222')

# Tighten the layout so everything fits
plt.tight_layout()

plt.hist(data["sample_900"], bins=10)

# Add titles etc.
plt.title("Histogram")
plt.xlabel("value")
plt.ylabel("count")

# Plot a zoomed view in the next cell. Again, check docs and explore
plt.subplot('223')

# Tighten the layout so everything fits
plt.tight_layout()


plt.plot(data["sample_900"])
plt.xlim(50,200)
plt.title("Zoomed")

# Finally, lets do an autocorrelation
plt.subplot('224')

# Tighten the layout so everything fits
plt.tight_layout()

plt.acorr(data["sample_900"])
plt.title("autocorrelation")

# Show the figure
plt.show()


