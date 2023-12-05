''' 
Python code to play the Find the Cat Game (please see the README.TXT for details)
'''

# Import libraries
import random
import numpy as np
import pandas as pd

# Define the box-opening sequences for each approach
sequence_traditional = (2, 3, 4, 4, 3, 2, 2)
sequence_bayesian = (2, 2, 3, 4, 4, 3, 2)

# Create dataframes to store the results after each game
result_traditional = pd.DataFrame(columns=["ft1", "ft2", "ft3", "ft4", "ft5", "ft6", ""ft7])
result_bayesian = pd.DataFrame(columns=["fb1", "fb2", "fb3", "fb4", "fb5", "fb6", "fb7"])

# Create dataframes to store the cumulative probabilities atfer each game
cdf_traditional = pd.DataFrame(columns=["ct1", "ct2", "ct3", "ct4", "ct5", "ct6", "ct7"])
cdf_bayesian = pd.DataFrame(columns=["cb1", "cb2", "cb3", "cb4", "cb5", "cb6", "cb7"])

# Create dataframes to store the cumulative results after each game
cum_result_traditional = pd.DataFrame(columns=["rt1", "rt2", "rt3", "rt4", "rt5", "rt6", "rt7"])
cum_result_bayesian = pd.DataFrame(columns=["rb1", "rb2", "rb3", "rb4", "rb5", "rb6", "rb7"])

# Set the number of simulations
s = -1
while s < 999:
    s += 1
    # Hide the cat in one of the five boxes
    cat_in_box = random.randint(1, 5)

    # Create and reset the lists to store the results for each game
    open_traditional = [0, 0, 0, 0, 0, 0, 0]
    open_bayesian = [0, 0, 0, 0, 0, 0, 0]

    # Reset the game results
    traditional_found = False
    bayesian_found = False

    # Look for the cat applying the sequences of the two approaches
    for b in range(7):
        if sequence_traditional[b] == cat_in_box and traditional_found == False:
            open_traditional[b] += 1
            traditional_found = True
        if sequence_bayesian[b] == cat_in_box and bayesian_found == False:
            open_bayesian[b] += 1
            bayesian_found = True
        # Move the cat one box left or right. If the cat is in the leftmost / rightmost box, then move it to the right / left.
        if cat_in_box == 1:
            cat_in_box += 1
        elif cat_in_box == 5:
            cat_in_box -=1
        else: 
            cat_in_box += random.choice([-1, 1]) 

    # Append the cumulative results
    result_traditional.loc[s] = open_traditional
    result_bayesian.loc[s] = open_bayesian

        
    # Append the cumulative results
    cum_result_traditional.loc[s] = np.cumsum(result_traditional)
    cum_result_bayesian.loc[s] = np.cumsum(result_bayesian)
    
    # Append the cumulative distributions
    cdf_traditional.loc[s] = np.round_((cum_result_traditional.loc[s] / sum(cum_result_traditional.loc[s])), decimals = 2).tolist()  
    cdf_bayesian.loc[s] = np.round_((cum_result_bayesian.loc[s] / sum(cum_result_bayesian.loc[s])), decimals = 2).tolist()

# Write the dataframes to csv files
cum_result_traditional.to_csv("cum_result_traditional.csv")
cdf_traditional.to_csv("cdf_traditional.csv")
cum_result_bayesian.to_csv("cum_result_bayesian.csv")
cdf_bayesian.to_csv("cdf_bayesian.csv")
