"""
Scatter plot program

Submitted by: Lucas Lower
"""

#imports
import functions as f


# output program info
print('Scatter Plot Generator   -----   Version 1.0')
print('  ')

# get the file name to process data from
print('Enter the file name to process. Ensure the file is in the same directory as this program.')
file_name = input('File: ')
print('  ')

# open file
file = open(file_name, "r")

# create list of ordered pairs
points = f.create_list(file)

# print lines as table
f.print_table(points)

# get the values for the best-fit equation
best_fit_vals = f.generate_best_fit_line(points)

# build equation's string representation
eq_string = 'y = '+str(best_fit_vals[0])+'x + '+str(best_fit_vals[1])

# print the calculated best-fit equation
print('  ')
print('Linear Regression Equation: ', eq_string)
