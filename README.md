# GPMDP Song Info
Python 3 script for automatic refreshing of song information according to what is now playing. It can be used in OBS or other broadcasting software.
## Dependencies
This script needs [Python 3](https://www.python.org) and [Websockets](https://websockets.readthedocs.io/en/stable/) installed.
## Usage
`song_refresher.py outputFile outputImageFile`
## What it does
It listens to webserver created by GPMDP and refreshes song info into two files. First is text file containing artist and song name which looks like this:  
`The Weeknd - The Hills`  
Second one is image downloaded from albumArt url.
