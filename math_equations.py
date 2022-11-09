########################################################################################################################
########################################################################################################################
# How to code math equations?
########################################################################################################################
########################################################################################################################
"""
I will explain step by step how to code a math equation.

proceed in order of
Basic 
Intermediate
Advanced 
Quantum :) (Maybe) 

Respectively;
simple math operations,
equations with one unknown,
variance and standard deviation, confidence interval and Pearson correlation coefficient.
Last but not least,  simple linear regression equation.
"""
########################################################################################################################
########################################################################################################################
# Start with Basics
########################################################################################################################
########################################################################################################################
"""
I'm getting straight to the point, assuming everyone knows the Python math operators.
You can refer to 1st link in the Resources  for more details.
"""
########################################################################################################################
########################################################################################################################
"""
x + 3 = 2

x plus 3 equals to 2 

solution simple right ?
"""
x = 2 - 3
########################################################################################################################
########################################################################################################################
"""
let's try another equation.
the following equation is twice of x plus 1 is equal to 5.
2x + 1 = 5
So let's leave x alone. it looks like someone who wants to be alone. :)
So:
2x + 1 -1 = 5 - 1
2x = 5-1
2x = 4
x = 4/2
"""
x = 4/2
########################################################################################################################
########################################################################################################################
# Intermediate
########################################################################################################################
########################################################################################################################
"""
Let's jump from boring simple operations to some more fun stuff. :)
Variance , Standard Deviation , Confidence Interval , Pearson Correlation Coefficient
"""
########################################################################################################################
########################################################################################################################
# Variance
########################################################################################################################
########################################################################################################################
"""
Variance is a measure of dispersion, 
meaning it is a measure of how far a set of numbers is spread out from their average value.

More mathematical sentence;

Subtract the mean from each value,
Square each of the resulting values,
then sum all values.

There is a variance formula in the link below.
https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/main/variance.svg

S2  =  sample variance  (S exponent 2)
Xi  =  the value of the one observation
x̄   =  the mean value of all observations
n   =  the number of observations
Σ   =  the summation symbol i.e. sum of observations (The upper case letter sigma)

Below subtract all values from the mean with a for loop. 
And square all the values and add them all.
Finally, subtract 1 from the sample number and divide by the total number we find.
"""

var_sample = random.normal(size = 11)

var_n = len(var_sample)

var_mean = sum(var_sample) / len(var_sample)

var = sum((var_i - var_mean)**2 for var_i in var_sample) / (var_n - 1)

"""
I am adding the stages of the above code to the below so that it can be followed easily.

var =                           for var_i in var_sample                 # get the values with for loop
var =      var_i - var_mean     for var_i in var_sample                 # subtract all values from the mean
var =     (var_i - var_mean)**2 for var_i in var_sample                 # square all subtracted values
var = sum((var_i - var_mean)**2 for var_i in var_sample)                # add up all squared values
var = sum((var_i - var_mean)**2 for var_i in var_sample) / (var_n-1)    # Divide add up all squared values by the number of sample values minus 1.
"""
########################################################################################################################
########################################################################################################################
# Standard Deviation (Sample)
########################################################################################################################
########################################################################################################################
"""
Standard deviation is a measure of the amount of variation or dispersion of a set of values.

https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/905d939b13d8ba0a8c1012f72c260032e4b8295c/sample_standard_deviation.svg

If look closely at the equation in the link above, 
can see that the standard deviation is actually the square root of the variance.

s  =  sample standard deviation
N  =  the number of observations
x̄  =  the observed values of a sample item
Σ  =  the summation symbol i.e. sum of observations (The upper case letter sigma)
"""
std = (sum((var_i - var_mean)**2 for var_i in var_sample) / (var_n - 1))**0.5

# or

var**0.5 # exponent 0.5 means square root

# or

import math

math.sqrt(var)

########################################################################################################################
########################################################################################################################
# Confidence Interval
########################################################################################################################
########################################################################################################################
"""
Confidence interval (CI) is a range of estimates for an unknown parameter. 
A confidence interval is computed at a designated confidence level; 
the 95% confidence level is most common, but other levels, such as 90% or 99%, are sometimes used. 
The confidence level represents the long-run proportion of corresponding CIs that contain the true value of the parameter. 
For example, out of all intervals computed at the 95% level, 95% of them should contain the parameter's true value. 

More mathematical sentence;

Confidence Interval is the sample mean minus/plus the z-score multiply the standard deviation divided by the square root of the sample size.

https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/bb808b792d837685a340ac2fb8dc037860bcc455/confidence_interval.svg

CI =  confidence interval

x̄  =  sample mean

z  =  confidence level value (z-score)

s  =  sample standard deviation

n  =  sample size
"""

from numpy import random

# sample x
x = random.normal(size = 29)

# mean of x
x_mean = sum(x)/len(x)

# size of sample
n = len(x)

# standard deviation of x
"""
I explained how to find the standard deviation above. 
But let's go over it again. 
All values are subtracted from the mean and the found values are squared. 
Then add them all up and divide by the number of elements minus 1. 
Then calculate the square root of the resulting number.
"""

x_std = (sum((x_i - x_mean)**2 for x_i in x) / (n - 1))**0.5


# Z-Score (or standard score)
"""
standard score or z score is the number of standard deviations by which the value of a raw score 
(i.e., an observed value or data point) is above or below the mean value of what is being observed or measured. 
Raw scores above the mean have positive standard scores, while those below the mean have negative standard scores.

https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/3d6cc70d78ee2f3a1ba297a504b2dc4b7089d8db/z_score.svg
https://github.com/bunyaminergen/how_to_code_math_equations/blob/main/z_score.gif?raw=true

How is the Z score calculated? If we're going to take the confidence interval as 95%, which can be taken as 99%, at 90%, the choice is up to you.
Then let's look at the red area in the image above. That's our safe zone. :)
That region represents 95%, that is, 0.95.
So what is the area left and right?
If the whole area is 1, subtract 0.95 from 1, we get these two areas, so 1 - 0.95 = 0.5.
And if we divide that by two, we get the areas and on the right. That's 0.5/2 = 0.025.
Let's do this with the formula.
"""

(1-0.95)/2

"""
Let's find the z-score. 
Focus on blue area in the image above. 
If the bottom of the whole curve is 1 and the area on the right is 0.025, 
then the blue area on the left is 1 - 0.025.

https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/main/positive-z-score-table.png
"""

1 - 0.025
# 0.975

"""
If we find the number we found above from the table and add the numbers on the axis, we get the following number.
"""

1.9 + 0.06

# 1.96

"""
Now that we have found all the unknowns, let's put them in the equation and implamate.
Here implamate the plus/minus expression in the equation to both sides of the distribution. 
We use addition in the equation for the positive side and subtraction for the negative side.

look at the equation again
https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/bb808b792d837685a340ac2fb8dc037860bcc455/confidence_interval.svg

"""

CI_pos = x_mean + (1.96 * (x_std/(n**0.5)))

CI_neg = x_mean - (1.96 * (x_std/(n**0.5)))
