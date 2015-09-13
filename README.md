What is this?
=============

My wife is a Montessori teacher, and didn't want screens to be a part of his life until 6 years old. I wanted him to be able to choose his own music and play it as much as he wanted. This jukebox lets him do that without screens.

He just holds the card with the picture of the song/album near the jukebox and it starts playing...

Magic!

Kit
===

This is still evolving, the last evolution was:

* [Raspberry Pi 2](http://www.amazon.com/gp/product/B00T2U7R7I?psc=1&redirect=true&ref_=oh_aui_detailpage_o07_s00)
* [NFC Card Reader](http://www.amazon.com/gp/product/B00E0ODLWQ?psc=1&redirect=true&ref_=oh_aui_detailpage_o07_s00)
* [Wi-Fi USB Adapter](http://www.amazon.com/gp/product/B003MTTJOY?psc=1&redirect=true&ref_=oh_aui_detailpage_o07_s00)
* [SD Card](http://www.amazon.com/gp/product/B00M55C0LK?psc=1&redirect=true&ref_=oh_aui_detailpage_o07_s00)
* [USB Flash Drive](http://www.amazon.com/gp/product/B005FYNSZA?psc=1&redirect=true&ref_=oh_aui_detailpage_o08_s00)
* [Jumper Cables](http://www.amazon.com/gp/product/B00D7SCMZ8?psc=1&redirect=true&ref_=oh_aui_detailpage_o08_s00)
* [CY Case for Raspberry Pi](http://www.amazon.com/gp/product/B00P2V8ZGI?psc=1&redirect=true&ref_=oh_aui_detailpage_o02_s00)
* [Mifare RFID cards](http://www.amazon.com/gp/product/B00NN6UTKY?psc=1&redirect=true&ref_=oh_aui_detailpage_o06_s00)
* [Card protector sleeves](http://www.amazon.com/gp/product/B00B7TUIFA?psc=1&redirect=true&ref_=oh_aui_detailpage_o04_s00)

Installation
============

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

create the mount

    cd /mnt
    sudo mkdir music
    sudo mount -o uid=pi,gid=pi /dev/sda1 /mnt/music
    sudo vi /etc/fstab

        add this line:
        /dev/sda1 /mnt/music vfat uid=pi,gid=pi,umask=0022,sync,auto,nosuid,rw,nouser 0 0

install mpd & mpc
    sudo apt-get alsa-utils mpd mpc
    sudo modprobe snd_bcm2835
    sudo nano /etc/mpd.conf
