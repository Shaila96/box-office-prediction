import pandas as pd
import matplotlib.pyplot as plt
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

    print(train_df.info())

    plt.figure(figsize=(10, 6))
    plt.scatter(train_df['budget'], train_df['revenue'])
    plt.xlabel('Budget')
    plt.ylabel('Revenue')
    plt.title('Budget vs Revenue')
    # plt.show()


    train_df['genres'] = train_df['genres'].apply(lambda row: {} if pd.isnull(row) else ast.literal_eval(row))
    train_df['genres'] = train_df['genres'].apply(lambda row: get_list(row, 'name') if row != {} else [])
    # print(train_df.info())
    print(train_df['genres'])

    genres_df = train_df.loc[train_df['genres'].str.len() == 1][
        ['genres', 'revenue', 'budget', 'popularity', 'runtime']].reset_index(drop=True)
    genres_df['genres'] = genres_df['genres'].apply(lambda row: ' '.join(row) if row != [] else '')
    genres_df['genres'] = genres_df['genres'].apply(str)

    plt.figure(figsize=(15, 10))
    # plt.subplot(2, 2, 1)
    plt.scatter(genres_df['genres'], genres_df['revenue'])
    plt.xticks(rotation=90)
    plt.xlabel('Genres')
    plt.ylabel('Revenue')
    # plt.scatter(genres_df['genres'], genres_df['budget'])
    # plt.scatter(genres_df['genres'], genres_df['popularity'])
    plt.show()


main()


