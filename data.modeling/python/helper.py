import pandas as pd
import datetime


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
