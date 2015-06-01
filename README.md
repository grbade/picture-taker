#Description
This module takes a picture with the camera attached to a rasperry pi and saves
the picture in the archive folder which is in the same folder as the script.

#Usage
The script is executable and can be used directly

#Example
```
$ ./take_picture.py
```
or as a cronjob
```
0 *   * * *   root    /opt/camera/take_picture.py
```

#Note
In order to use the module you need to install:

* picamera

