#%%
# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#%%
# Start coding!
csv_file = 'netflix_data.csv'
netflix_df = pd.read_csv(csv_file, index_col=0)
netflix_subset = netflix_df[netflix_df['type'] != 'TV Show']

netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

short_movies = netflix_movies[netflix_movies["duration"] < 60]

genre_color_map = {
    'Children': 'Yellow',
    'Documentaries': 'Blue',
    'Stand-Up': 'Green'
}

colors = [genre_color_map[row['genre']] if row['genre'] in genre_color_map else 'Red' for _, row in netflix_movies.iterrows()]

fig = plt.figure()

plt.scatter(x=netflix_movies['release_year'], y=netflix_movies['duration'], c=colors, alpha=0.5)
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.show()