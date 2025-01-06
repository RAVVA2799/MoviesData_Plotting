

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from movie_FileLink import movie_Path

df = pd.read_csv(movie_Path)
print(df)

# Pair Plot on the basis of Different Genre Movies
sns.pairplot(df.drop(['rating'],axis=1),hue="genre")

plt.show()
