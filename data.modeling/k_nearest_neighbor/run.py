import helper

df = helper.get_data('./csv/output/test.csv')

print(df.isnull().sum())
