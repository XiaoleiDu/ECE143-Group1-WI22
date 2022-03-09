import pandas as pd

def recommender_stats_surprise(full_data_path, mechanics_data_path, df_games):
    """

    :param full_data_path: Cleaned CSV file path (games).
    :param df_games: The games recommended by Surprise Model, to get extract features of interest.
    :return: Selected features from the df_games, pd.DataFrame return
    """
    assert isinstance(full_data_path, str)
    assert isinstance(mechanics_data_path, str)
    assert isinstance(df_games, pd.DataFrame)

    # Read clean csv game path
    df_csv_clean = pd.read_csv(full_data_path)

    # Read mechanics
    df_csv_mechanics = pd.read_csv(mechanics_data_path)

    return_df = pd.DataFrame(columns=df_csv_clean.columns)
    for game in df_games['ID']:
        return_df = pd.concat([return_df, df_csv_clean[df_csv_clean['BGGId'] == game]], ignore_index=True)

    return_df = return_df.loc[:, ~(return_df.columns.str.contains('^Unnamed') | return_df.columns.str.contains('^Cat'))]

    return return_df[['GameWeight', 'MinPlayers', 'MaxPlayers', 'ComAgeRec', 'MfgPlaytime']]
