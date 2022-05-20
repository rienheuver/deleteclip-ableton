# deleteclip-ableton

A simple remote script for ableton to delete the currently selected clip

## CREDITS

All credits go to rynhardt from this thread: https://forum.ableton.com/viewtopic.php?f=4&t=235724

## Usage

1. Create a directory called `DeleteClip` in `C:\ProgramData\Ableton\Live 10 Intro\Resources\MIDI Remote Scripts\`. On MacOS, this will be something like `/Applications/Ableton Live 11 Suite.app/Contents/App-Resources`
2. Put the files from this repository in that directory.
3. Reload/startup Ableton, go to Options > Preferences > Link MIDI. There find your midi-instrument and select DeleteClip as the Control Surface. For mine I have Track, Sync and Remote turned On, but rynhardt had his working with all turned off, so whatever you need I guess.
4. Enjoy!

By default, this will delete the active clip if you send midi note 39 on channel 8. I had a hard time finding that note and channel, so if you do as well, copy the contents from SearchNote.py to DeleteClip.py. Then hit the note you want to use, and check the logs in `C:\Users\<username>\AppData\Roaming\Ableton\Live 10.1.30\Preferences\Log.txt`.

Mac users, the logs are here `/Users/<username>/Library/Preferences/Ableton/Live\ 11.0.12/Log.txt`. A handy MacOS Terminal command for seeing the log output in realtime is `tail -f <path-to-log-file>`.

Last note, Python is sensitive about indentation -- they either all need to be spaces, or they all need to be tabs. If they are mixed, the script will throw.
