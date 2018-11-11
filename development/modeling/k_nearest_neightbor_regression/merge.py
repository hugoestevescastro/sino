import pandas as pd

# Set data sets folder
PATH_TO = './csv/input/'

# Load data sets into data frames
print("=> READING DATA SETS. PLEASE WAIT...\n")
train = pd.read_csv(PATH_TO + 'train.csv')
stores = pd.read_csv(PATH_TO + 'stores.csv')
features = pd.read_csv(PATH_TO + 'features.csv')
print("=> FINISHED READING DATA SETS.\n")

# Merge Features and Stores data frames
print("=> MERGING STORES AND FEATURES DATA FRAMES. PLEASE WAIT...\n")
merge_stores_features = pd.merge(features, stores, on='Store')
print("=> FINISHED MERGING DATA FRAMES(1).\n")

# Merge the acquired data frame with train data frame
print("=> MERGING TRAIN INTO PREVIOUSLY ACQUIRED DATA FRAME. PLEASE WAIT...\n")
data = pd.merge(merge_stores_features, train, on=['Store', 'Date'])
print("=> FINISHED MERGING DATA FRAMES(2).\n")


# Organize data by Store, Dept and Date
print("=> INDEXING FINAL DATA FRAME. PLEASE WAIT...\n")
data.set_index(['Store', 'Dept', 'Date'])

# Export data to a csv
data.to_csv('./csv/output/data.csv')
print("=> SUCCESS!! FIND THE DATA AT './csv/output/data.csv'\n")
