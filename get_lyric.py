## foo_genius
## Written by zyme-xd on Github
import lyricsgenius
from dotenv import load_dotenv
import os
import sys
import re

load_dotenv(".env")
g = lyricsgenius.Genius(os.getenv("APIKEY")) # Puts it in a secure place
g.verbose = False
artist = g.search_artist(sys.argv[4], max_songs=1, sort="title")
track = g.search_song(sys.argv[2], artist.name, get_full_info=True)

if artist is None:
    quit()
if track is None:
    quit() 
else:
    result = re.sub('^(.+Lyrics)', "", track.lyrics)
    result = re.sub('(\d.+Embed)$', "", track.lyrics)
    print(result)
    