= Installation

I followed this to hookup the nfc thing:

https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks/library-installation

Run this:

    sudo apt-get update
    sudo apt-get install build-essential python-dev git
    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_PN532.git
    cd Adafruit_Python_PN532
    sudo python setup.py install

Run this:

    cd examples
    sudo python readmifare.py

For MP3, read this:

https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/install-python-module-rpi-dot-gpio

Run this: 

    sudo apt-get install alsa-utils mpg123

Reboot:

    sudo reboot

Setup the audio port:

    sudo modprobe snd_bcm2835
    sudo amixer cset numid=3 1