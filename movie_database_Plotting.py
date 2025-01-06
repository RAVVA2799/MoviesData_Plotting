
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


movie_Path="C:/Users/Microsoft/OneDrive/Desktop/pythonAssignments/movieDataBase/movies_updated.csv"
df = pd.read_csv(movie_Path)

print(df)

#VIOLIN PLOT
# Violin Plot on the basis of different Genre movies per Year

sns.violinplot(y="genre",x="year",data=df)
plt.show()

#PAIR PLOT
# Pair Plot on the basis of Different Genre Movies

sns.pairplot(df.drop(['rating'],axis=1),hue="genre")
plt.show()

# LINE PLOT
# Average ratings on the basis og Genre 

sns.lineplot(x="genre",y="score",data=df)
plt.show()


# BAR GRAPH
# Count occurrences of each Country upto 1000 values
country_counts = df[:1000]['country'].value_counts()
colors = sns.color_palette("hsv", len(country_counts))  # or use your own list of colors

# Plot the bar graph with different colors
plt.figure(figsize=(10, 6))
sns.barplot(x=country_counts.index, y=country_counts.values, palette=colors)
plt.xlabel("Country")
plt.ylabel("Number of Movies")
plt.title("Number of Movies by country of origin")
plt.xticks(rotation=45)

# Adding value annotations on top of each bar
for index, value in enumerate(country_counts.values):
    plt.text(index, value + 0.5, str(value), ha='center', color='black')

plt.show()


# BAR GRAPH 2
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



# PIE CHART
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