Quicktime/MP4 Rotation Tools (IPhone, Android)
============================
Tool to work with **rotated** Quicktime/MP4 files (e.g. from iphones and similar).
Tool can **read rotation angle** and **set new rotation angle**.

Installation
------------
    $ pip install qtrotate

Quickstart
------------
    import qtrotate
    rotation = qtrotate.get_set_rotation(file_path)

From console
------------
    $ ./qtrotate.py myfile.mp4  # Read rotation from mp4
    
    90

    $ ./qtrotate.py myfile2.mp4 -90
    
    $ ./qtrotate.py myfile2.mp4
    
    270
