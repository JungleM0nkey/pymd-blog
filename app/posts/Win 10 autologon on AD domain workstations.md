---
layout: post
title: Win 10 autologon on AD domain workstations
published-on: April 16, 2020
---

#
This is going to be a quick one. Had to dig way too much online to get a solid answer to this. 
The registry change below will configure automatic logon on Windows 10 computers, specifically local accounts on computers connected to a domain.  
  
Open **regedit** and navigate to:  

```python
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon  
```

#
Modify the keys below, if you cannot find them create them: **Right Click** > **New** > **String Value**  

```python
AutoAdminLogon=1  
DefaultDomain=your.domain.name  
DefaultUserName=UserName  
DeafaultPassword=Password
```

