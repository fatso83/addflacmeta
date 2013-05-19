#!/usr/bin/python

import sys,mutagen
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC

if len(sys.argv) < 2:
	print "Usage: ",sys.argv[0], "filename.flac",\
			"\nWill parse any id3 info in the file and add it as FLAC meta information"
	exit(1)

filename=sys.argv[1]

if not filename.endswith(".flac"):
	print "This program is strictly intended for use with flac files"
	exit(1)

try:
	audio = EasyID3(filename)
except mutagen.id3.ID3NoHeaderError:
	print "No ID3 information found in",filename,"Exiting ..."
	exit(1)

flacinfo = FLAC(filename)

if flacinfo.tags:
	print "This program already has flac information. Skipping ..."
	exit(0)

title=audio["title"] 
album=audio["album"] 
artist=audio["artist"] 
track=audio["tracknumber"] 
genre=audio["genre"]
date=audio["date"]
#Not supported by EasyID3
#comment=audio["comment"]

# Keep for later?
#audio.delete()

#lagre som flacformat
flacinfo['artist'] = artist
flacinfo['title'] = title
flacinfo['album'] = album
#flacinfo['comment'] = comment
flacinfo['date'] = date 
flacinfo['tracknumber'] = track
flacinfo['genre'] = genre
flacinfo.save()
