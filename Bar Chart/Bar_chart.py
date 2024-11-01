import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# importing the cars dataset

cars_df = pd.read_csv("CarsData.csv")
columns = ["Manufacturer", "Model", "Type", "Price", "MPG.city", "MPG.highway",
           "Horsepower", "Rear.seat.room", "Passengers"]

#print(cars_df[columns].head())

fig = plt.figure()

# code to create bar chart
# vertical Bar chart
plt.bar(cars_df["DriveTrain"], cars_df["MPG.city"],width=0.2,label="Mileage in city")

# title and label
plt.suptitle("DriveTrain vs MPG.city",fontsize=12)
plt.xlabel("DriveTrain")
plt.ylabel("MPG.city")

# legend
plt.legend()

plt.show()

# horizontal bar graph
plt.barh(cars_df["DriveTrain"], cars_df["MPG.city"],height=0.2,label="Mileage in city")
plt.xlabel("MPG.city")
plt.ylabel("DriveTrain")

plt.show()

# Stacked Bar Chart
# Use the following code snippet to filter the unique values of no. of passengers a car can carry
cars_df["Passengers"].unique()

# Use the following code snippet to filter the unique values of Types of car.
cars_df["Type"].unique()

# Use the following code snippet to filter the data and obtain the target columns into a separate dataframe.
grouped_data = cars_df[["Passengers","Type"]].groupby(by = ["Passengers","Type"]).size().unstack().reset_index()

print(grouped_data)

# Stacked Bar Graph can be plotted using the grouped data, as follows:
grouped_data.plot(x="Passengers",kind="bar",stacked=True,colormap=cm.Paired)

# ------------- Error bar CHart------------------
# Error bars can be added to the stacked bar graph with the 'yerr' argument as follows
grouped_data.plot(x="Passengers",kind="bar",stacked=True,colormap=cm.seismic,yerr=np.std(cars_df["Passengers"]))

plt.show()

# --------------- Grouped Bar Chart ------------------
# let's see the unique value of "DriveTrain"
cars_df["DriveTrain"].unique()

grouped_cars = cars_df[["MPG.city", "MPG.highway", "RPM", "DriveTrain"]].groupby(by="DriveTrain").mean().T

print(grouped_cars)

# Now, let us plot the bar chart
grouped_cars.loc["RPM"] /= 100
# assign the value for the width of bar and number of groups
width = 0.2
# assign a unique value in range of "DriveTrain"
ind = list(range(len(cars_df["DriveTrain"].unique())))
print(grouped_cars.loc["RPM"])
# now, plot the bar chart for the grouped_cars
plt.bar([i for i in ind], height=grouped_cars["4WD"], label="4WD", width=width)
plt.bar([i+width for i in ind], height=grouped_cars["Front"],
        width=width, bottom=0, label="Front")
plt.bar([i+width*2 for i in ind], height=grouped_cars["Rear"],
        label="Rear", width = width, bottom=0)

plt.suptitle("Mileage in City, Mileage on Highway, RPM vs DriveTrain", fontsize = 12)
plt.xlabel("Mileage in City, Mileage in Highway, RPm")
plt.ylabel("Average per Drivetrain Type")
plt.xticks([i+width for i in ind], ["Mileage in City", "Mileage in Highway", "RPM"])

plt.legend()
plt.show()