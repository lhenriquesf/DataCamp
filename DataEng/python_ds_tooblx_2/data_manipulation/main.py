#%%
import pandas as pd
netflix_df = pd.read_csv('../netflix_data.csv', index_col=0)

netflix_subset = netflix_df[netflix_df['type']=='Movie']
netflix_movies = netflix_subset[['title','genre','duration','director','country']]

netflix_movies_genre_agg = netflix_movies.groupby('genre')['duration'].sum()

# %%
print(len(netflix_movies_genre_agg))
shortest_movies = netflix_movies[netflix_movies['duration']<10]
# %%
s= netflix_movies['duration'].agg(sum)
# %%
total = netflix_movies_genre_agg/sum(netflix_movies_genre_agg)
# %%
