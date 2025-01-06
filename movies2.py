
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from movie_FileLink import movie_Path
df = pd.read_csv(movie_Path)

# plt.show()
df = df.drop(['rating'], axis=1)  # Drop rating column as in the original pairplot

# Select the first 200 rows to limit data if needed
df = df[:200]

# List of columns for pairwise plotting
columns = df.columns.difference(['genre'])  # Exclude 'genre' if it's categorical

# Create a grid of subplots for pairwise plots
fig, axes = plt.subplots(len(columns), len(columns), figsize=(20, 20))
plt.subplots_adjust(hspace=0.5, wspace=0.5)

# Plot each pair
for i, col_x in enumerate(columns):
    for j, col_y in enumerate(columns):
        if i == j:
            # Diagonal: histogram
            sns.histplot(df[col_x], ax=axes[i, j], kde=True)
        else:
            # Off-diagonal: bar plot of col_x vs. col_y
            sns.barplot(x=col_x, y=col_y, hue="genre", data=df, ax=axes[i, j], errorbar=None)

plt.show()