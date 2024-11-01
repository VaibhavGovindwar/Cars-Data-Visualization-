import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# importing the cars dataset

cars_df = pd.read_csv("CarsData.csv")
columns = ["Manufacturer", "Model", "Type", "Price", "MPG.city", "MPG.highway",
           "Horsepower", "Rear.seat.room", "Passengers"]

#print(cars_df[columns].head())

# To Plot the data as a scatter plot
ax = cars_df.plot(["Horsepower"],["MPG.city"],kind="scatter", color = "black",marker = "*")

# To add labels and title to the output
ax.set_xlabel("Horsepower")	#sets label for x-axis
ax.set_ylabel("MPG.city")	#sets label for y-axis
ax.set_title("Horsepower vs MPG.city",fontsize=16)	#sets title for the graph

# Scatter Plot Based on a Category
car_type_list = cars_df["Type"].unique()
fig = plt.figure()

# We extract the colours using the 'seismic_r' method. Here, 'r' indicates the reverse.
colors = cm.seismic_r(np.linspace(0, 1, len(car_type_list)))

# for every car type in the car_type_list we plot all the points in the scatter plot
for car_type,c in zip(car_type_list,colors):
    x = cars_df[cars_df["Type"] == car_type]["Horsepower"]
    y = cars_df[cars_df["Type"] == car_type]["MPG.city"]
    plt.scatter(x,y,color = c,label=car_type)
plt.suptitle("Scatter plot of horsepower and mileage",fontsize=16)
plt.xlabel("Horsepower")
plt.ylabel("Mileage City")
plt.legend()

plt.show()