---
layout: post
title: Turn your Raspberry Pi into a WIFI access point
published-on: June 1, 2017
---

![](https://1.bp.blogspot.com/-iiD3J2aIIVw/WTCjlc9UYXI/AAAAAAAACo4/8ngtJbtCeyc98vqQfBOlnsiDg-KYCaQpACLcB/s1600/pi_ap.jpg)
#
This tutorial will guide you through the steps of converting your Raspberry Pi into a local WiFi Access Point for your network.
Security: WPA2

Note: The AP is for an existing network with working dhcp.

Recommended WiFi dongle: 
```
EDUP EP-MS1559 11N 300Mbps Wifi Wireless-N USB Adapter.
```

Is there a specific reason why I am recommending this one? No, not really but it has worked for me without any issues and it provides a strong signal without any drops. 
Also the antenna I am using came from a different dongle, however the one it comes with should do the job just fine. 

If you are going to get a different dongle make sure that it uses the Realtek 8192cu chip, it is possible to get an AP working on a different chipset however this guide is for 8192cu. 


Connect your Pi to your home network via ethernet and plugin the wifi dongle into one of the USB slots.

```bash
dmseg | grep 8192cu
usbcore: registered new interface driver rtl8192cu
```
#
Install hostapd

```bash
sudo apt-get install hostapd bridge-utils

wget http://www.daveconroy.com/wp3/wpcontent/uploads/2013/07/hostapd.zip
unzip hostapd.zip 
sudo mv /usr/sbin/hostapd /usr/sbin/hostapd.bak
sudo mv hostapd /usr/sbin/hostapd.edimax 
sudo ln -sf /usr/sbin/hostapd.edimax /usr/sbin/hostapd 
sudo chown root.root /usr/sbin/hostapd 
sudo chmod 755 /usr/sbin/hostapd
```
#
The hostapd binary by default does not work with the 8192 chipset however if you replace it with the one above it should work without any issues.

Edit the interfaces file to look like this, modify the IP values to fit your own network.

```bash
nano /etc/network/interfaces
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
address 192.168.1.18
netmask 255.255.255.0
gateway 192.168.1.1

allow-hotplug wlan0
iface wlan0 inet manual

auto br0
iface br0 inet static
address 192.168.1.252
netmask 255.255.255.0
network 192.168.1.0
broadcast 192.168.1.255
gateway 192.168.1.1

bridge-ports eth0 wlan0
```

#
Edit the hostapd config file to look like this, modify the fields to your requirements.
Generate the wpa-psk string by going to http://jorisvr.nl/wpapsk.html and entering your SSID and password into the generator.

```bash
nano /etc/hostapd/hostapd.conf

ctrl_interface=/var/run/hostapd
macaddr_acl=0 auth_algs=1
driver=rtl871xdrv
interface=wlan0
bridge=br0
hw_mode=g
ieee80211n=1
wme_enabled=1
channel=4
ssid=Wifi-Name
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_psk=4bba27cede6b7ee0a62c8d597dc8fb0b3ff4eebb99a5cd037e5acf4cb4a8
wpa_key_mgmt=WPA-PSK
#wpa_pairwise=TKIP
rsn_pairwise=CCMP
```
#
This will enable hostapd to start on boot.
```bash
nano /etc/default/hostapd
Uncomment the line: DAEMON_CONF="/etc/hostapd/hostapd.conf"
```
#
Restart your pi and attempt to connect!
Enjoy your new AP.