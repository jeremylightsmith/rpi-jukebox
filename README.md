What is this?
=============

My wife is a Montessori teacher, and didn't want screens to be a part of his life until 6 years old. I wanted him to be able to choose his own music and play it as much as he wanted. This jukebox lets him do that without screens.

He just holds the card with the picture of the song/album near the jukebox and it starts playing...

Magic!

Kit
===

This is still evolving, the last evolution was:

* [Raspberry Pi 2](http://www.amazon.com/gp/product/B00T2U7R7I?psc=1&redirect=true&ref_=oh_aui_detailpage_o07_s00) $39
* [USB NFC Card Reader](http://www.amazon.com/gp/product/B00BYKPHSU?psc=1&redirect=true&ref_=oh_aui_detailpage_o04_s00) $18
* [Wi-Fi USB Adapter](http://www.amazon.com/gp/product/B003MTTJOY?psc=1&redirect=true&ref_=oh_aui_detailpage_o07_s00) $9
* [SD Card](http://www.amazon.com/gp/product/B00M55C0LK?psc=1&redirect=true&ref_=oh_aui_detailpage_o07_s00) $11
* [USB Flash Drive](http://www.amazon.com/gp/product/B005FYNSZA?psc=1&redirect=true&ref_=oh_aui_detailpage_o08_s00) $8
* [Case for Raspberry Pi 2](http://www.amazon.com/Official-Raspberry-Pi-Foundation-Model/dp/B00ZW4RKFM/ref=pd_sim_147_11?ie=UTF8&dpID=21Vhd3vo7FL&dpSrc=sims&preST=_AC_UL160_SR160%2C160_&refRID=1ZKG2697ATZRSE53RKYA) $9
* [Mifare RFID cards](http://www.amazon.com/gp/product/B00NN6UTKY?psc=1&redirect=true&ref_=oh_aui_detailpage_o06_s00) $26
* [Card protector sleeves](http://www.amazon.com/gp/product/B00B7TUIFA?psc=1&redirect=true&ref_=oh_aui_detailpage_o04_s00) $7
* [Mini Remote Control](http://www.amazon.com/gp/product/B00RBGB91K?psc=1&redirect=true&ref_=oh_aui_detailpage_o03_s00) $13
* [Mini USB Cables](http://www.amazon.com/gp/product/B007NLW3C2?psc=1&redirect=true&ref_=oh_aui_detailpage_o02_s00) $9

=> $150

Installation
============

Setup WiFi
----------

According to [this](https://techblog.willshouse.com/2013/06/11/solved-raspbian-with-edimax-ew-7811un-wifi-adapter-and-802-1x-authentication/)

You should now be able to ssh into your raspberry pi.

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

Setting Up Audio
----------------

Run this: 

    sudo apt-get install alsa-utils mpg123

Reboot:

    sudo reboot

Setup the audio port:

    sudo modprobe snd_bcm2835
    sudo amixer cset numid=3 1

Turn up the volume:

    amixer set PCM -- -0000

Update Software & Pull Libraries
--------------------------------

Run this:

    sudo apt-get update
    sudo apt-get install build-essential python-dev git

Downloading our software
------------------------

create an ssh key

    ssh-keygen

add your public key as a deploy key in the project

    git clone https://github.com/jeremylightsmith/rpi-jukebox.git jukebox

try it by

    jukebox/bin/jukebox

<!-- 
sudo apt-get install python-dev python-pip gcc
sudo apt-get install linux-headers-$(uname -r)
 -->

Start on boot
-------------

    sudo vi /etc/rc.local

add this line:

    /home/pi/jukebox/bin/jukebox &
