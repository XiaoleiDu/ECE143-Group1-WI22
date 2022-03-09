import pandas as pd

def recommender_surprise(algo, full_data_path, data_recommender, target_games, board_game_categories: dict,
                         number_recommendations=10):
    """
    This function returns top rated games by people who game poor/average rating to target games.

    :param algo: The Surprise algo returned by build_model_surprise from recommender_model.py .
    :param full_data_path: Clean CSV, containing all game features.
    :param data_recommender: Pandas DF of df_reviews
    :param target_games: The games the recommender is targeting.
    :param board_game_categories: The target game categories someone is looking for.
    :param number_recommendations: The number of games that are recommended to extract features.
    :return: The top rated games recommended by the Model. We will extract the features in the recommender_stats.
    """

    assert isinstance(data_recommender, pd.DataFrame)
    assert isinstance(target_games, list)
    assert isinstance(board_game_categories, dict)
    assert isinstance(number_recommendations, int) and number_recommendations > 0

    for game_id in target_games:
        if len([data_recommender['ID'] == game_id]) == 0:
            assert False, f"{game_id} from target_games list not in Recommender System Data."

    # Find Reviews of target_games
    target_games_reviews = data_recommender.query("ID in @target_games")

    # Get Reviewers who gave low/average rating
    target_games_reviews = target_games_reviews.sort_values(by="rating", ascending=True)

    # target_games_reviews.to_csv("target_games_reviews.csv", index=False)

    # Get First 10 Reviewers
    if target_games_reviews.shape[0] > 10:
        target_games_reviews = target_games_reviews[:10]

    valid_categories = ['Cat:Thematic', 'Cat:Strategy', 'Cat:War', 'Cat:Family', 'Cat:CGS',
                        'Cat:Abstract', 'Cat:Party', 'Cat:Childrens']

    # Assert if Incorrect Categories Found
    # assert (set(board_game_categories) - set(valid_categories)) != 0

    valid_targets = {k: v for k, v in board_game_categories.items() if v not in [None, False]}

    # Find games in request categories
    df_full_data = pd.read_csv(full_data_path, index_col=0)
    all_selected_categories = pd.DataFrame(columns=df_full_data.columns)
    for cat in valid_targets.keys():
        all_selected_categories = pd.concat([all_selected_categories, df_full_data[df_full_data[cat] == 1]],
                                            ignore_index=True)

    # all_selected_categories.to_csv('all_selected_categories.csv', index=False)

    list_of_rating = []

    # Run Model on those reviewers and found games from all_selected_categories.
    for user in target_games_reviews['user']:
        for game in all_selected_categories['BGGId']:
            y = algo.predict(uid=user, iid=game)
            list_of_rating.append((user, y[1], y[3]))

    list_of_rating = pd.DataFrame(list_of_rating, columns=["user", "ID", "Rating"])
    # list_of_rating.to_csv('list_of_rating.csv')

    list_of_rating = list_of_rating.groupby(list_of_rating['ID'], as_index=False).aggregate({'Rating': 'mean'})
    list_of_rating = list_of_rating.sort_values(by='Rating', ascending=False)

    return list_of_rating.iloc[:number_recommendations]





