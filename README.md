# Football-Tracking-Interpolation
Code to process Statsbomb 360 data to estimate the positions of off-camera players.

This repository contains the following files:

**Statsbomb_Processing.ipynb:** This contains the code for processing Statsbomb 360 data.

**Helper_Functions.py** This contains extra functions for processing.

**Model_n.pkl** These are the pre-trained ARMAX models for predicting the x and y coordinates of players.

**n_Perc.png:** These images show the predicted positions and true positions when the code was used on the test dataset generated from Metrica Sports data at the nth percentile of errors (with higher n reflecting higher overall errors).

**Neat_Code_nH.ipynb:** The code used to process half "n" of the Metrica Sports test data.

**Error_Analyis.ipynb:** The code used to analyse the errors between the predicted and true positions for the Metrica Sports test data

**XXX.npy:** These store the errors from the predictions on the test data.


Statsbomb 360 matches can be processed using the "Statsbomb_Processing.ipynb" notebook.
