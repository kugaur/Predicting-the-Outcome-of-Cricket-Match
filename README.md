Predicting-the-Outcome-of-Cricket-Match
=======================================

This project aims to predict the outcome of a cricket match given the team configurations and the previous performances of the players. 

Steps
1) Run scoreboards.py to get the urls of scoreboards of matches played between India and any other country. The list containing the urls will be stored as India_url.pkl file
2) Run rawdata.py to the detailed data of the matches. This will save the data as rawdata1.csv
3) Run training.py to train the model on using rawdata1.csv
4) Run the testing.csv to test the model.
