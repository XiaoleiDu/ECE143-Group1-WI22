import pandas as pd

def data_processing_surprise(dataset_path: str, number_of_reviews=1000000, shuffle=False):
    """

    :param dataset_path: The path to reviews csv, needs to contain these exact columns: ["user" , "ID", "rating"].
    :param number_of_reviews: The number of reviews you want to train for Recommender. Default is 1,000,000.
    :param shuffle: If true, the reviews dataset gets shuffled. Default is False.
    :return: pandas DataFrame containing only ["user", "ID", "rating"] columns.
    """

    assert isinstance(dataset_path, str)
    assert isinstance(number_of_reviews, int) and number_of_reviews >= 10000
    assert isinstance(shuffle, bool)

    # Read Dataset
    df_reviews = pd.read_csv(dataset_path, index_col=0)
    df_reviews = df_reviews.iloc[:number_of_reviews]

    """
    If data is from this Kaggle (https://www.kaggle.com/threnjen/board-games-database-from-boardgamegeek?select
    =user_ratings.csv), update columns to "user", "ID", "rating". 
    """
    if {"Rating", "Username"}.issubset(df_reviews.columns):
        df_reviews = df_reviews.rename_axis('BGGId').reset_index()
        df_reviews = df_reviews.rename(columns={'BGGId': 'ID', 'Rating': 'rating', 'Username':'user'})

    # Check if Columns ["user" , "ID", "rating"] exist
    assert {"user", "ID", "rating"}.issubset(df_reviews.columns)

    # Shuffle Dataset if True
    if shuffle:
        df_reviews = df_reviews.sample(frac=1).reset_index(drop=True)

    # Return user id, item id and rating which are required for Surprise Framework
    return df_reviews[["user", "ID", "rating"]]
