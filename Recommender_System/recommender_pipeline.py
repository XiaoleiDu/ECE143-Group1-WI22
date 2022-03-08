import pandas as pd

from recommender_data_processing import data_processing_surprise
from recommender_model import build_model_surprise
from recommender_generation import recommender_surprise
from recommender_stats import recommender_stats_surprise

from surprise import dump

"""
Pipeline for Recommender System
"""

review_csv_path = r"./user_ratings.csv"
# df_reviews = data_processing_surprise(review_csv_path, number_of_reviews=2000000, shuffle=True)

# Load Algo
_, algo = dump.load(r"./model_2000000_kaggle_random.pkl")

# Save df_reviews
# df_reviews.to_csv(r"./df_reviews.csv")

# Load df_reviews
df_reviews = pd.read_csv(r"./df_reviews.csv")

#algo, predictions_dict = build_model_surprise(df_reviews)
#print(predictions_dict)

# Save Algo
#dump.dump(r"model_2000000_kaggle_random.pkl", algo=algo)

board_game_cat = {
    "Cat:Thematic": False,
    "Cat:Strategy": True,
    "Cat:War": False,
    "Cat:Family": False,
    "Cat:CGS": False,
    "Cat:Abstract": False,
    "Cat:Party": False,
    "Cat:Childrens": False
}

df_games = recommender_surprise(algo, r"./games_cleaned.csv",
                                df_reviews, target_games=[167791],
                                board_game_categories=board_game_cat)

clean_csv_path = r"./games_cleaned.csv"

df = recommender_stats_surprise(clean_csv_path, df_games)

df.to_csv(r"./final_output.csv")
