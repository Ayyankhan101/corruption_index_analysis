# Corruption Perception Index Analysis

This project analyzes the Corruption Perception Index (CPI) data to identify and visualize the most and least corrupt countries, and to cluster countries based on their corruption levels.

## Features

- Loads CPI data from a CSV file.
- Identifies and displays the top 10 most and least corrupt countries.
- Visualizes CPI scores using bar charts and histograms.
- Applies K-Means clustering to group countries by corruption levels.

## Data

The data used in this analysis is a simulated dataset based on the Corruption Perception Index. It is stored in `corruption_data.csv`.

## Usage

To run the analysis, you need to have Python and the following libraries installed:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

### Running the Data Script (Optional)

The `get_corruption_data.py` script is provided to demonstrate how data might be fetched or loaded. In this project, it simply reads from the `corruption_data.csv` file.

```bash
python get_corruption_data.py
```

### Using the Jupyter Notebook

Open and run the `corruption_analysis.ipynb` notebook to perform the data analysis, visualizations, and machine learning clustering.

```bash
jupyter notebook corruption_analysis.ipynb
```
