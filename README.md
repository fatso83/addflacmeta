ID3 to FLAC comments
====================
This program removes id3 tags and adds the info as real meta flac info. It does not (as of today) remove the original id3 info, as future versions might copy more information than the basic info it does today.

##Usage:
id3_to_flac_comments.py my_track.flac

##Prerequisites
- The python library <code>mutagen</code>
Can be installed through PIP: <code>sudo pip install mutagen</code>
- Make the script executable by chmod +x id3_to_flac_comments.py
