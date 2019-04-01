import pandas as pd

train_df = pd.read_csv('../data/tmdb-box-office-prediction/train.csv')
test_df = pd.read_csv('../data/tmdb-box-office-prediction/test.csv')

print("train dataset size:", train_df.shape)
print("test dataset size: ", test_df.shape)



print(train_df.columns)
print(train_df.describe())
# print(train_df.head())

