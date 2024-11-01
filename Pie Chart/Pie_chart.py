import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# importing the cars dataset

cars_df = pd.read_csv("CarsData.csv")
columns = ["Manufacturer", "Model", "Type", "Price", "MPG.city", "MPG.highway",
           "Horsepower", "Rear.seat.room", "Passengers"]

#print(cars_df[columns].head())

# First, see the unique number of cylinders a car contains.
cars_df["Cylinders"].unique()

# Create the pie chart
grouped_data = cars_df[["Cylinders", "Type"]].groupby(by=["Cylinders", "Type"]).size().unstack()
fig, ax = plt.subplots(2,3, figsize=(10,7))
grouped_data.plot.pie(ax = ax, subplots = True, fontsize = 12)
fig.suptitle("Number of Cars for each type of Cylinders", fontsize = 12)
fig.tight_layout()
plt.show()