# Cars-Data-Visualization-

This repository contains Python scripts and resources to visualize various aspects of a car dataset (`CarsData.csv`). Each visualization type is organized into its own folder with code, instructions, and output screenshots to make it easy to understand and reproduce the visualizations. These visualizations reveal insights into features like car pricing, fuel efficiency, mileage in city, distribution of MPG.city, milage on highway, engine size and horsepower, providing a clear and interactive data overview.

## Project Structure

- **`boxplot/`**: Contains the box plot visualization scripts and documentation.
- **`bar chart/`**: Contains the bar chart visualization scripts and documentation.
- **`scatter plot/`**: Contains the scatter plot visualization scripts and documentation.
- **`line chart/`**: Contains the line chart visualization scripts and documentation.
- **`histogram/`**: Contains the histogram visualization scripts and documentation.
- **`pie chart/`**: Contains the pie chart visualization scripts and documentation.

Each folder includes:
- `visualization_type.py`: Python script to generate the respective chart.
- `visualization_type.txt`: Instructions and explanations about the code and dataset.
- `output_screenshot.png`: Screenshot of the resulting chart for reference.

---

## Folder Descriptions and Usage

### Box Plot
- **Folder**: `boxplot/`
- **Script**: `box_plot.py`
- **Documentation**: `boxplot.txt`
- **Output**: `figure.png`

The box plot summarizes key statistics for specific columns, such as the Prices of car according to car type. This plot can help identify the distribution and outliers in each variable.

### Bar Chart
- **Folder**: `bar chart/`
- **Script**: `bar_chart.py`
- **Documentation**: `barchart.txt`
- **Output**: `figure.png`

This bar chart categorizes cars by type or manufacturer, allowing comparison between categorical data.

### Scatter Plot
- **Folder**: `scatter plot/`
- **Script**: `scatter_plot.py`
- **Documentation**: `scatterplot.txt`
- **Output**: `figure.png`

The scatter plot shows relationships between two numerical variables, such as Horsepower and MPG, to identify trends or correlations.

### Line Chart
- **Folder**: `line chart/`
- **Script**: `line_chart.py`
- **Documentation**: `linechart.txt`
- **Output**: `figure.png`

This line chart visualizes trends in continuous data, like Horsepower over time or by index.

### Histogram
- **Folder**: `histogram/`
- **Script**: `histogram.py`
- **Documentation**: `histogram.txt`
- **Output**: `figure.png`

The histogram illustrates the frequency distribution of numerical variables such as Price or MPG, showing the spread of values.

### Pie Chart
- **Folder**: `pie chart/`
- **Script**: `pie_chart.py`
- **Documentation**: `piechart.txt`
- **Output**: `figure.png`

The pie chart demonstrates the percentage distribution of categorical data, like the number of cars per type or manufacturer.

---

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VaibhavGovindwar/Car-Data-Visualization.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Car-Data-Visualization
   ```

3. Install Dependencies:
  ```bash
  pip install python 3.10
  pip install numpy
  pip install pandas
  pip install matplotlib
  ```

4. Run the Scripts:

- Navigate to each folder and run the respective script.
- For example, to view the box plot:

  ```bash
  cd box plot
  python box_plot.py
  ```

## Screenshots:
- Each folder contains output screenshots

## Contributing:
I want you to know that contributions to improving the dataset or visualizations are welcome. Please open an issue or submit a pull request.

## License: 
This project is licensed under the MIT License. See the LICENSE file for more details.
