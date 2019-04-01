import pandas as pd
import json
import ast

def main():
    train_df = pd.read_csv('../data/tmdb-box-office-prediction/train.csv')
    test_df = pd.read_csv('../data/tmdb-box-office-prediction/test.csv')

    # print(train_df.columns)
    # print(train_df.describe())
    # print(train_df.head())

    # print(train_df.info())
    train_df['genres'] = train_df['genres'].apply(lambda x: {} if pd.isnull(x) else ast.literal_eval(x))
    train_df['genres'] = train_df['genres'].apply(lambda x: [i['name'] for i in x] if x != {} else []).values
    # print(train_df.info())
    print(train_df['genres'])

main()