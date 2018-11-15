import helper as h


def treatment(path_to='./csv/input/'):
    # Import files
    _train = h.get_data(path_to + 'train.csv')
    _features = h.get_data(path_to + 'features.csv')
    _stores = h.get_data(path_to + 'stores.csv')
    _test = h.get_data(path_to + 'test.csv')

    # Merge data frames
    _data = h.merge_data(_features, _stores, 'Store')
    _data = h.merge_data(_data, _train, ['Store', 'Date'])

    # Calculate week number
    _data['week_number'] = _data.apply(lambda row: h.calculate_week(row['Date']), axis=1)
    _test['week_number'] = _data.apply(lambda row: h.calculate_week(row['Date']), axis=1)

    _data = _data.drop('IsHoliday_y', axis=1)
    _data = _data.rename(columns={'IsHoliday_x': 'IsHoliday'})

    # Index data by Store, Dept and Date
    _data.set_index(['Store', 'Dept', 'Date'])
    _test.set_index(['Store', 'Dept', 'Date'])

    # Export data to a csv
    _data.to_csv('./csv/output/data.csv')
    _test.to_csv('./csv/output/test.csv')
