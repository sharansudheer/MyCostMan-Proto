import pandas as pd

# Write a function to import the file and choose the file format

# export? so that the dataframe df is accessible accross the program after load or throw an error -
# dataframe not loaded
# dataframe loaded but not accessible in the program's global scope like after executing a code block in jupyter notebook,
#  the data is cached in the browser or somewhere 


# From a code point A how do I navigate to load data and get back to A after the data is loaded with a flag 1.
# At Point A, if the flag is 1 and the data is accessible then throw an error/log it
# If the app is shutdown, how do we resume from the last state eg-
# A user navigated from the dashboard to load data. And loaded the data, ie df init is over and the app crashes
# How can the user proceed from the state where df is initalised, goes back to the dashboard
# start an env
# do we need to install pandas, numpy etc. If yes, a startup/app init process, install script, text file with all the things to be installed

filename = "hh"

df = pd.read_excel(filename)