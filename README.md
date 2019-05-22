# Face Tracker

This program utilize a Raspberry Pi face/object tracking.

It does so by using the Raspi-Cam for face/object detection and two servoes for moving in the x and y plane.


## Installing

Once your Raspberry is up and running.

```bash
   sudo apt-get update
   sudo apt-get upgrade
```

```bash
   cd ~
   git clone https://github.com/magnusoy/Face-Tracker.git
```

```bash
   sudo apt-get install build-essential cmake unzip pkg-config
   sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
   sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
   sudo apt-get install libxvidcore-dev libx264-dev
   sudo apt-get install libgtk-3-dev
   sudo apt-get install libcanberra-gtk*
   sudo apt-get install libatlas-base-dev gfortran
   sudo apt-get install python3-dev
```

```bash
   cd Face-Tracker
   sudo pip3 install -r requirements.txt
```


## Setup

Only nessecary for object tracking. Since its based on HSV settings.


```bash
   cd ~
   cd Face-Tracker/src/
   python3 morphological_transformation.py
```
Change the slideres until you have successfully isolated your object with white space

in the dilation frame.

Write down the numbers, and change the self.lower_color and self.upper_color lists in

the color_tracking.py file.


## Usage

```bash
   cd ~
   cd Face-Tracker/src/
   python3 app.py
```
or 

```bash
   cd ~
   cd Face-Tracker/src/
   python3 app_color.py
```


## Built With

* [Python](https://www.python.org/) - Python


## Contributing

If you want to contribute or find anything wrong, please create a Pull request, or issue addressing the change, or issue.


## Author

* **Magnus Øye** - [magnusoy](https://github.com/magnusoy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/magnusoy/SelfBalancingRobot/blob/master/LICENSE) file for details.


## Libraries

[Pyserial](https://pythonhosted.org/pyserial/)

[OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

[Adafruit Servokit](https://circuitpython.readthedocs.io/projects/servokit/en/latest/)
