import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib.cm as cm

# importing the cars dataset

cars_df = pd.read_csv("CarsData.csv")
columns = ["Manufacturer", "Model", "Type", "Price", "MPG.city", "MPG.highway",
           "Horsepower", "Rear.seat.room", "Passengers"]

#print(cars_df[columns].head())

# plot a histogram

cars_df["MPG.city"].plot(kind="density")
cars_df["MPG.city"].plot(kind="hist", bins=15, density = True, color = "C2")
plt.suptitle("Distribution of MPG.city", fontsize = 12)

plt.xlim(14,50)
plt.legend()


plt.show()