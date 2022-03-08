import pandas as pd

def recommender_stats_surprise(full_data_path, df_games):
    """

    :param full_data_path: Cleaned CSV file path.
    :param df_games: The games recommender by Surprise, to get stats on various features.
    :return: All the Features of the df_games.
    """
    assert isinstance(full_data_path, str)
    assert isinstance(df_games, pd.DataFrame)

    df = pd.read_csv(full_data_path)

    return_df = pd.DataFrame(columns=df.columns)
    for game in df_games['ID']:
        return_df = pd.concat([return_df, df[df['BGGId'] == game]], ignore_index=True)

    return_df = return_df.loc[:, ~(return_df.columns.str.contains('^Unnamed') | return_df.columns.str.contains('^Cat'))]

    return return_df
