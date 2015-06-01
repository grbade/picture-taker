#!/usr/bin/python
"""take_picture.py

This module takes a picture with the camera attached to a rasperry pi and saves
the picture in the archive folder which is in the same folder as the script.

The script is executable and can be used directly

Example:
      $ ./take_picture.py

      or as a cronjob

      0 *   * * *   root    /opt/camera/take_picture.py

Note:
    In order to use the module you need to install:
    picamera
"""


import picamera
from datetime import datetime

def take_picture():
    """The picture recording

    The function takes the picture and saves it in the archives folder. The
    filename is the time it was takes.

    Example:
        201506011853 = 2015/06/01 18:53

    Args:
        None

    Returns:
        None

    """
    camera = picamera.PiCamera()
    camera.capture('/opt/camera/archive/%s.jpg' % 
            datetime.utcnow().strftime("%Y%m%d%H"))

if __name__ == "__main__":
    take_picture()
