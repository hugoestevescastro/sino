from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import datetime
import numpy as np
import math


def get_data(path):
    """Imports *.csv using pandas library.
    Args:
        path: The path to the file.

    Returns:
        Data frame originated from *.csv.

    """
    return pd.read_csv(path)


def merge_data(df1, df2, merge_by):
    """Merge two data frames by given order.

    Args:
        df1: First data frame.
        df2: Second data frame.
        merge_by: String or array of Strings with the columns to merge by.

    Returns:
        Merged data frame.

    """
    return pd.merge(df1, df2, on=merge_by)


def calculate_week(dt_str):
    """Calculates the week number based on the given date string.

    Args:
        dt_str: Date in a string. YYYY:MM:DD.

    Returns:
        The week number of the given date.

    """
    year = int(dt_str[:4])
    month = int(dt_str[5:-3])
    day = int(dt_str[8:])
    return datetime.date(year, month, day).isocalendar()[1]

def calculate_year(dt_str):
    """Calculates the date year.

    Args:
        dt_str: Date in a string. YYYY:MM:DD.

    Returns:
        The year of the given date

    """
    return dt_str[:4]


def draw_3d_scatter_plot(df, x_lbl, y_lbl, z_lbl, color='r', marker='.'):
    """Draws a 3D scatter plot.

    Args:
        df: Panda data frame to extract data from.
        x_lbl: X axis label.
        y_lbl: Y axis label.
        z_lbl: Z axis label.
        color: Marker color (DEFAULT='red').
        marker: Marker type (DEFAULT='.').

    """
    warnings.simplefilter(action='ignore', category=FutureWarning)  # To ignore Future Warning bug
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.asarray(df[x_lbl].tolist())
    y = np.asarray(df[y_lbl].tolist())
    z = np.asarray(df[z_lbl].tolist())

    ax.scatter(x, y, z, c=color, marker=marker)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)

    plt.show()


def euclidean_distance(row, distance_columns, selected_week):
    """
    A simple euclidean distance function
    """
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_week[k]) ** 2
    return math.sqrt(inner_value)


def get_points(df, x, y):
    """Returns all the points based on the given info.

    Args:
        df: Data frame
        x: Array containing all the 3 labels that compose de x axis
        y: Y axis to obtain from data frame.

    Returns:
        Array containing all points.

    """
    points = []
    for index, row in df.iterrows():
        x2 = int(str(row[x[0]])+str(row[x[1]])+str(row[x[2]]))
        if y is None:
            point = [x2, 0]
            points.append(point)
        else:
            point = [x2, row[y]]
            points.append(point)
    return points
