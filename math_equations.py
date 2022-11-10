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
Xi  =  the value of the one observation ( X sub i )
x̄   =  the mean value of all observations ( x bar)
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
Here implement the plus/minus expression in the equation to both sides of the distribution. 
We use addition in the equation for the positive side and subtraction for the negative side.

look at the equation again
https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/bb808b792d837685a340ac2fb8dc037860bcc455/confidence_interval.svg

"""

CI_pos = x_mean + (1.96 * (x_std/(n**0.5)))

CI_neg = x_mean - (1.96 * (x_std/(n**0.5)))

########################################################################################################################
########################################################################################################################
# Simple Linear Regression
########################################################################################################################
########################################################################################################################
"""
Simple linear regression is a method used to predict the dependent variable with the help of the independent variable 
when there is a linear relationship between a single independent variable and the dependent variable.

https://github.com/bunyaminergen/how_to_code_math_equations/blob/main/simple-linear-regression1.jpg?raw=true

Y   = dependent variable

β0  = intercept

β1  = slope

X   = independent variable

ϵ   = random error 

Of course, since want find the values to be predicted, should the equation as follows.
The only difference is, as you know, that hats which is mean predicted value and " i " letter means each value. 
For more information, you can refer to the projection matrix. 

https://github.com/bunyaminergen/how_to_code_math_equations/blob/main/simple-linear-regression2.jpg?raw=true

https://github.com/bunyaminergen/how_to_code_math_equations/blob/main/simple-linear-regression3.jpg?raw=true

"""

"""
Create a dataset with a linear relation.
we can implement this from the datasets class in the sklearn module.
"""

from sklearn import datasets

x , y  = datasets.make_regression(random_state = 17)

"""
now we have a data set of independent variables and dependent variable.
Since we will implement simple linear regression, let's take one of the independent variables and assign it as x.
"""

x = x[0]

"""
Dive into solving the equation!
we have x and y. And we know that they are in a linear relation.
then let's find other unknowns
first β1 i.e. slope

https://github.com/bunyaminergen/how_to_code_math_equations/blob/main/slope.png?raw=true

Let's explain the above unknowns.

r  = Pearson correlation coefficient

Sy = standard deviation of y

Sx = standard deviation of x

Let's start with the simple first and find the standard deviations of x and y.
Since I explained how to find the standard deviation above, I'm going directly to the solution.
"""

y_mean = sum(y)/len(y)

x_mean = sum(x)/len(x)

Sy = (sum((y_i - y_mean)**2 for y_i in y) / (len(y) - 1))**0.5

Sx = (sum((x_i - x_mean)**2 for x_i in x) / (len(x) - 1))**0.5

"""
Now that we have found the standard deviations of x and y, we can move on to r, i.e. Pearson correlation coefficient.

# image of equation

r	=	correlation coefficient
xi 	=	values of the x-variable in a sample ( x sub i )
x̄	=	mean of the values of the x-variable
yi	=	values of the y-variable in a sample ( y sub i )
ȳ	=	mean of the values of the y-variable

Let's explain equation. 
There is a vector operation the numerator of this fraction. 
The first Σ (upper case sigma) sign means summation symbol, that is, we will summation the results. 
Let's take the first parenthesis for the numerator, subtract the mean of x from each x value, 
Then move on to the next parenthesis, subtract the mean of y from each y value. 
Then we will have two new arrays ,
Then multiply this two array , 
And then summation them all ,
And we will have found the numerator of the fraction of this equation. 
Let's implement the code for the numerator part first to avoid confusion.
"""

import numpy as np

r_up = sum(np.array([(x_i - x_mean) for x_i in x]) * np.array([(y_i - y_mean) for y_i in y]))

"""
I am adding the stages of the above code to the below so that it can be followed easily.

             [(x_i - x_mean) for x_i in x]  *          [(y_i - y_mean) for y_i in y]
    np.array([(x_i - x_mean) for x_i in x]) * np.array([(y_i - y_mean) for y_i in y])
sum(np.array([(x_i - x_mean) for x_i in x]) * np.array([(y_i - y_mean) for y_i in y]))
"""
"""
Now let's do the denominator part of the equation:
for the denominator, we'll subtract the mean of x from each x value and square the resulting values and summation them all  .
implement the same for y.
multiply two array each other.
Then take the square root of the result.
"""

r_down = (sum([(x_i - x_mean) ** 2 for x_i in x]) * sum([(y_i - y_mean) ** 2 for y_i in y])) ** 0.5

"""
Now that have the numerator and denominator part of the equation, solve the equation.
"""

r = r_up / r_down

"""
If you want, you can code directly without creating a variable as follows.
Personally, I like the following process more.
I don't like creating variables for even the slightest thing.

r = sum(np.array([(x_i - x_mean) for x_i in x]) * np.array([(y_i - y_mean) for y_i in y])) / (sum([(x_i - x_mean)**2 for x_i in x]) * sum([(y_i - y_mean)**2 for y_i in y]))**0.5

"""

"""
# Yes, now that we've found all the variables, let's find our main operation, β1, i.e. the slope.
# check equation again.

https://github.com/bunyaminergen/how_to_code_math_equations/blob/main/slope.png?raw=true

"""

B1 = r * (Sy/Sx)

"""
Now solve for β0

https://github.com/bunyaminergen/how_to_code_math_equations/blob/main/Intercept.png?raw=true

"""

B0 = y_mean - (B1 * x_mean)



"""
Now let's find R-Squared, i.e. Coefficient of determination.

In statistics, the coefficient of determination, denoted R2 or r2 and pronounced "R squared", 
is the proportion of the variation in the dependent variable that is predictable from the independent variable(s).

It is a statistic used in the context of statistical models whose main purpose is 
either the prediction of future outcomes or the testing of hypotheses, 
on the basis of other related information. It provides a measure of how well observed outcomes are 
replicated by the model, based on the proportion of total variation of outcomes explained by the model.

https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/69baec51c4640abe32eb41b86baf1d956db3daf6/coefficient_of_determination_r2.svg

R2	=	coefficient of determination
RSS	=	sum of squares of residuals
TSS	=	total sum of squares

Let's go step by step and find the RSS first.

https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/6823cdcef168da3c42e7bc0f59682ac3cc7c39a6/residual_sum_of_squares.svg

RSS	   =  residual sum of squares
y_i	   =  each value of the dependent variable
f(x_i) =  predicted values of the dependent variables
"""

# find the predicted values first.
y_pred = [B0 + (B1 * x_i) for x_i in x]

RSS = sum((np.array(y) - np.array(y_pred)) ** 2)

"""
Now TSS

https://raw.githubusercontent.com/bunyaminergen/how_to_code_math_equations/d0377c83d7390137de9e70af9ca3ab152c6126fc/total_sum_of_squares.svg

TSS	=	total sum of squares
n	=	number of observations
y_i	=	each value in a sample   ( y sub i )
ȳ	=	mean value of a sample   ( y bar )
"""

TSS = sum((y_i - y_mean)**2 for y_i in y)

"""
Now that all the unknowns have been revealed,
find the R-Squared, i.e. Coefficient of determination.
"""

R2 = 1 - RSS/TSS

"""
Let's also find the adjusted R2 value to get a more accurate result.

https://github.com/bunyaminergen/how_to_code_math_equations/blob/main/Adjusted_R_squared.png?raw=true

R2 = Sample R-squared

n  = sample size

p = number of independent variable


Since we are solving the simple linear regression equation we naturally have one independent variable so p = 1.

"""

n = len(x)

p = 1

R2_adf = 1 - ((1 - R2) * (n - 1)) / (n - p - 1)


"""
As seen, actually need two things to code an equation.
First, understand the equation; meanings of unknowns and how to solve them.
Second, encode the equation according to the python syntax.

Let's stay up until morning and code.
Then we'll have a good sleep and maybe solve the quantum equations in our dreams. :)

Please note that some equations are solved in more than one way, just pick one and go for it.

Thank you very much.
"""

########################################################################################################################
########################################################################################################################
# Resources
########################################################################################################################
########################################################################################################################
"""
https://en.wikibooks.org/wiki/Python_Programming/Basic_Math#Order_of_Operations

https://en.wikibooks.org/wiki/Python_Programming/Math

https://en.wikipedia.org/wiki/Equation

https://en.wikipedia.org/wiki/Standard_deviation

https://en.wikipedia.org/wiki/Algebra

https://en.wikipedia.org/wiki/Linear_algebra

https://en.wikipedia.org/wiki/Algorithm

https://tr.wikipedia.org/wiki/G%C3%BCven_aral%C4%B1%C4%9F%C4%B1

https://en.wikipedia.org/wiki/Confidence_interval

https://www.hec.ca/en/cams/help/topics/The_summation_symbol.pdf

https://www.google.com/search?q=pearson+correlation&oq=pears&aqs=chrome.1.69i57j0i67l4j46i67i199i465i512j46i67i199i465j0i67j0i512l2.2288j0j7&sourceid=chrome&ie=UTF-8#wptab=si:AC1wQDDneak2MGu90lY3o217UabRapWzjDthgzyFzlAOtapK_XelKDQ0sK5jawlGt2w_oar5FFDeT_JvBz88xxP8D6VOybUCcyNBsfUDoiTAnNHmNHFEbadZC4MFIHjJ0T6vIQyA8LS_x7MMoZsHh8JafeACI40Yew%3D%3D

"""