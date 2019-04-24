# Face Tracker

This program utilize a Raspberry Pi and a Arduino for face tracking.

It does so by using the Raspi-Cam and a two servoes.


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

Use Arduino IDE to flash the bot.ino script over too the Arduino board.

Finally plug the USB to the Raspberry and find the connected port.

Then change the port in the Python script.

```bash
   cd ~
   cd Face-Tracker/src
   sudo nano app.py
```
Press CTRL + O and then ENTER to save.

Press CTRL + X to close.

## Usage

```bash
   cd ~
   cd Face-Tracker/
   sh run.sh
```


## Built With

* [Python](https://www.python.org/) - Python
* [Arduino](https://www.arduino.cc/) - Arduino


## Contributing

If you want to contribute or find anything wrong, please create a Pull request, or issue addressing the change, or issue.


## Author

* **Magnus Øye** - [magnusoy](https://github.com/magnusoy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/magnusoy/SelfBalancingRobot/blob/master/LICENSE) file for details.


## Libraries

[Pyserial](https://pythonhosted.org/pyserial/)

[OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
