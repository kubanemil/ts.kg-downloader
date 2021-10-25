from ts_kg import *
import os

for show in shows_link_list():
    print(show)
    if new_episode(show):
        download_episode(new_episode(show))
        print('downloaded')
        add_one_watched(new_episode(show))
    else:
        print('No new episodes')
