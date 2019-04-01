import pandas as pd
import ast

def get_list(row, key):
    list = []
    for item in row:
        list.append(item[key])
    return list



def main():
    train_df = pd.read_csv('../data/tmdb-box-office-prediction/train.csv')
    test_df = pd.read_csv('../data/tmdb-box-office-prediction/test.csv')

    # print(train_df.columns)
    # print(train_df.describe())
    # print(train_df.head())

    # print(train_df.info())
    train_df['genres'] = train_df['genres'].apply(lambda row: {} if pd.isnull(row) else ast.literal_eval(row))
    train_df['genres'] = train_df['genres'].apply(lambda row: get_list(row, 'name') if row != {} else [])
    # print(train_df.info())
    print(train_df['genres'])


main()


