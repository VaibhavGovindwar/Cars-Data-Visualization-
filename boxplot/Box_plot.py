import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# importing the cars dataset

cars_df = pd.read_csv("CarsData.csv")
columns = ["Manufacturer", "Model", "Type", "Price", "MPG.city", "MPG.highway",
           "Horsepower", "Rear.seat.room", "Passengers"]

#print(cars_df[columns].head())

# plot Box plot
# create a box plot for variable "Price"
cars_df["Price"].plot(kind="box")


# ----------------------------plot Sub Plot -----------------------------
# The following lines enable us to use subplot functionality
fig, (ax1, ax2) = plt.subplots(2, 1)

# you can Set a height and width of the fig
# using fig.set_figwidth() and fig.set_figheight()

# The following lines of code change the alignment from vertical to horizontal
ax1.boxplot(cars_df["Horsepower"],vert=False)
ax2.boxplot(cars_df["MPG.city"],vert=False)

# title
fig.suptitle("Box Plot Using Sub Plot", fontsize=16)

# The following lines of code are used to add labels to axes and title to the graph
ax1.set_title('Horsepower')
ax1.set_xlabel('Horsepower')
ax2.set_title('City Mileage')
ax2.set_xlabel("City Mileage (in miles per US gallon)")


# In case of any superimposition of the subplots, the following functions caters the aesthetics
fig.tight_layout()

# ---------------- Multiple Box Plots with Same Axes ---------------------
# Setting up the plot, length and width of the figure
fig, ax = plt.subplots(2, 3, sharey=True, sharex=True)

# title
fig.suptitle("Multiple Box Plots", fontsize=16)

# Accessing each partition[m][n] and providing the plot and its title
ax[0][0].boxplot(cars_df["Price"][cars_df["Type"]=="Compact"])
ax[0][0].set_title('Compact')
ax[0][1].boxplot(cars_df["Price"][cars_df["Type"]=="Large"])
ax[0][1].set_title('Large')
ax[0][2].boxplot(cars_df["Price"][cars_df["Type"]=="Midsize"])
ax[0][2].set_title('Midsize')
ax[1][0].boxplot(cars_df["Price"][cars_df["Type"]=="Small"])
ax[1][0].set_title('Small')
ax[1][1].boxplot(cars_df["Price"][cars_df["Type"]=="Sporty"])
ax[1][1].set_title('Sporty')
ax[1][2].boxplot(cars_df["Price"][cars_df["Type"]=="Van"])
ax[1][2].set_title('Van')

# ---------------- multiple Box Plots --------------------------
# Finding the list of unique values of 'car type'
car_type_list = cars_df["Type"].unique()
print(car_type_list)

# The following lines enable us to use subplot functionality
fig, ax = plt.subplots()


# creating a box plot for every unique car type
ax.boxplot([cars_df["Price"][cars_df["Type"]==k] for k in car_type_list])

# To set the position for each plots in the iteration
# create a list of values which contain the data required for plotting each box plot.
# Each item in the list is the data associated with each type of car in the car_type_list.

plt.xticks([i for i in range(1,len(car_type_list)+1)],[k for k in car_type_list])

# super-title
fig.suptitle("Prices of car according to car type", fontsize=16, y = 1)

plt.show()