#!/usr/bin/python
# Changes track and disc entries on the form "3/12" to "3"
import sys,mutagen,re
from mutagen.flac import FLAC

filename=sys.argv[1]
flacinfo = FLAC(filename)

tracknumber = flacinfo['tracknumber']
new_track = re.sub('/..','',tracknumber[0],1)
flacinfo['tracknumber'] = new_track

discnumber = flacinfo['discnumber']
new_disc = re.sub('/..','',discnumber[0],1)
flacinfo['discnumber'] = new_disc
flacinfo.save()
