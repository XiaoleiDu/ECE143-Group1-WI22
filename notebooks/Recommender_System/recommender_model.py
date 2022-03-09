import pandas as pd

from surprise.model_selection import train_test_split
from surprise import Dataset, Reader
from surprise import SVDpp
from surprise.model_selection import cross_validate
from surprise import accuracy


def build_model_surprise(df_reviews, test_size_ratio=.1, use_cross_validate=False):
    """
    The function builds the Surprise SVDpp model using reviews dataframe.

    :param df_reviews: This dataframe was returned by data_processing_surprise from recommender_data_processing.py .
    :param test_size_ratio: The ratio of data given to become the test set. The default is .1 .
    :param use_cross_validate: Enable CV using Surprise Framework. The default is False.
    :return: Surprise Model, dict contain RMSE, MSE, MAE, and FCP
    """

    assert isinstance(df_reviews, pd.DataFrame)
    assert isinstance(test_size_ratio, float) and .4 >= test_size_ratio >= .01
    assert isinstance(use_cross_validate, bool)

    reader = Reader(line_format='user item rating', sep=',', rating_scale=(0, 10))
    data = Dataset.load_from_df(df_reviews, reader)
    trainset, testset = train_test_split(data, test_size=test_size_ratio)

    # This algo is extension of SVD, by taking in implicit reviews.
    algo = SVDpp()

    if use_cross_validate:
        cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    else:
        algo.fit(trainset)

    predictions = algo.test(testset)

    predictions_dict = {'RMSE': accuracy.rmse(predictions), 'MSE': accuracy.mse(predictions),
                        'MAE': accuracy.mae(predictions), 'FCP': accuracy.fcp(predictions)}

    return algo, predictions_dict



