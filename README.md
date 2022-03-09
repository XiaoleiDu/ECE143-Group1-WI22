# ECE143-Group1-WI22

## Summary
Board Games are slowly becoming an integral part of the life. Using a collection of different features about the most popular games, we aim to extract the recipe for the most popular board game. We use the Board Game Geek database as the main data bank and analyse different hypotheses and conditions to recommend the best game.

## Team
- Kai Chuen Tan
- Manas Bedmutha
- Siddhant Saoji
- Joshua Smith
- Ali Zaidi
- Xiaolei Du



## Installation

Requires python 3.7+

Please do have Microsoft Visual C++ 14.0 or greater to work with scikit-surprise: https://www.youtube.com/watch?v=rcI1_e38BWs

Major third-party modules:
- pandas 1.4.1
- plotly 5.6.0
- seaborn 0.11.2
- scikit-surprise 1.1.1

Clone the repository using
```
git clone https://github.com/XiaoleiDu/ECE143-Group1-WI22.git
```

Install dependencies
```
pip install -r requirements.txt
```

Please download Reviews CSV into notebooks/Recommender_System folder.

https://www.kaggle.com/threnjen/board-games-database-from-boardgamegeek?select=user_ratings.csv

## Usage

All the data used for visualisation is stored in the [data](https://github.com/XiaoleiDu/ECE143-Group1-WI22/tree/main/data) folder, visualisation can be seen in the [notebook](https://github.com/XiaoleiDu/ECE143-Group1-WI22/blob/main/notebooks/combined_notebook.ipynb).


## Data Selection & Collection
The goal of the analysis is to find the best parameters to make a game. In this sense, BoardGameGeek is a large repository of games and their metrics. BoardGameGeek is a community platform for board game enthusiasts to discuss and explore new board games, interact about their progress and rate their favorites. The database also has numerous details about each game. The categories, themes, mechanics, popularity metrics among others can help us gain deep insights into the community of board game players.

We found many people had tried to collect different aspects and details about board games. But the BGG database seemed to be the most complete. We found a very recent snapshot of this data on Kaggle and chose to use that for our analysis. The data was scraped and collected by a user on Kaggle. More details about the dataset can be found [here](https://www.kaggle.com/threnjen/board-games-database-from-boardgamegeek?select=bgg_data_documentation.txt).

### Data Cleaning
The datset was analyzed and checked for relevant features. While preprocessing the data by filling missing and NaN values.
The  available csv files are

#### Games
The file contains the following relevant information,
BoardGameGeek game ID, the name of the game,  Year the game was published, Average user rating for the game, Bayes weighted average rating and its standard deviation, the Minimum number of players, Maximum number of players, Community's recommended minimum age, Number of users who own this game, Number of users who want this game, Number of users who wishlisted this game, Manufacturer stated playtime, Community minimum play time, Community maximum playtime, Manufacturer age recommendation, Number of user ratings, Number of alternate versions, Number of expansions, Number of implementations. Along with information about which family of games the games belong to, If it was Kickstarted, The overall rank and the games rank in a particular category.
The following data was discarded as it is not relevant or insufficient for the study Game description, Image of the game, Language, Number of user comments, Number of good players, and the Best players.
 
The community age requirement data is missing for various games, so they have been approximated for the children's game category as 7, 12 for Family games, and 18 for the remaining games.

#### Mechanics
The file contains the mechanics of the games.

#### Themes
The file contains the themes of the games.

#### Subcategories
The file contains the subcategories of the games which were found irrelevant to the study.

#### User Rating
The file contains the ratings per user in detail, which is not necessary for the study.

#### Artists Reduced
This file contains the name of the artists who developed the game. This data was discarded as it is not relevant for this analysis.

#### Publishers Reduced
The file contains the name of the producers who published the game. This data was discarded as it is not relevant for this analysis.

#### Designers Reduced
The file contains the name of the designers who designed the game. This data was discarded as it is not relevant for this analysis.

##### Rating Distribution 
This file contains the rating distribution of the game, but the necessary information is already available in the Games file thus, this was discarded
The preprocessing can be seen in the cleanup [Notebook](./notbeooks/data-cleanup.ipynb)

## Data Visualization and Analysis

We first checked through each of the columns to see the relevant data available. Upon secondary research on trends in lifestyle, the effect of the pandemic, ages, etc. we developed different hypotheses. Using these hypotheses, we found corresponding features matching these trends to model them into our data paradigm. The visualizations can be seen in the viusalization notebook [Link](link).

### Data Point 0: Correlation Between the Board Game Design Features and User Ratings
As a board game developer, it is crucial to analyze which board game design features are correlated with the user ratings. With the correlation heatmap, board game developers can optimize the board game design features to improve the product ratings and players' satisfaction in the future.

### Data Point 1: Games Published per Year

We are interested in the trend of in supposed trend of increased demand in board games. To find this trend we filter data to after 1950 since Board Game Geek has data going into the B.C.s

### Data Point 2: Game Weight
Board game Geek has a rating system of for game complexity. This system ranks games as from 1 to 5. This is a possible key indicator to whether a board is well recieve and/or sells well. First we sum the amount of games in each range to determine if there is an opening in the market. Then we compared complexity to attributes that tied to increased ownership. these include user rating, ownership and number of people who want the game.

### Set 4: Minimum and Maximum Numbers of Players
The optimal minimum and maximum numbers of players for a board game are two of the most important board game design features. Some categories of the board game are more suitable for team players, and some others might be more exciting to play individually. The dataset will be visualized with boxplots to determine the minimum, first quartile, median, third quartile, and maximum players for each board game category minimum and maximum numbers of players.

### Data point 3: Minimum and Maximum Numbers of Players
The optimal minimum and maximum numbers of players for a board game are two of the most important board game design features. Some categories of the board game are more suitable for team players, and some others might be more exciting to play individually. The dataset will be visualized with boxplots to determine the minimum, first quartile, median, third quartile, and maximum players for each board game's minimum and maximum numbers of players per category.


### Data Point 4: Recommended Ages
We want to see the effect of recommended ages on their popularity and ratings. The data has the community's recommendation for minimum age of the players as well as the manufacturer's recommendation for playing age. Using these we see how popular are board games in people of different ages. We also see the gap in the two recommended ages and derive ideas for what kind of games are easier than the manufacturers thought they were. 

### Data Point 5: Popularity of Different Board Game Categories
Analyzing and studying the popularity of different board game categories is crucial for board game developers publishers, and manufacturers. With the data visualization, the board game industry would be able to know which board game categories they should put more effort in the game development to maximize their profits. Besides that, the board game industry can continue to get more feedback from the users to improve the overall board game designs that have low popularity.

### Data Point 6: Reimplementation

We study the effect of number of reimlementations of a game depending on the number of people who own the game, due to the large amount of people we use a log10 scale for the number of people owning the board games.

### Data Point 7: Play time
We are mainly interested in understanding the effect of play time of a game with its popularity. The column 'MfgPlaytime' show the play time as per the manufacturer recommendations. The columns 'ComMinPlaytime' and 'ComMaxPlaytime'show the minimum and maximun play time of the game as per the community


### Data Point 8: Crowdfunding/ Effect of Kickstarter
For a new manufacturer entering the industry, funding is of utmost importance. Hence it is necessary to see if crowdfunding impacts the popularity of games. Crowdfunding also shows that the audience is already excited about the game even before it is released. We explore which categories and themes are most likely to be funded by Kickstarter campaigns and thus add another feature towards designing the most meaningful game from the manufacturer's perspective.

### Data Point 9: Top 10 Board Game Themes for Different Board Game Categories
Visualizing top 10 board game themes for different board game categories for the game developers to understand which board game themes are the most common for different board game categories. With the user rating data and board game themes data, board game developers can determine which board games themes designs are considered a success and which are not. Including the right board game design themes are crucial to capture the interests of board game lovers and increase player engagement towards the board game.

### Data Point 10: Top 10 Board Game Mechanics for Different Board Game Categories
Visualizing the top 10 board game mechanics for different board game categories data is important for the game developers to understand which board game mechanics are the most common for different board game categories. With the user rating data and board game mechanics data, board game developers can determine which board games mechanics designs are considered a success and which are not. Including the right board game design, mechanics are crucial to capture the interests of board game lovers and increase player engagement towards the board game.

### Data Point 11: Board Game Subcategories
Pie charts are ustilised to visualise most popular board game subcategories.

### Data Point 11: Publisher
To be able to sales as many copies of games we must find a will publisher with a track record of publishing games similar games.

## Recommender System
Run recommender_pipeline.py to get started.

In the recommender_pipeline.py, please change board_game_cat to your target categories and in the recommender_surprise function
change target_games to list of BGGId games you are looking insight for.

To train a new model, here are the steps:
1) Download Reviews CSV, https://www.kaggle.com/threnjen/board-games-database-from-boardgamegeek?select=user_ratings.csv
2) Chane review_csv_path to path of Reviews CSV.
3) Uncomment data_processing_surprise and adjust hyperparameters.
4) Uncomment build_model_surprise, you will get the model and performance information. 

