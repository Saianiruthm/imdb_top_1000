# Import the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the csv file into a dataframe
df = pd.read_csv("imdb_top_1000.csv")

# Display the first five rows of the dataframe
df.head()


# Check the shape, size and info of the dataframe
df.shape # (1000, 16)
df.size # 16000
df.info() # No missing values, some columns are of object type

# Drop the Poster_Link column as it is not relevant for analysis
df = df.drop("Poster_Link", axis=1)

# Convert the Released_Year column to numeric type
df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors="coerce")

# Convert the Runtime column to numeric type by removing the "min" suffix
df["Runtime"] = df["Runtime"].str.replace(" min", "").astype(int)

# Convert the IMDB_Rating column to numeric type
df["IMDB_Rating"] = pd.to_numeric(df["IMDB_Rating"], errors="coerce")

# Convert the Meta_score column to numeric type
df["Meta_score"] = pd.to_numeric(df["Meta_score"], errors="coerce")

# Convert the No_of_Votes column to numeric type
df["No_of_Votes"] = pd.to_numeric(df["No_of_Votes"], errors="coerce")

# Convert the Gross column to numeric type by removing the "," separator
df["Gross"] = df["Gross"].str.replace(",", "").astype(float)

# Display the summary statistics of the numerical columns
df.describe()

# Display the unique values and counts of the categorical columns
df['Certificate'].value_counts()
df['Genre'].value_counts()
df['Director'].value_counts()

# Create a new column for the main genre of each movie
df['Main_Genre'] = df['Genre'].str.split(',').str[0] # Split the genre column by comma and take the first element

# Display the unique values and counts of the main genre column
df['Main_Genre'].value_counts()

# Count the occurrences of each genre
genre_counts = df['Genre'].str.split(',').explode().value_counts()

# Display the genre counts
print(genre_counts)

# Create a new column for the decade of each movie
df['Decade'] = (df['Released_Year'] // 10) * 10 # Divide the released year by 10 and multiply by 10 to get the decade

# Display the unique values and counts of the decade column
df['Decade'].value_counts()

# Create a new column for the adjusted gross earnings of each movie
# Assume an average inflation rate of 3% per year
df['Adjusted_Gross'] = df['Gross'] * (1.03 ** (2024 - df['Released_Year'])) # Multiply the gross by the inflation factor

# Check the dataframe info to see the data types and missing values
df.info()

# Display the first five rows of the dataframe with the new columns
df.head()

# Calculate average ratings per genre without exploding the column
genre_avg_ratings = df.assign(Genre=df['Genre'].str.split(',')).explode('Genre').groupby('Genre')['IMDB_Rating'].mean()

# Plotting the average ratings
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_avg_ratings.index, y=genre_avg_ratings.values, color='blue')
plt.xlabel('Genre')
plt.ylabel('Average IMDB Rating')
plt.title('Bar Chart of Average IMDB Ratings by Genre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Average_IMDB_Ratings_by_Genre.png')
plt.show()

# Insight: The bar chart shows that the average IMDB ratings are similar across different film genres, around 7.

# Group by Director and calculate mean gross earnings
director_gross = df.groupby('Director')['Gross'].mean().sort_values(ascending=False)

# Visualize top directors by average gross earnings
top_directors = director_gross.head(10)  # Select top 10 directors for visualization
plt.figure(figsize=(10, 6))
sns.barplot(x=top_directors.index, y=top_directors.values,hue = top_directors.index,legend=False, palette='viridis')
plt.xticks(rotation=45)
plt.xlabel('Director')
plt.ylabel('Average Gross Earnings')
plt.title('Top 10 Directors by Average Gross Earnings')
plt.savefig('Top_10_Directors_by_Average_Gross_Earnings.png')
plt.show()

#insight:The bar graph shows Anthony Russo as the director with the highest average gross earnings.

# Count the occurrences of each genre per year
genre_year_counts = df.groupby(['Released_Year', 'Main_Genre']).size().reset_index(name='Count')

# Plotting genre popularity over the years
plt.figure(figsize=(12, 8))
sns.lineplot(x='Released_Year', y='Count', hue='Main_Genre', data=genre_year_counts, palette='Set2')
plt.xlabel('Released Year')
plt.ylabel('Number of Movies')
plt.title('Genre Popularity Over the Years')
plt.legend(title='Main Genre', loc='upper right', bbox_to_anchor=(1.2, 1))
plt.savefig('genre_popularity_over_years.png')
plt.show()

#Insight:The line graph indicates a trend of varying popularity for different film genres over time, with one genre peaking around 2013

# Plot a histogram of the IMDB ratings
plt.figure(figsize=(10,6)) # Set the figure size
plt.hist(df['IMDB_Rating'], bins=20, color='green') # Plot the histogram with 20 bins and green color
plt.xlabel('IMDB Rating') # Set the x-axis label
plt.ylabel('Frequency') # Set the y-axis label
plt.title('Histogram of IMDB Ratings') # Set the title
plt.savefig('Histogram_of_IMDB_Ratings.png')
plt.show() # Show the plot

# Insight: The IMDB ratings are skewed to the right, with most movies having ratings between 7 and 8.

# Plot a boxplot of the runtime
plt.figure(figsize=(10,6)) # Set the figure size
sns.boxplot(x=df['Runtime'], color='orange') # Plot the boxplot with orange color
plt.xlabel('Runtime (minutes)') # Set the x-axis label
plt.title('Boxplot of Runtime') # Set the title
plt.savefig('Boxplot_of_Runtime.png')
plt.show() # Show the plot

# Insight: The median runtime is around 120 minutes, with some outliers above 200 minutes.

# Plot a scatterplot of the gross earnings vs the IMDB ratings
plt.figure(figsize=(10,6)) # Set the figure size
sns.scatterplot(x=df['Gross'], y=df['IMDB_Rating'], color='blue') # Plot the scatterplot with blue color
plt.xlabel('Gross Earnings (USD)') # Set the x-axis label
plt.ylabel('IMDB Rating') # Set the y-axis label
plt.title('Scatterplot of Gross Earnings vs IMDB Ratings') # Set the title
plt.savefig('scatterplot_of_GE_vs_rating.png')
plt.show() # Show the plot

# Correlation matrix including IMDB ratings and gross earnings
correlation_matrix_extended = df[['IMDB_Rating', 'Gross']].corr()

# Heatmap of the extended correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix_extended, annot=True, cmap='coolwarm')
plt.title('Extended Heatmap of Correlation Matrix (IMDB Rating, Gross Earnings)')
plt.savefig('CM_GE_vs_rating.png')
plt.show()

# Insight: There is no clear correlation between the gross earnings and the IMDB ratings.

# Scatterplot of Runtime vs. IMDB Ratings
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Runtime', y='IMDB_Rating', data=df, color='green')
plt.xlabel('Runtime (minutes)')
plt.ylabel('IMDB Rating')
plt.title('Scatterplot of Runtime vs. IMDB Ratings')
plt.savefig('SP_runtime_vs_rating.png')
plt.show()

# Scatterplot of Runtime vs. Gross Earnings
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Runtime', y='Gross', data=df, color='orange')
plt.xlabel('Runtime (minutes)')
plt.ylabel('Gross Earnings')
plt.title('Scatterplot of Runtime vs. Gross Earnings')
plt.savefig('SP_runtime_vs_GE.png')
plt.show()


# Plot a bar chart of the average IMDB ratings by certificate
plt.figure(figsize=(10,6)) # Set the figure size
sns.barplot(x=df['Certificate'], y=df['IMDB_Rating'], color='red') # Plot the bar chart with red color
plt.xlabel('Certificate') # Set the x-axis label
plt.ylabel('Average IMDB Rating') # Set the y-axis label
plt.title('Bar Chart of Average IMDB Ratings by Certificate') # Set the title
plt.savefig('Average_IMDB_Ratings_by_Certificate.png')
plt.show() # Show the plot

# Insight: The movies with certificate A have the highest average IMDB rating, followed by U/A and U.

# Plot a pie chart of the main genre distribution
plt.figure(figsize=(10,6)) # Set the figure size
df['Main_Genre'].value_counts().plot.pie(autopct='%1.1f%%') # Plot the pie chart with percentage labels
plt.title('Pie Chart of Main Genre Distribution') # Set the title
plt.savefig('Pie_Chart_of_Main_Genre_Distribution.png')
plt.show() # Show the plot

# Insight: The most common main genre is Drama, followed by Action and Comedy.

# Count the number of movies per year
movies_per_year = df.groupby('Released_Year')['Series_Title'].count().reset_index()

# Plot a line chart of the number of movies released by year
plt.figure(figsize=(10,6))
sns.lineplot(x='Released_Year', y='Series_Title', data=movies_per_year, color='purple')
plt.xlabel('Released Year')
plt.ylabel('Number of Movies')
plt.title('Line Chart of Number of Movies Released by Year')
plt.savefig('Line_Chart_of_Number_of_Movies_Released_by_Year.png')
plt.show()

# Insight: The number of movies released has increased over the years, with a peak in 2016.

# Select only the numerical columns for the correlation matrix
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Compute the correlation matrix using only numerical columns
correlation_matrix = df[numerical_columns].corr()

# Plot a heatmap of the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.savefig('Heatmap_of_Correlation_Matrix.png')
plt.show()


# Insight: The strongest positive correlation is between the gross earnings and the number of votes, while the strongest negative correlation is between the meta score and the runtime.

# Plot a violin plot of the runtime by main genre
plt.figure(figsize=(10,6)) # Set the figure size
sns.violinplot(x=df['Main_Genre'], y=df['Runtime'], color='pink') # Plot the violin plot with pink color
plt.xlabel('Main Genre') # Set the x-axis label
plt.ylabel('Runtime (minutes)') # Set the y-axis label
plt.title('Violin Plot of Runtime by Main Genre') # Set the title
plt.savefig('Violin_Plot_of_Runtime_by_Main_Genre.png')
plt.show() # Show the plot

# Insight: The main genres with the longest runtime are Biography and Adventure, while the shortest are Comedy and Horror.

# Plot a pair plot of the numerical columns
# Select only the numerical columns for the pair plot
numerical_column = df.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(10,6)) # Set the figure size
sns.pairplot(numerical_column) # Plot the pair plot
plt.title('Pair plot of the numerical columns') # Set the title
plt.savefig('pair_plot_of_the_numerical_columns.png')
plt.show() # Show the plot

# Insight: The pair plot shows the distribution and the relationship of the numerical columns.

# Plot a count plot of the number of movies by decade
plt.figure(figsize=(10,6)) # Set the figure size
sns.countplot(x=df['Decade'], color='yellow') # Plot the count plot with yellow color
plt.xlabel('Decade') # Set the x-axis label
plt.ylabel('Number of Movies') # Set the y-axis label
plt.title('Count Plot of Number of Movies by Decade') # Set the title
plt.savefig('Count_Plot_of_Number_of_Movies_by_Decade.png')
plt.show() # Show the plot

# Insight: The decade with the most movies is 2010s, followed by 2000s and 1990s.

# Plot a joint plot of the gross earnings and the IMDB ratings
plt.figure(figsize=(10,6)) # Set the figure size
sns.jointplot(x=df['Gross'], y=df['IMDB_Rating'], color='cyan') # Plot the joint plot with cyan color
plt.xlabel('Gross Earnings (USD)') # Set the x-axis label
plt.ylabel('IMDB Rating') # Set the y-axis label
plt.title('Joint plot of the gross earnings and the IMDB ratings') # Set the title
plt.savefig('joint_plot_of_the_gross_earnings_and_the_IMDB_ratings.png')
plt.show() # Show the plot

# Insight: The joint plot shows the distribution and the relationship of the gross earnings and the IMDB ratings.

# Plot a boxplot of the IMDB ratings by main genre
plt.figure(figsize=(10,6)) # Set the figure size
sns.boxplot(x=df['Main_Genre'], y=df['IMDB_Rating'], color='magenta') # Plot the boxplot with magenta color
plt.xlabel('Main Genre') # Set the x-axis label
plt.ylabel('IMDB Rating') # Set the y-axis label
plt.title('Boxplot of IMDB Ratings by Main Genre') # Set the title
plt.savefig('Boxplot_of_IMDB_Ratings_by_Main_Genre.png')
plt.show() # Show the plot

# Plotting the counts
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values, color='green')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.title('Bar Chart of Genre Counts')
plt.xticks(rotation=45)
plt.savefig('Bar_Chart_of_Genre_Counts.png')
plt.show()
# Insight: The most frequent genre is Drama, followed by Adventure and Action.


# Explode the genres and plot a pie chart for distribution
genre_distribution = df['Genre'].str.split(',').explode().value_counts()

plt.figure(figsize=(10, 6))
genre_distribution.plot.pie(autopct='%1.1f%%')
plt.title('Genre Distribution')
plt.ylabel('')
plt.savefig('Genre_Distribution.png')
plt.show()

#Insight:The pie chart shows Drama, Comedy, and Action as the most prevalent film genres, with Drama leading at 17.1%.

# Create a 3D bar plot with matplotlib
# Create a figure and 3D subplot
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Discretize or categorize the data to define bars
x_data = df['Gross'] // 100000  # Example: Discretizing Gross by dividing to create bar categories
y_data = df['IMDB_Rating'] // 1  # Example: Discretizing IMDB_Rating (rounding to the nearest whole number)
z_data = df['Meta_score'] // 10  # Example: Discretizing Meta_score

# Count occurrences for each combination of categories
data_count = df.groupby([x_data, y_data, z_data]).size().reset_index(name='Count')

# Define bar dimensions
dx = dy = dz = 1  # Width, depth, and height of bars

# Create 3D bars
ax.bar3d(data_count['Gross'], data_count['IMDB_Rating'], data_count['Meta_score'], dx, dy, data_count['Count'], color='skyblue')

# Set labels and title
ax.set_xlabel('Gross Category')
ax.set_ylabel('IMDB Rating Category')
ax.set_zlabel('Meta Score Category')
ax.set_title('3D Bar Plot of Gross Earnings, IMDB Ratings, and Meta Score')

# Save the plot
plt.savefig('3D_Bar_Plot_of_Gross_Earnings_IMDB_Ratings_and_Meta_Score.png')
plt.show()

#Insight: movies that earn more tend to have higher ratings and scores.