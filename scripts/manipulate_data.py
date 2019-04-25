import os
import pandas as pd
import matplotlib.pyplot as plt
import ast


def read_data(file_name):
    df = pd.read_csv(os.path.join('../data/tmdb-box-office-prediction', file_name))
    return df

def print_info(df):
    # print(df.columns)
    # print(df.describe())
    # print(df.head())
    print(df.info())

def get_list(row, key):
    list = []
    for item in row:
        list.append(item[key])
    return list

def draw_scatter_plot(df, x_col, y_col, width, height, x_tick_rot=0):
    plt.figure(figsize=(width, height))
    plt.scatter(df[x_col], df[y_col])
    plt.xlabel(x_col.capitalize())
    plt.ylabel(y_col.capitalize())
    plt.xticks(rotation=x_tick_rot)
    plt.title(x_col.capitalize() + ' vs ' + y_col.capitalize())
    plt.show()

def main():
    train_df = read_data('train.csv')
    test_df = read_data('test.csv')

    print_info(train_df)



    # draw_scatter_plot(train_df, x_col='budget', y_col='revenue', width=10, height=6)
    # draw_scatter_plot(train_df, x_col='original_language', y_col='revenue', width=10, height=6)
    # draw_scatter_plot(train_df, x_col='popularity', y_col='revenue', width=10, height=6)
    # draw_scatter_plot(train_df, x_col='belongs_to_collection', y_col='revenue', width=10, height=6) ##NaN problem










    train_df['genres'] = train_df['genres'].apply(lambda row: {} if pd.isnull(row) else ast.literal_eval(row))
    train_df['genres'] = train_df['genres'].apply(lambda row: get_list(row, 'name') if row != {} else [])
    ### train_df['genres'] = train_df['genres'].apply(lambda row: '-'.join(sorted(row)) if row != [] else '')
    # print(train_df['genres'])

    genres_df = train_df.loc[train_df['genres'].str.len()==1][
        ['genres', 'revenue', 'budget', 'popularity', 'runtime']].reset_index(drop=True)
    genres_df['genres'] = genres_df['genres'].apply(lambda row: ' '.join(row) if row != [] else '')

    # draw_scatter_plot(genres_df, x_col='genres', y_col='budget', width=12, height=6, x_tick_rot=90)
    # draw_scatter_plot(genres_df, x_col='genres', y_col='popularity', width=12, height=6, x_tick_rot=90)






    train_df['production_companies'] = train_df['production_companies'].apply(lambda row: {} if pd.isnull(row) else ast.literal_eval(row))
    train_df['production_companies'] = train_df['production_companies'].apply(lambda row: get_list(row, 'name') if row != {} else [])
    print(train_df['production_companies'])

    production_companies_df = train_df.loc[train_df['production_companies'].str.len() == 1][
        ['production_companies', 'revenue', 'budget', 'popularity', 'runtime']].reset_index(drop=True)
    production_companies_df['production_companies'] = production_companies_df['production_companies'].apply(lambda row: ' '.join(row) if row != [] else '')
    print_info(production_companies_df)


    # draw_scatter_plot(production_companies_df, x_col='production_companies', y_col='budget', width=12, height=6, x_tick_rot=90)
    # draw_scatter_plot(production_companies_df, x_col='production_companies', y_col='revenue', width=12, height=6, x_tick_rot=90)
    # draw_scatter_plot(production_companies_df, x_col='production_companies', y_col='popularity', width=12, height=6, x_tick_rot=90)






    train_df['Keywords'] = train_df['Keywords'].apply(lambda row: {} if pd.isnull(row) else ast.literal_eval(row))
    train_df['Keywords'] = train_df['Keywords'].apply(lambda row: get_list(row, 'name') if row != {} else [])
    print(train_df['Keywords'])

    keywords_df = train_df.loc[train_df['Keywords'].str.len() == 1][
        ['Keywords', 'revenue', 'budget', 'popularity', 'runtime']].reset_index(drop=True)
    keywords_df['Keywords'] = keywords_df['Keywords'].apply(lambda row: ' '.join(row) if row != [] else '')
    # print_info(keywords_df)


    # draw_scatter_plot(keywords_df, x_col='Keywords', y_col='budget', width=12, height=6, x_tick_rot=90)
    # draw_scatter_plot(keywords_df, x_col='Keywords', y_col='revenue', width=12, height=6, x_tick_rot=90)
    # draw_scatter_plot(keywords_df, x_col='Keywords', y_col='popularity', width=12, height=6, x_tick_rot=90)







    train_df['cast'] = train_df['cast'].apply(lambda row: {} if pd.isnull(row) else ast.literal_eval(row))
    train_df['cast'] = train_df['cast'].apply(lambda row: get_list(row, 'name') if row != {} else [])
    print(train_df['cast'])

    cast_df = train_df.loc[train_df['cast'].str.len() == 1][
        ['cast', 'revenue', 'budget', 'popularity', 'runtime']].reset_index(drop=True)
    cast_df['cast'] = cast_df['cast'].apply(lambda row: ' '.join(row) if row != [] else '')
    # print_info(cast_df)

    # draw_scatter_plot(cast_df, x_col='cast', y_col='budget', width=12, height=6, x_tick_rot=90)
    # draw_scatter_plot(cast_df, x_col='cast', y_col='revenue', width=12, height=6, x_tick_rot=90)
    # draw_scatter_plot(cast_df, x_col='cast', y_col='popularity', width=12, height=6, x_tick_rot=90)









    train_df['crew'] = train_df['crew'].apply(lambda row: {} if pd.isnull(row) else ast.literal_eval(row))
    train_df['crew'] = train_df['crew'].apply(lambda row: get_list(row, 'name') if row != {} else [])
    print(train_df['crew'])

    crew_df = train_df.loc[train_df['crew'].str.len() == 1][
        ['crew', 'revenue', 'budget', 'popularity', 'runtime']].reset_index(drop=True)
    crew_df['crew'] = crew_df['crew'].apply(lambda row: ' '.join(row) if row != [] else '')
    # print_info(cast_df)

    draw_scatter_plot(crew_df, x_col='crew', y_col='budget', width=12, height=6, x_tick_rot=90)
    draw_scatter_plot(crew_df, x_col='crew', y_col='revenue', width=12, height=6, x_tick_rot=90)
    draw_scatter_plot(crew_df, x_col='crew', y_col='popularity', width=12, height=6, x_tick_rot=90)








main()


