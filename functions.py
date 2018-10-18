"""
Homework 4 functions module.

Submitted by: Lucas Lower
"""

import turtle


def create_list(file):
    """
    creates a list of tuples from a file containing x,y pairs of data
    :param file: the file object to pull data from
    :return: a list of tuples
    """
    points = []
    for line in file:
        # skip comments and empty lines
        if line[0] != '#' and line.strip():
            # split at comma if csv, space otherwise (remove last char (newline))
            if ',' in line:
                line_vals = line[:-1].split(',')
            else:
                line_vals = line[:-1].split(' ')
            # remove empty elements in case more than one space was used as separator
            line_vals = list(filter(None, line_vals))
            # insert into list as tuple
            # see what type (float or int) to convert to for each value in pair
            if '.' in line_vals[0]:
                x_val = float(line_vals[0])
            else:
                x_val = int(line_vals[0])
            if '.' in line_vals[1]:
                y_val = float(line_vals[1])
            else:
                y_val = int(line_vals[1])
            # append tuple
            points.append((x_val,y_val))
    return points


def get_values(list, index):
    """
    gets a list of values from the given tuple index from a list of tuples
    :param list: a list of tuples
    :param index: the index (1 or 0) to get values from
    :return: a list of values
    """
    return_list = []
    for item in list:
        return_list.append(item[index])
    return return_list


def print_table(points):
    """
    prints a well-formatted table given a list of tuples
    :param points: list of tuples
    :return: None (prints a table)
    """
    print('Table of values:')
    print('  ')
    # get max length in x and y (+1 for padding)
    # lambda function as key so we can recast float or int as str to we can get len
    max_x = max(get_values(points,0), key=lambda item:len(str(item)))
    max_y = max(get_values(points,1), key=lambda item:len(str(item)))
    # cast max's as string so len() works
    x_len = len(str(max_x)) + 1
    y_len = len(str(max_y)) + 1
    # build format string
    format_str = '%' + str(x_len) + 's%2s%' + str(y_len) + 's'
    # print headers
    print(format_str % ('x', '|', 'y'))
    # print horizontal line
    print(format_str % ('-' * x_len, '-|', '-' * (y_len + 1)))
    # print points
    for pair in points:
        print(format_str % (pair[0], '|', pair[1]))


def generate_best_fit_line(points):
    """
    generates the line of best fit for the given list of coordinates
    :param points: the list of tuples to process
    :return: a list containing the slope, intercept
    """

    # get number of points
    num_points = len(points)

    # grab x values
    x_vals = get_values(points,0)
    # grab y values
    y_vals = get_values(points,1)

    # generate mean x and mean y
    x_mean = sum(x_vals) / len(x_vals)
    y_mean = sum(y_vals) / len(y_vals)

    # calculate slope (m)
    # numerator of slope equation
    point_product_sum = 0
    for point in points:
        point_product_sum += point[0] * point[1]
    numerator = point_product_sum - (num_points*x_mean*y_mean)
    # denominator of slope equation
    x_square_sum = 0
    for x in x_vals:
        x_square_sum += x*x
    denominator = x_square_sum - (num_points*x_mean*x_mean)
    # calculate the slope
    slope = numerator/denominator

    # calculate value of intercept (b)
    intercept = y_mean - (slope*x_mean)

    # return list of values
    return [slope, intercept]


def draw_regression_plot(points):
    """
    draws a scatterplot with regression line for given list of tuples
    :param points: list of tuples to process
    :return: None (draws a plot with turtle)
    """
    # init turtle and other things
    t = turtle.Turtle()
    w = turtle.Screen()
    w.tracer(0)
    w.title('Linear Regression Plot')

    # get x and y values
    x_vals = get_values(points,0)
    y_vals = get_values(points,1)

    # get min and maxes
    min_x = min(x_vals)
    max_x = max(x_vals)
    min_y = min(y_vals)
    max_y = max(y_vals)

    # set turtle coordinates from those
    # check min x
    if min_x >= 0:
        w_minx = 0
    else:
        w_minx = min_x-10
    # check min y
    if min_y >= 0:
        w_miny = 0
    else:
        w_miny = min_y-10
    # check max x
    if max_x <= 0:
        w_maxx = 0
    else:
        w_maxx = max_x+10
    # check max y
    if max_y <= 0:
        w_maxy = 0
    else:
        w_maxy = max_y+10
    w.setworldcoordinates(w_minx,w_miny,w_maxx,w_maxy)

    # draw axis lines
    t.pensize(2)
    t.pencolor("black")
    # x
    t.up()
    t.goto(w_minx,0)
    t.down()
    t.goto(w_maxx,0)
    # y
    t.up()
    t.goto(0,w_miny)
    t.down()
    t.goto(0,w_maxy)

    # plot points
    t.up()
    for point in points:
        t.goto(point[0],point[1])
        t.dot(5,"blue")

    # plot regression line
    fit_line_vals = generate_best_fit_line(points)
    left_y = (fit_line_vals[0]*min_x) + fit_line_vals[1]
    left_point = (min_x,left_y)
    right_y = (fit_line_vals[0] * max_x) + fit_line_vals[1]
    right_point = (max_x, right_y)
    t.up()
    t.goto(left_point)
    t.pensize(2)
    t.pencolor("red")
    t.down()
    t.goto(right_point)

    # hide turtle, update, and don't exit
    t.hideturtle()
    w.update()
    w.exitonclick()