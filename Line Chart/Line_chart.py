import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# importing the cars dataset

cars_df = pd.read_csv("CarsData.csv")
columns = ["Manufacturer", "Model", "Type", "Price", "MPG.city", "MPG.highway",
           "Horsepower", "Rear.seat.room", "Passengers"]

#print(cars_df[columns].head())

# First sort the data to get a proper line chart
cars_df = cars_df.sort_values(by="Horsepower")

# The following lines of code create a blank canvas to plot on
fig, ax = plt.subplots()

# plotting fig 1
# Data is fed and plotted using the following lines
cars_df.plot(ax = ax, x = "Horsepower", y = "MPG.highway", kind = "line", )
cars_df.plot(ax = ax, x = "Horsepower",y= "MPG.city", kind = "line", linestyle='--')

# The following part of code adds labels and titles to make the graph readable
ax.set_ylabel("Mileage in (mile per US gallon)")
ax.set_title("Mileage vs Horsepower",fontsize=12)
plt.show()

# plotting fig 2
plt.plot(cars_df["Horsepower"], cars_df["MPG.city"],label="MPG.city")
plt.plot(cars_df["Horsepower"], cars_df["EngineSize"], label="Engine Size")
plt.plot(cars_df["Horsepower"], cars_df["MPG.highway"], label="MPG.highway")
plt.plot(cars_df["Horsepower"], [i/100 for i in cars_df["RPM"]],label="RPM")
plt.suptitle("Horsepower vs Mileage in city, Engine size, Mileage on highway, RPM",fontsize=12)
plt.xlabel("Horsepower")
plt.ylabel("Mileage in city, Engine size, Mileage on highway, RPM")
plt.legend()
plt.show()

# plotting fig 3
plt.plot(cars_df["MPG.city"],cars_df["Horsepower"],label="MPG.city")
plt.plot(cars_df["EngineSize"],cars_df["Horsepower"],label="Engine Size")
plt.plot(cars_df["MPG.highway"],cars_df["Horsepower"],label="MPG.highway")
plt.plot([i/100 for i in cars_df["RPM"]],cars_df["Horsepower"],label="RPM") # interchanging x and y
plt.suptitle("Mileage in city, Engine size, Mileage on highway, RPM vs Horsepower",fontsize=12)
plt.ylabel("Horsepower")
plt.xlabel("Mileage in city, Engine size, Mileage on highway, RPM")
plt.legend()

plt.show()