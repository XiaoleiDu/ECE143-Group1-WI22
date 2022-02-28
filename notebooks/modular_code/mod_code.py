import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

def plot_Min_Max_Players_Boxplot(games_df, BG_cat, BG_cat_name, showfliers = [False, False], notches = [False, False]):
    """
    Plot Min and Maximum Number of Players of a Board Game Category Boxplots
    :Inputs (Type)        : 1.) game_df (pd.Dataframe)       - Board game data frame
                            2.) BG_cat (str)                 - Board Game Category
                            3.) BG_cat_name (str)            - Board Game Category name
                            4.) showfliers (Bool in list)    - To plot outliers or not
                            5.) notches (Bool in list)       - To plot notches
                            

    :Output (Type)        : 1.) None
    """
    # Make sure it is a panda series
    assert isinstance(games_df, pd.DataFrame)
    # Make sure it is a string and valid board game categories
    assert isinstance(BG_cat, str)
    assert BG_cat in list(games_df.columns[34:].values.tolist())
    # Check for valid showfliers input
    assert isinstance(showfliers, list)
    for showflier in showfliers:
        assert isinstance(showflier, bool)
    # Check for valid notches input
    assert isinstance(notches, list)
    for notch in notches:
        assert isinstance(notch, bool)
    # Check for valid board game category name
    assert isinstance(BG_cat_name, str)
    assert BG_cat_name in ['Thematic', 'Strategy', 'War', 'Family', 'CGS', 'Abstract', 'Party', 'Childrens']

    # Replace 0 zeros with NaN to prevent creating another subcategory for the boxplot
    games_df[BG_cat] = games_df[BG_cat].replace({0:np.nan})

    ## Create two subplots of a boxplot for Thematic Board Game's Minimum and Maximum Number of Players
    _, axes = plt.subplots(1, 2)

    # Minimum Number of Players
    ax_min = sns.boxplot(x=BG_cat, y='MinPlayers', palette="Oranges", width = 0.3, ax=axes[0],
                            data=games_df, showfliers=showfliers[0], notch=notches[0])
    plt.suptitle( BG_cat_name + " Board Game Category\nMinimum and Maximum Number of Players", fontweight='bold', fontsize = 16)
    ax_min.set(xlabel=None)
    ax_min.set_ylabel("Number of Minimum Players", fontsize=12, fontweight='bold')
    ax_min.set_xticklabels([])
    ax_min.axes.get_xaxis().set_visible(False)

    # Maximum Number of Players 
    ax_max = sns.boxplot(x=BG_cat, y='MaxPlayers', palette="mako",  width = 0.3, ax=axes[1],
                data=games_df, showfliers=showfliers[1], notch=notches[1])
    ax_max.set(xlabel=None)
    ax_max.set_ylabel("Number of Maximum Players", fontsize=12, fontweight='bold')
    ax_max.set_xticklabels([])
    ax_max.axes.get_xaxis().set_visible(False)

def manipulate_Y_vs_X_data(games_df, board_game_Y_vs_X, Y_data_frame):

    """
    Manipulate Y vs X Data counts.
    :Inputs (Type)        : 1.) game_df (pd.Dataframe)       - Board game data frame
                            2.) board_game_Y_vs_X (array)    - Y vs X relationship to manipulate
                            3.) Y_data_frame (pd.Dataframe)  - Y dataframe
                            
    :Output (Type)        : 1.) board_game_Y_vs_X (array)    - Final counts Y vs X relationship to manipulate
    """
    # Make sure it is a panda series
    assert isinstance(games_df, pd.DataFrame)
    assert isinstance(Y_data_frame, pd.DataFrame)
    # Make sure it is an array
    assert isinstance(board_game_Y_vs_X, np.ndarray)

    # Thematic Category
    thematic_cat = games_df['Cat:Thematic'].to_numpy()
    # Strategy Category
    strategy_cat = games_df['Cat:Strategy'].to_numpy()
    # War Category
    war_cat = games_df['Cat:War'].to_numpy()
    # Family Category
    family_cat = games_df['Cat:Family'].to_numpy()
    # Crafts, Games, and Science (CGS) Category
    CGS_cat = games_df['Cat:CGS'].to_numpy()
    # Abstract Category
    abstract_cat = games_df['Cat:Abstract'].to_numpy()
    # Party Category
    party_cat = games_df['Cat:Party'].to_numpy()
    # Childrens Category
    childrens_cat = games_df['Cat:Childrens'].to_numpy()


    for idx in range(0, len(games_df)):
    
        # If it is a thematic category, starts counting
        if thematic_cat[idx] == 1:
        
            # Update counts
            board_game_Y_vs_X[:,0] += Y_data_frame.iloc[idx].to_numpy()
        
        # If it is a startegic category, starts counting
        if strategy_cat[idx] == 1:
        
            # Update counts
            board_game_Y_vs_X[:,1] += Y_data_frame.iloc[idx].to_numpy()
        
        # If it is a war category, starts counting
        if war_cat[idx] == 1:
        
            # Update counts
            board_game_Y_vs_X[:,2] += Y_data_frame.iloc[idx].to_numpy()
    
        # If it is a family category, starts counting
        if family_cat[idx] == 1:
        
            # Update counts
            board_game_Y_vs_X[:,3] += Y_data_frame.iloc[idx].to_numpy()
        
        # If it is a CSG category, starts counting
        if CGS_cat[idx] == 1:
        
            # Update counts
            board_game_Y_vs_X[:,4] += Y_data_frame.iloc[idx].to_numpy()
        
        # If it is a abstract category, starts counting
        if abstract_cat[idx] == 1:
        
            # Update counts
            board_game_Y_vs_X[:,5] += Y_data_frame.iloc[idx].to_numpy()
    
        # If it is a party category, starts counting
        if party_cat[idx] == 1:
        
            # Update counts
            board_game_Y_vs_X[:,6] += Y_data_frame.iloc[idx].to_numpy()
        
        # If it is a childrens category, starts counting
        if childrens_cat[idx] == 1:
        
            # Update counts
            board_game_Y_vs_X[:,7] += Y_data_frame.iloc[idx].to_numpy()

    return board_game_Y_vs_X


def plot_top_10_hbar(board_game_Y_vs_X_df, Y_label, BG_cat_name, plt_hatch = '*', plt_color = '#1f77b4'):

    """
    Plot top 10 Y features.
    :Inputs (Type)        : 1.) board_game_Y_vs_X (array)    - Y vs X data frame
                            2.) Y_label (str)                - Y label name
                            2.) BG_cat_name (str)            - Board Game Category name
                            3.) plt_hatch (str)              - Plot hatch
                            4.) plt_color (str)              - Plot color
                            
    :Output (Type)        : 1.) None
    """
    # Make sure it is a dataframe
    assert isinstance(board_game_Y_vs_X_df, pd.DataFrame)
    # Check for valid board game category name
    assert isinstance(BG_cat_name, str)
    assert BG_cat_name in ['Thematic', 'Strategy', 'War', 'Family', 'CGS', 'Abstract', 'Party', 'Childrens']
    # Check for valid plot inputs
    assert isinstance(plt_hatch, str)
    assert isinstance(plt_color, str)
    assert isinstance(Y_label, str)

    # Dataframe in percentage
    board_game_Y_vs_X_df_percent_df = board_game_Y_vs_X_df / board_game_Y_vs_X_df.sum(axis=0).to_numpy() * 100
    # Top 10 Y
    sorted_df = board_game_Y_vs_X_df_percent_df.nlargest(10, BG_cat_name)

    # Board Game Category placement for plotting
    if BG_cat_name == 'Thematic': placement = 0
    if BG_cat_name == 'Strategy': placement = 1
    if BG_cat_name == 'War': placement = 2
    if BG_cat_name == 'Family': placement = 3
    if BG_cat_name == 'CGS': placement = 4
    if BG_cat_name == 'Abstract': placement = 5
    if BG_cat_name == 'Party': placement = 6
    if BG_cat_name == 'Childrens': placement = 7

    # Plot graphs
    plt.figure(figsize=(10,10))
    ax1 = board_game_Y_vs_X_df_percent_df[BG_cat_name].sort_values(ascending=False).head(10).plot(kind='barh', hatch = plt_hatch, color = plt_color, edgecolor = 'white')
    ax1.set_ylabel("")
    ax1.set_title('Top 10 ' + Y_label + ' for ' + BG_cat_name + ' Board Games', fontweight='bold', fontsize = 16)
    ax1.set_xlim([0, np.ceil(sorted_df.iloc[0,placement]) + 3])
    ax1.set_xlabel("Share [%]", fontsize = 14, fontweight = 'bold')

    # Annotate the percentage value
    for i, perc in enumerate(sorted_df.iloc[:10,placement]):

        ax1.text(perc + 0.05, i -0.05, f'{sorted_df.iloc[i,placement]:0.1f} %', color='black', fontweight='bold')
    
    plt.show()