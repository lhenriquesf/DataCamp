#%%
import numpy as np

heroes = ['Batman', 'Superman', 'Wonder Woman']

hts = np.array([188.0, 191.0, 183.0])
wts = np.array([95.0, 101.0, 74.0])

def convert_unit_to_usa(heroes,heights,weights):
    new_hts = [round((ht * 0.39370),2) for ht in heights]
    new_wts = [round(wt * 2.20462),2) for wt in weights]

    hero_data = {}
    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
    return hero_data

converts = convert_unit_to_usa(heroes=heroes,heights=hts,weights=wts)
print(converts)
# %%
%load_ext line_profiler

%lprun -f convert_unit_to_usa convert_unit_to_usa(heroes,hts,wts)
# %%
def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes

#%%
def get_publisher_heroes_np(heroes, publishers, desired_publisher):

    heroes_np = np.array(heroes)
    pubs_np = np.array(publishers)

    desired_heroes = heroes_np[pubs_np == desired_publisher]

    return desired_heroes