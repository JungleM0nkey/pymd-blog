---
layout: post
title: Creating an NFS Share on Centos 7
published-on: June 7, 2017
---

#
This tutorial will cover setting up a shared file directory on CentOS 7 using NFS. The guide will be sharing the directory with a Windows 10 Client.

#
Install the software

```bash
yum install nfs-utils libnfsidmap
```
#
Set the services to start on startup

```bash
systemctl enable nfs-server
systemctl enable rpcbind
```
#
Reboot the server

```bash
reboot
```
#
Select the directory you want to share or create one.

```bash
mkdir /nfsdir
```
#
Set permissions on the NFS shared directory

```bash
chmod 777 /nfsdir 
```
#
Edit the /etc/exports file with the location of your shared NFS directory.
Make sure the IP address is that of the PC you are sharing the directory with.

```bash
/nfsdir 192.168.1.3(rw,sync,no_root_squash,no_all_squash)
```
#
Export the directory

```bash
exportfs -r
```
#
Configure firewall

```bash
firewall-cmd --permanent --zone public --add-service mountd
firewall-cmd --permanent --zone public --add-service rpc-bind
firewall-cmd --permanent --zone public --add-service nfs
firewall-cmd --reload
```
#
Edit /etc/rc.local and add the following lines

```bash
systemctl restart nfs-server
mount -a
```
#
Add Services for NFS to Windows 10.
Search for Turn Windows features on or off in the start menu. 
Expand Services for NFS and check off Administrative Tools and Client for NFS

![](https://1.bp.blogspot.com/-Mtiqk_bAMnY/WTidUQI3KuI/AAAAAAAACxs/CaFXdMiBmh8ke-4GqIfAt06tkhO84WKhgCLcB/s320/Capture.PNG)

After the install reboot your computer & mount the linux share to a network drive. Run the command, where 192.168.1.2 is the address of the Linux server. 
```bash
mount 192.168.1.2:\nfsdir z:
```