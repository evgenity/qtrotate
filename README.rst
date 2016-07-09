Quicktime/MP4 Rotation Tools
============================
Tools to work with rotated Quicktime/MP4 files. Currently this consists of a tool to detect and return the rotation angle if one can be found. Once known, you can use the info to rotate the video using MEncoder's rotate filter, AviSynth, etc. You can also write a new rotation angle into the files. 

NOTE that translation info will be LOST if a new rotation angle is written.


Patches and new tools welcome.

Installation
------------
    $ pip install qtrotate

Simple Usage
------------
The script is usable as both a Python library and a standalone script:

    $ ./qtrotate.py myfile.mp4
    90

    $ ./qtrotate.py myfile2.mp4 -90
    $ ./qtrotate.py myfile2.mp4
    270
