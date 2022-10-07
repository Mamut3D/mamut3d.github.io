---
layout: post
title:  "PiZero backup server"
date:   2022-08-27 12:00:00 +0100
weight: 3
---

<!-- vim-markdown-toc GFM -->

* [The problem](#the-problem)
	* [Cloud storage](#cloud-storage)
	* [Local NAS](#local-nas)
* [The solution](#the-solution)
* [The summary](#the-summary)
* [2022.07.10 update](#20220710-update)

<!-- vim-markdown-toc -->

## The problem

For a long time, almost two decades now, I take care of my personal collection of photos which extends back approximately to year 2005. Last few years I was really not very happy with my setup. For a year or two I had a setup of two external hard drives, where I would store my photos. One copy on each hard drive. Currently one copy takes around 250GB of data.

I had one external drive in living room and one in my room to at least prevent some local accidents, but lets be honest, one flood/fire and years of my life are gone in a finger snap.

When I had discussions about this with my friends and colleagues it always came to the same solutions:

- Cloud storage
  - Google Drive/Pictures
  - Microsoft OneDrive
  - Azure S3 Glacier
- Local NAS

### Cloud storage

One thing I love about cloud is the data resiliency and ease of use with really easy access to your photos, search by object name, date etc. and sharing of your photos.

The things don't like about cloud services:

- They give you the illusion, that they backup your photos for you from your Mobile. But there are multiple photo applications which may store photos elsewhere on the device and thus may not end up in the backup. Plus you easily end up in a state where you just take photos and don't care. Filtering your photos is really necessary, or you end up with a heap of crap for which you end up paying and not using.
- Automatic backup to cloud services tend to change the format of your photos, which may end up in worse quality.
- You give access to your photos to Google learning algorithms or whatnot. Basically you don't know who is doing what with them.
- Cloud is a pay as you go service, so you have to pay yearly/monthly fee. God I hate regular payments. General rule of thumb is get as many regular payment's to you as you can and avoid as many from you to others ;-)

Pricing for my needs ~250GB:

- Google cloud is 100euro/year
  ![Google drive pricing 08.27.2022](/blog/2022-08-27-pizero-storage-server/googledrive.jpg)
- OneDrive is 70euro/year
  ![OneDrive pricing 08.27.2022](/blog/2022-08-27-pizero-storage-server/onedrive.jpg)

> [Azure S3 Glacier](https://aws.amazon.com/s3/storage-classes/glacier/) seems like a good fit. I am considering it now as a third locality. But I need to test it, mainly the data recovery process and price. From my basic calculations 250GB should cost ~5USD per year when using S3 Glacier Deep Archive which is more than reasonable. This [blog post](https://betterdev.blog/personal-backup-to-amazon-s3/) seems like a good starting point.

### Local NAS

Local NAS might be good fit for somebody who wants to share movies or photos around the house for other family members but I have dismissed the idea for the following reasons:

- It does not provide disaster resiliency over multiple localities, only local RAID.
- It requires personal LAN (I am on shared LAN with neighbours)
- It is expensive and another thing to take care of
- NAS shared over internet are regular targets for hackers and vendors typically provide short update life cycle


## The solution

![PiZero storage server](/blog/2022-08-27-pizero-storage-server/server.jpg)

I wanted to use my already owned unused resources:

  - 2 external [1TB hard drives](https://www.amazon.com/Elements-Portable-External-Drive-WDBUZG0010BBK-WESN/dp/B00CRZ2PRM)
    - Cost around 55USD so over three years, I am already beating the cloud pricing ;-)
  - Raspberry PiZero(w)
    - Costs around 20USD and it is leftover from my chicken door project
  - 5V power brick
    - Costs 0USD since it is a leftover from some older phone

I decided to setup a Raspberry server at my parents house with one of the HDDs attached for remote backup/archivation of my photos using `rsync` from my trusty Samsung S10 termux station :-).

The problems that I had to tackle along the route:

- My parents internet provider does not provide public IP (IPv4 nor IPv6).
  - I was not able to connect to my Pi from the Internet. Internet provider prices the public IP at 10euros/month ... Jeez...
  - The solution was to use some kind of VPN service. I have selected [ZeroTier One](https://www.zerotier.com). ZeroTier provides a free VPN for personal use for up to 25 devices and through [hole punching](https://en.wikipedia.org/wiki/UDP_hole_punching) gets around the no public IP issue. Also they have a client for the Pi and Android.
  ![ZeroTier pricing 08.27.2022](/blog/2022-08-27-pizero-storage-server/zerotier.jpg)
- power the external hard drive
  - Although the HDD was able to run from the Pi data port, after some time it stopped to work. I think it was due to some power spike or something.
  - The solution was to use [externally powered USB hub](https://www.alza.sk/axagon-hue-msa-switch-hub-usb-a-metal-d6588596.htm) for 15euro
    > The PiZero had some issues with the hubs I have originally bought with 3.0 USB support, so try to use some dummy 2.0 HUBs (PiZero has only USB2 ports anyway) or some newer USB3.1 HUBs.

- Power outages
  - sometimes there are power outages at my second locality, so far it seems that the PiZero boots all right after outage however it seems that it boots before the WiFi router. This in causes that Pi won't connect to the network and it is not accessible from the internet and requires manual restart. I am trying to tackle this with a Cron Job proposed [here](https://weworkweplay.com/play/rebooting-the-raspberry-pi-when-it-loses-wireless-connection-wifi/).

  ```bash
  #!/bin/bash

  # Try to ping the local router
  ping -c4 10.0.1.1 > /dev/null

  if [ $? != 0 ]
  then
    echo "wrecon start '$(date)'" >> /home/pi/wrecon_log
    echo "No network connection, restarting wlan0" >> /homr/pi/wrecon_log
    sudo zerotier-cli info >> /home/pi/wrecon_log
    /sbin/ifdown 'wlan0'
    sleep 5
    /sbin/ifup --force 'wlan0'
    sleep 5
    sudo zerotier-cli info >> /home/pi/wrecon_log
    echo "wrecon stop '$(date)'" >> /home/pi/wrecon_log
  fi
  ```

- External HDD spinning all the time
  - It seems that external HDD keeps spinning for at least 2hours before it stops. But these results were inconsistent during my tests, and sometimes even when the disk was unmounted it kept spinning for hours. I have tried to tackle this using [hdparm](https://wiki.archlinux.org/title/hdparm) utility. I was unable to get the state of the disk via cli so I kept listening the for the rotation like a ding dong.
> At the time of writing this, I have found that `sudo smartctl -i -n standby /dev/sda` returns the info needed...
  - I have ended up using two scripts one for mount and one for unmount which also control the disk spinning .
    - `bmount`
      ```bash
      #!/bin/bash
      echo "Trying to mount /mnt/mydisk and set benevolent spindown times for HDD"
      sudo hdparm -B100 -S60 /dev/sda
      sudo mount -t ntfs-3g -o uid=1000,gid=1000,umask=007 /dev/sda1 /mnt/mydisk
      ```
    - `bumount`
      ```bash
      #!/bin/bash
      echo "Trying to unmount /mnt/mydisk and set aggresive spindown times for HDD"
      sudo hdparm -B1 -S60 /dev/sda
      sudo umount /mnt/mydisk
      ```

- Power consumption
  - I wanted to know how much electricity will the setup consume over a year and how much it will cost. The server will run most of the year doing nothing, disc not spinning and waiting for ssh connection. I have connected the Pi to the 5.2V power brick with V/A display on the picture below.
  ![PiZero storage server current consumption](/blog/2022-08-27-pizero-storage-server/server-consumption.jpg)
  - Setup consumes in Idle state ~0.27A, and around 0.6A when actively receiving data
  - Yearly consumption
    - 5.2 * 0.27 * 24 * 365 / 1000 = 12.299 kW/h
  - Yearly electricity price (price for kWh was taken from [here](https://servisprofi.sk/kolko-stoji-kwh-elektrickej-energie/))
    - 12.299 * 1.12 = 13.775euro
    - I am not very happy with this, since during my tests, the measuring power plug was unable to measure power consumption of PiZero without HDD attached. It would be ideal if I could disconnect data and power from external HUB when HDD is not used. Maybe in the future ;-).

- Backup time
  - During my tests transfer speeds were somewhere around 500kB/s. This is of course no lightning speed in today's world, but it was expected, since PiZero has only USB 2.0 ports and single CPU. Still it is good enough for me. PiZero represents my second locality and my workflow consists of:
    - Sort photos locally on the phone
    - Backup the folder structure via USB to my on-site external HDD
    - Backup to my second locality
      - Put my phone to charger
      - Connect my phone to ZeroTier VPN
      - Start `termux`
      - Mount the discs with `bmount` on the pi
      - Run `rsync` over night. So even few gigabytes are no issue. Also I backup data to my second locality after I backup them at home to my other HDD directly over USB 3.0 which is much faster.
      - Verify backup in the morning and unmount the disk with `bumount`

- ZeroTier One disconnects on Android
  - There seems to be an issue, where Android kills the ZeroTier VPN connection after some time when screen is locked.
  - So far I have no idea what causes this, I am testing some Keep Screen On workaround Apps. Luckily `rsync` can easily continue where it left off.

## The summary

I am quite happy with the result. For a long time I was unable to find a reasonable use case for my Raspberry Pi which was just lying around doing nothing (this seems to be the case for many of my friends and colleagues with Pi). I have learned a thing or two along the way and obtained some reasonably priced backup locality.

## 2022.07.10 update

Well in the end I was not able to solve the issue with ZeroTier disconnecting on Android after random amount of time. This was especially annoying when I was trying to upload some larger backups. I have switched to similar service - [Tailscale](https://tailscale.com).

Tailscale is build on top of  WireGuard and has clients for Android, Pi, Window and Mac... They also generously provide free tier for single admin with up to 20 devices which is awesome. I was able to deploy the solution on my remote RPi Zero through ssh using ZeroTier and all went fine. Currently I have kept ZeroTier and Tailscale running next to each other.
Tailscale client works as expected on Android and they even provide Android Quick Setting button which is a really nice touch.
