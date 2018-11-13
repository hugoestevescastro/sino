import helper
import math
import numpy as np

# Get the training data set
train = helper.get_data('./csv/output/data.csv')
test = helper.get_data('./csv/output/test.csv')

# From the data set makes the training set
training_set = helper.get_points(train, ['week_number', 'Store', 'Dept'], 'Weekly_Sales')
testing_set = helper.get_points(test, ['week_number', 'Store', 'Dept'], None)

# Calculate the number of neighbors
k = int(math.sqrt(len(training_set)))

# Checks the k nearest for each testing set point
pairs = []
for test_pt in testing_set:
    pair = [test_pt, []]
    _distances = []
    for train_pt in training_set:
        _distances.append(helper.calculate_distance_between_points(test_pt, train_pt))

    distances = np.array(_distances)
    k_smallest = np.argpartition(distances, k)

    for index in k_smallest:
        if index >= k :
            break
        pair[1].append(training_set[index])
    pairs.append(pair)

print(pairs)
