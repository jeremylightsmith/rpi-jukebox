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
* [HDMI -> Audio converter](http://www.amazon.com/Female-Adapter-Converter-Projector-Notebook/dp/B00IVD019I/ref=sr_1_7?ie=UTF8&qid=1442168128&sr=8-7&keywords=hdmi+to+audio) the audio output on the pi sucks, but HDMI audio is supposed to be better?

Installation
============

Setup WiFi
----------

According to [this](https://techblog.willshouse.com/2013/06/11/solved-raspbian-with-edimax-ew-7811un-wifi-adapter-and-802-1x-authentication/)

You should now be able to ssh into your raspberry pi.

Update Software & Pull Libraries
--------------------------------

Run this:

    sudo apt-get update
    sudo apt-get install build-essential python-dev git

Mount the USB Flash Drive
-------------------------

create the mount

    cd /mnt
    sudo mkdir bigdaddy
    sudo mount -o uid=pi,gid=pi /dev/sda1 /mnt/bigdaddy
    sudo vi /etc/fstab

        add this line:
        /dev/sda1 /mnt/bigdaddy vfat uid=pi,gid=pi,umask=0022,sync,auto,nosuid,rw,nouser 0 0

Try it out, you should see everything on the flash drive under /mnt/bigdaddy

Setting Up Audio
----------------

<!-- For MP3, read this:

https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/install-python-module-rpi-dot-gpio

Run this: 

    sudo apt-get install alsa-utils mpg123

Reboot:

    sudo reboot

Setup the audio port:

    sudo modprobe snd_bcm2835
    sudo amixer cset numid=3 1


install mpd & mpc
    sudo apt-get alsa-utils mpd mpc
    sudo modprobe snd_bcm2835
    sudo nano /etc/mpd.conf
 -->

Downloading our software
------------------------

create an ssh key

    ssh-keygen

add your public key as a deploy key in the project

    git clone git@github.com:jeremylightsmith/rpi-jukebox.git

Setting up the NFC Card
-----------------------

enable spi 

    sudo raspi-config

sudo vi /etc/modprobe.d/raspi-blacklist.conf

*New* : https://github.com/mxgxw/MFRC522-python

Install SPI-Py

    cd ~
    git clone git@github.com:lthiery/SPI-Py.git
    cd SPI-Py
    sudo python setup.py install

    cd ~
    git clone https://github.com/mxgxw/MFRC522-python.git
    cd MFRC522-python
    sudo python Read.py



or

    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.35.tar.gz
    tar -zxf bcm2835-1.35.tar.gz
    cd bcm2835-1.35
    ./configure
    sudo make install

then

    cd ~
    sudo apt-get install subversion
    svn checkout http://rpi-rc522.googlecode.com/svn/trunk/ rpi-rc522-read-only
    cd rpi-rc522-read-only/rc522
    gcc config.c rfid.c rc522.c main.c -o rc522_reader -lbcm2835
    sudo cp RC522.conf /etc/
    ./rc522_reader -d





I followed this to hookup the nfc thing:

https://learn.adafruit.com/raspberry-pi-nfc-minecraft-blocks/library-installation

Run this:

    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_PN532.git
    cd Adafruit_Python_PN532
    sudo python setup.py install

Run this:

    cd examples
    sudo python readmifare.py


