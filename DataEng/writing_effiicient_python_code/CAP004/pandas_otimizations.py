#%%
import numpy as np
import pandas as pd

baseball_df = pd.read_csv('baseball_stats.csv')

def calc_run_diff(runs_scored,runs_allowed):
    run_diff = runs_scored-runs_allowed
    return run_diff

def calc_win_perc(wins, games_played):
    win_perc = wins/games_played
    return np.round(win_perc,2)
#%%
run_diff_apply = baseball_df.apply(
    lambda row: calc_run_diff(row['RS'],row['RA']),
    axis=1
)

wins_perc_apply = baseball_df.apply(
    lambda row2: calc_win_perc(row2['W'], row2['G']),
    axis=1
)

baseball_df['RD'] = run_diff_apply
baseball_df['WP'] = wins_perc_apply

#%%
baseball_df['RD'] = baseball_df['RS'].values - baseball_df['RA'].values