import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from movie_FileLink import movie_Path

df = pd.read_csv(movie_Path)

# Count occurrences of each genre upto 500 values
genre_counts = df[:400]['genre'].value_counts()

# Define custom colors for the pie chart
colors = sns.color_palette("hsv", len(genre_counts))  # or use your own list of colors

# Plot a pie chart
plt.figure(figsize=(10, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, 
        wedgeprops={'edgecolor': 'black'}, textprops={'fontsize': 10})

# Adding a legend to the right side for the number of movies in each genre
plt.legend(
    [f"{genre}: {count} movies" for genre, count in zip(genre_counts.index, genre_counts.values)],
    title="Genre Counts",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

plt.title("Percentage Distribution of 1st 400 Movies by Genre")
plt.show()
