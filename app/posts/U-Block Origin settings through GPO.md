---
layout: post
title: U-Block Origin settings through GPO
published-on: October 21, 2019
---

#
There is a couple of guides I was able to find online for Chrome but not for Firefox. Hopefully someone will find this helpful!

Note: This guide assumes you already have a GPO configured to install the U-Block Origin extension on your domain workstations.
#
**Firefox - Creating the Group Policy Object**

1. Right click on the GPO and click edit
2. Navigate to Computer Configuration > Preferences > Windows Settings > Registry

![](https://1.bp.blogspot.com/-TLTQVSOe4R8/Xa3TEd7gL6I/AAAAAAAAPks/apSIRTFlRZs1gHZ20-LKiNQ2Bj9MlnV2QCEwYBhgL/s320/ublock-1.png)

3. On the right hand side Right click in the empty area > New > Registry Item
4. Fill out the settings as follows:

```
Action: Create
Hive: HKEY_LOCAL_MACHINE
Key Path: SOFTWARE\Mozilla\ManagedStorage\uBlock0@raymondhill.net
Value name: Turn on Default
Value type: REG_SZ
Value data: \\path\to\the\file.json
```
#
**Firefox - Creating the .json configuration file**

1. Create a .json file in the location you wrote in the previous section of the tutorial
2. Paste the following data into it

```json
{
    "name": "uBlock0@raymondhill.net",
    "description": "ignored",
    "type": "storage",
    "data": {
        "adminSettings":
    }
}
```

3. Open U-Block and click on settings
4. Modify all the settings as you want them on all your domain workstations, auto-update, whitelist etc.
5. Go to the Settings tab and click Back Up to File at the bottom
6. Open the newly saved .txt file and remove all of the setting lines which you wish to remain configurable by your users
7. Copy the file contents
8. Go to http://raymondhill.net/ublock/adminSetting.html and paste your .txt contents into the top most field
9. Click the downward facing arrow
10. Copy the newly generated contents from the bottom-most field
11. Paste the newly copied line after "adminSettings": in your .json file
12. Save the file
13. You are done!
