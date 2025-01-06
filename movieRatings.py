

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from movie_FileLink import movie_Path

df = pd.read_csv(movie_Path)

# Average ratings on the basis og Genre
sns.lineplot(x="genre",y="score",data=df)
plt.show()