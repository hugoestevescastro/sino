import helper

# Import files
PATH_TO = './csv/input/'
train = helper.get_data(PATH_TO + 'train.csv')
features = helper.get_data(PATH_TO + 'features.csv')
stores = helper.get_data(PATH_TO + 'stores.csv')
test = helper.get_data(PATH_TO + 'test.csv')

# Merge data frames
data = helper.merge_data(features, stores, 'Store')
data = helper.merge_data(data, train, ['Store', 'Date'])

# Calculate week number
data['week_number'] = data.apply(lambda row: helper.calculate_week(row['Date']), axis=1)
test['week_number'] = data.apply(lambda row: helper.calculate_week(row['Date']), axis=1)

# Index data by Store, Dept and Date
print("=> INDEXING DATA. PLEASE WAIT.\n")
data.set_index(['Store', 'Dept', 'Date'])
test.set_index(['Store', 'Dept', 'Date'])

# Export data to a csv
data.to_csv('./csv/output/data.csv')
test.to_csv('./csv/output/test.csv')
print("=> SUCCESS!! FIND THE DATA AT './csv/output/*.csv'\n")
