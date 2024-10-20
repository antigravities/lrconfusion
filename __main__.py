import os
from plexapi.server import PlexServer

plex = PlexServer(os.getenv("PLEX_SERVER"), os.getenv("PLEX_TOKEN"))

removing = False

items = []

for playlist in plex.playlists():
    if playlist.title == os.getenv("PLEX_PLAYLIST"):
        for item in playlist.items():
            if removing:
                items.append(item)

            if item.title == os.getenv("PLEX_STOP_AT"):
                removing = True
        
        if removing:
            print(f"Removing {len(items)} items from playlist. Are you sure? (y/n)")
            answer = input()

            if answer == "y":
                playlist.removeItems(items)
                print("Items removed.")

