# ECE143-Group1-WI22 Group I

## Summary
Board Games are slowly becoming an integral part of the life. Using a collection of different features about the most popular games, we aim to extract the recipe for the most popular board game. We use the Board Game Geek database as the main data bank and analyse different hypotheses and conditions to recommend the best game.

## Team
- Kai Chuen Tan
- Manas Bedmutha
- Siddhant Saoji
- Joshua Smith
- Ali Zaidi
- Xiaolei Du

## Data Selection & Collection
The goal of the analysis is to find the best parameters to make a game. In this sense, BoardGameGeek is a large repository of games and their metrics. BoardGameGeek is a community platform for board game enthusiasts to discuss and explore new board games, interact about their progress and rate their favorites. The database also has numerous details about each game. The categories, themes, mechanics, popularity metrics among others can help us gain deep insights into the community of board game players.

We found many people had tried to collect different aspects and details about board games. But the BGG database seemed to be the most complete. We found a very recent snapshot of this data on Kaggle and chose to use that for our analysis. The data was scraped and collected by a user on Kaggle. More details about the dataset can be found [here](https://www.kaggle.com/threnjen/board-games-database-from-boardgamegeek?select=bgg_data_documentation.txt).

## Data Cleaning
Cleaning ... [Notebook](./notbeooks/data-cleanup.ipynb)

## Data Visualization and Analysis

We first checked through each of the columns to see the relevant data available. Upon secondary research on trends in lifestyle, the effect of the pandemic, ages, etc. we developed different hypotheses. Using these hypotheses, we found corresponding features matching these trends to model them into our data paradigm. The visualizations can be seen in the viusalization notebook [Link](link).

### Set 5: Recommended Ages
We want to see the effect of recommended ages on their popularity and ratings. The data has the community's recommendation for minimum age of the players as well as the manufacturer's recommendation for playing age. Using these we see how popular are board games in people of different ages. We also see the gap in the two recommended ages and derive ideas for what kind of games are easier than the manufacturers thought they were. 

### Set 9: Crowdfunding
For a new manufacturer entering the industry, funding is of utmost importance. Hence it is necessary to see if crowdfunding impacts the popularity of games. Crowdfunding also shows that the audience is already excited about the game even before it is released. We explore which categories and themes are most likely to be funded by Kickstarter campaigns and thus add another feature towards designing the most meaningful game from the manufacturer's perspective.