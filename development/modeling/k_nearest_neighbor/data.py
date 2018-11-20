import helper as h


def treatment(path_to='./csv/input/'):
    # Import files
    _train = h.get_data(path_to + 'train.csv')
    _features = h.get_data(path_to + 'features.csv')
    _stores = h.get_data(path_to + 'stores.csv')
    _test = h.get_data(path_to + 'test.csv')

    # Map store type values
    _stores['Type'] = _stores['Type'].map({'A': 0, 'B': 1, 'C': 2})

    # Merge data frames
    _data = h.merge_data(_features, _stores, 'Store')
    _data = h.merge_data(_data, _train, ['Store', 'Date'])

    # Calculate week number and year
    _data['week_number'] = _data.apply(lambda row: h.calculate_week(row['Date']), axis=1)
    _data['year'] = _data.apply(lambda row: h.calculate_year(row['Date']), axis=1)

    _test['week_number'] = _test.apply(lambda row: h.calculate_week(row['Date']), axis=1)
    _test['year'] = _test.apply(lambda row: h.calculate_year(row['Date']), axis=1)

    # Correct IsHoliday values
    _data = _data.drop('IsHoliday_y', axis=1)
    _data = _data.rename(columns={'IsHoliday_x': 'IsHoliday'})
    _data['IsHoliday'] = _data['IsHoliday'].map({False: 0, True: 1})

    # Drop unused columns
    _data = _data.drop('Date', axis=1)
    _data = _data.drop('Markdown1', axis=1)
    _data = _data.drop('Markdown2', axis=1)
    _data = _data.drop('Markdown3', axis=1)
    _data = _data.drop('Markdown4', axis=1)
    _data = _data.drop('Markdown5', axis=1)
    _test = _test.drop('Date', axis=1)

    # Index data by Store, Dept and Date
    _data.set_index(['Store', 'Dept', 'year', 'week_number'])
    _test.set_index(['Store', 'Dept', 'year', 'week_number'])

    # Export data to a csv
    _data.to_csv('./csv/output/regression.data.csv')
    _test.to_csv('./csv/output/test.csv')

def classification(path_to='./csv/output/'):
    # Treat the origin data set
    treatment()

    # Import file
    _continuous = h.get_data(path_to + 'regression.data.csv')

    p25 = _continuous['Weekly_Sales'].describe(percentiles=[.25, .5, .75])['25%']
    p50 = _continuous['Weekly_Sales'].describe(percentiles=[.25, .5, .75])['50%']
    p75 = _continuous['Weekly_Sales'].describe(percentiles=[.25, .5, .75])['75%']

    # Class definition
    def get_class(_value):
        if _value <= p25:
            return 0
        elif p25 < _value <= p50:
            return 1
        elif p50 < _value <= p75:
            return 2
        else:
            return 3

    _continuous['class'] = _continuous.apply(lambda row: get_class(row['Weekly_Sales']), axis=1)

    # Export data to a csv
    _continuous.to_csv('./csv/output/classification.data.csv')

