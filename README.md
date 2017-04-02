What is this?
=============

My wife is a Montessori teacher, and didn't want screens to be a part of his life until 6 years old. I wanted him to be able to choose his own music and play it as much as he wanted. This jukebox lets him do that without screens.

He just holds the card with the picture of the song/album near the jukebox and it starts playing...

Magic!

Kit
===

This is still evolving, the last evolution was:

* [Raspberry Pi 3 + Case / Power](https://www.amazon.com/gp/product/B01C6EQNNK/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1) $50
* [USB Mifare Card Reader](https://www.amazon.com/gp/product/B00BYKPHSU/ref=oh_aui_detailpage_o05_s01?ie=UTF8&psc=1) $16
* [SD Card](http://www.amazon.com/gp/product/B00M55C0LK?psc=1&redirect=true&ref_=oh_aui_detailpage_o07_s00) $11
* [USB Flash Drive](http://www.amazon.com/gp/product/B005FYNSZA?psc=1&redirect=true&ref_=oh_aui_detailpage_o08_s00) $8
* [Mifare RFID cards](https://www.amazon.com/gp/product/B01HC5XHH8/ref=oh_aui_detailpage_o04_s00?ie=UTF8&psc=1) $40
* [Card protector sleeves](http://www.amazon.com/gp/product/B00B7TUIFA?psc=1&redirect=true&ref_=oh_aui_detailpage_o04_s00) $7
* [Mini Remote Control](http://www.amazon.com/gp/product/B00RBGB91K?psc=1&redirect=true&ref_=oh_aui_detailpage_o03_s00) $13
* [Mini USB Cables](http://www.amazon.com/gp/product/B007NLW3C2?psc=1&redirect=true&ref_=oh_aui_detailpage_o02_s00) $9

=> $154

Installation
============

Install Raspbian on the Pi
-------------------------

# Install NOOBS (https://www.raspberrypi.org/documentation/installation/noobs.md)
# Choose Raspbian
# Setup your wifi (top right)
# Update configuration
    - top left Raspberry > Preferences > Raspberry Pi Configuration
    - boot: To CLI
# Reboot

Preparing your music
--------------------

The structure for the USB Flash Drive is:

    music/
        1-my song.mp3
        2-my other song.mp3
        3-my album/
            first album song.mp3
            second album song.mp3
    sounds/
        i_am_listening.mp3
        repeating_on.mp3
        repeating_off.mp3
    cards.txt

You can copy the sounds directory from this repository. And the cards.txt file will get generated for you.

You have to populate with music directory. All that's important is that every file or directory starts with a distinct number then dash.

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

Update Software & Pull Libraries
--------------------------------

Run this:

    sudo apt-get update
    sudo apt-get install build-essential python-dev git

Setting Up Audio
----------------

Run this: 

    sudo apt-get install alsa-utils mpg123

Reboot:

    sudo reboot

Setup the audio port:

    sudo modprobe snd-bcm2835
    sudo amixer cset numid=3 1

Turn up the volume:

    amixer set PCM -- -0000

Downloading our software
------------------------

create an ssh key

    ssh-keygen

add your public key as a deploy key in the project

    git clone https://github.com/jeremylightsmith/rpi-jukebox.git jukebox

try it by

    jukebox/bin/jukebox

Start on boot
-------------

    sudo vi /etc/rc.local

add this line:

    /home/pi/jukebox/bin/jukebox &
