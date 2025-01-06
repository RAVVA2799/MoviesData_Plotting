
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from movie_FileLink import movie_Path  # Assuming FILE_PATH is stored in config.py

# Load the dataset
df = pd.read_csv(movie_Path)

# Count occurrences of each genre
genre_counts = df['genre'].value_counts()

# Define custom colors for each bar
colors = sns.color_palette("hsv", len(genre_counts))  # or use your own list of colors

# Plot the bar graph with different colors
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette=colors)
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.title("Number of Movies by Genre")
plt.xticks(rotation=45)

# Adding value annotations on top of each bar
for index, value in enumerate(genre_counts.values):
    plt.text(index, value + 0.5, str(value), ha='center', color='black')

plt.show()
