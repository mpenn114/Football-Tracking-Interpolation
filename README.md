# Football-Tracking-Interpolation
Code to process Statsbomb 360 data to estimate the positions of off-camera players.

### Using the Model
1. Data
To use this model, it is necessary to have the following data:
- `open-data/data/three-sixty`: This should contain the 360 data in files named "[match_id].json"
- `open-data/data/three-sixty`: This should contain the event data in files named "[match_id].json"

Note that `open-data` should be a folder at the top level of the repository. This file structure can be achieved with Statsbomb's open data by running
```bash
!git clone https://github.com/statsbomb/open-data
```

Note that this is a large repository and therefore this command may take a substantial amount of time to run

2. Running the Code
To run the code, you must run all cells in the `Statsbomb_Processing.ipynb` notebook. This will create a folder called `Outputs` at the top level of the repository, which will contain processed 360 files, again named "[match_id].json".

3. Using the Data
We believe that the model implemented in this repository gives good-quality outputs, and should be useful for, for example, examining team shape in different phases of play. However **all the outputs are estimates** and so should not be treated as exact measurements of player positions. In particular:

- Off-camera movements are difficult to predict, and therefore this data will not be a reliable source for, for example, categorising runs that are not captured on screen

- The predictions will be less accurate for players that spend a lot of time off-camera. This is particularly true for goalkeepers

### Testing:
To check that all packages have been installed correctly, we have included some dummy data in `open-data/data`. To test that the model works, you can run all the cells in the `Statsbomb_Processing.ipynb` notebook, which processes this test JSON and checks that the output data is of the correct format. Do raise an issue on the page if you have problems running this test.

### File List:

This repository contains the following files:

**Statsbomb_Processing.ipynb:** This contains the code for processing Statsbomb 360 data.

**Helper_Functions.py** This contains extra functions for processing.

**Model_n.pkl** These are the pre-trained ARMAX models for predicting the x and y coordinates of players.

**n_Perc.png:** These images show the predicted positions and true positions when the code was used on the test dataset generated from Metrica Sports data at the nth percentile of errors (with higher n reflecting higher overall errors).

**Neat_Code_nH.ipynb:** The code used to process half "n" of the Metrica Sports test data.

**Error_Analyis.ipynb:** The code used to analyse the errors between the predicted and true positions for the Metrica Sports test data

**XXX.npy:** These store the errors from the predictions on the test data.

