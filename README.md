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

### Set 0: Correlation Between the Board Game Design Features and User Ratings
As a board game developer, it is crucial to analyze which board game design features are correlated with the user ratings. With the correlation heatmap, board game developers can optimize the board game design features to improve the product ratings and players' satisfaction in the future.

### Set 4: Minimum and Maximum Numbers of Players
The optimal minimum and maximum numbers of players for a board game are two of the most important board game design features. Some categories of the board game are more suitable for team players, and some others might be more exciting to play individually. The dataset will be visualized with boxplots to determine the minimum, first quartile, median, third quartile, and maximum players for each board game category minimum and maximum numbers of players.

### Set 5: Recommended Ages
We want to see the effect of recommended ages on their popularity and ratings. The data has the community's recommendation for minimum age of the players as well as the manufacturer's recommendation for playing age. Using these we see how popular are board games in people of different ages. We also see the gap in the two recommended ages and derive ideas for what kind of games are easier than the manufacturers thought they were. 

### Set 6: Popularity of Different Board Game Categories
Analyzing and studying the popularity of different board game categories is crucial for board game developers publishers, and manufacturers. With the data visualization, the board game industry would be able to know which board game categories they should put more effort in the game development to maximize their profits. Besides that, the board game industry can continue to get more feedback from the users to improve the overall board game designs that have low popularity.

### Set 9: Crowdfunding
For a new manufacturer entering the industry, funding is of utmost importance. Hence it is necessary to see if crowdfunding impacts the popularity of games. Crowdfunding also shows that the audience is already excited about the game even before it is released. We explore which categories and themes are most likely to be funded by Kickstarter campaigns and thus add another feature towards designing the most meaningful game from the manufacturer's perspective.

### Set 13: Top 10 Board Game Themes for Different Board Game Categories
Visualizing top 10 board game themes for different board game categories for the game developers to understand which board game themes are the most common for different board game categories. With the user rating data and board game themes data, board game developers can determine which board games themes designs are considered a success and which are not. Including the right board game design themes are crucial to capture the interests of board game lovers and increase player engagement towards the board game.

### Set 16: Top 10 Board Game Mechanics for Different Board Game Categories
Visualizing the top 10 board game mechanics for different board game categories data is important for the game developers to understand which board game mechanics are the most common for different board game categories. With the user rating data and board game mechanics data, board game developers can determine which board games mechanics designs are considered a success and which are not. Including the right board game design, mechanics are crucial to capture the interests of board game lovers and increase player engagement towards the board game.
