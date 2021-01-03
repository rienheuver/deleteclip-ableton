# deleteclip-ableton
A simple remote script for ableton to delete the currently selected clip

## CREDITS
All credits go to rynhardt from this thread: https://forum.ableton.com/viewtopic.php?f=4&t=235724

## Usage
By default, this will delete the active clip if you send midi note 39 on channel 8. I had a hard time finding that note and channel, so if you do as well, copy the contents from SearchNote.py to DeleteClip.py. Then hit the note you want to use, and check the logs in `C:\Users\<username>\AppData\Roaming\Ableton\Live 10.1.30\Preferences\Log.txt`
I didn't properly test SearchNote.py since I kinda built something like that along the way, but it should at least be more or less working ;-).
