Quicktime/MP4 rotation tool
============================
.. image:: https://badge.fury.io/py/qtrotate.svg
    :target: https://badge.fury.io/py/qtrotate
Tool to read or change a new rotation meta of mp4 (Quicktime) files (e.g. from iphones and similar). 

Installation
------------
.. code-block:: bash

   $ pip install qtrotate

Quickstart
------------
.. code-block:: python

   import qtrotate
   rotation = qtrotate.get_set_rotation(file_path)

From terminal
------------
.. code-block:: bash

   $ ./qtrotate.py myfile.mp4  # Read rotation from mp4
   90
   $ ./qtrotate.py myfile2.mp4 -90 # Set rotation
   $ ./qtrotate.py myfile2.mp4
   270
