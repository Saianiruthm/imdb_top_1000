
# IMDb Top 1000 Dataset Analysis

## Overview
This repository contains an in-depth analysis of the IMDb Top 1000 movies dataset using Python, Pandas, Seaborn, and Matplotlib libraries. The dataset includes information about various movies, including IMDb ratings, directors, genres, gross earnings, and more.

## Table of Contents
- [Dataset Information](#dataset-information)
- [Repository Structure](#repository-structure)
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
- [Visualizations](#visualizations)
- [Insights](#insights)
- [Files and Folders](#files-and-folders)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Dataset Information
The dataset "imdb_top_1000.csv" consists of 1000 entries and 16 columns containing various attributes of the top-rated IMDb movies.

## Repository Structure
The repository structure is organized as follows:
- **index.py**: Python file containing the code for data cleaning, preprocessing, analysis, and visualization.
- **/visualizations**: Folder containing visualizations generated from the analysis.
- **README.md**: This file providing an overview of the project.

## Data Cleaning and Preprocessing
The `index.py` script performs extensive data cleaning and preprocessing tasks, including:
- Handling missing values
- Converting data types
- Creating new columns for analysis (e.g., Main Genre, Decade, Adjusted Gross)

## Visualizations
The analysis generates various visualizations to explore different aspects of the dataset, including:
- Bar charts
- Line plots
- Scatter plots
- Box plots
- Heatmaps
- 3D plots

All visualizations are saved in the `/visualisations` folder for reference.

## Insights
Key insights derived from the analysis include:
- Distribution of movie genres
- Trends in IMDb ratings over the years
- Relationship between gross earnings, ratings, and runtime
- Top directors by average gross earnings
- Genre popularity trends
- Correlations between different attributes

## Files and Folders
- `imdb_top_1000.csv`: The dataset file.
- `index.py`: Python script for data analysis.
- `/visualisations`: Folder containing visualizations.
- `/visualisations/*.png`: Various visualizations generated from the analysis.

## Usage
To reproduce the analysis:
1. Clone the repository:
```bash
git clone https://github.com/Saianiruthm/imdb_top_1000.git
```
2. Run the following command in your terminal or command prompt to install the required packages:
```bash
pip install -r requirements.txt
```
3. Run following command to perform data analysis and generate visualizations.
```bash
index.py
```

## Requirements
To run the analysis, ensure you have the necessary Python libraries installed. You can install them using `pip` and the provided `requirements.txt` file.

### Installation
Run the following command in your terminal or command prompt to install the required packages:

```bash
pip install -r requirements.txt
```

This command will install all the dependencies listed in the `requirements.txt` file.

### Requirements File
The `requirements.txt` file includes the following dependencies:
- pandas
- seaborn
- matplotlib

Make sure to have these packages installed in your Python environment before running the analysis script.

## Medium Article
The `Medium_Article.md` file contains a Medium article discussing the analysis, insights, and findings derived from the IMDb Top 1000 dataset. It provides a detailed explanation of the analyses performed and the significance of the derived insights.You may also find article[here](https://medium.com/@sai2804aniruth/unveiling-movie-trends-in-depth-analysis-of-imdb-top-1000-dataset-4d707a5e31c5)

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or additional analyses, feel free to open an issue or create a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
