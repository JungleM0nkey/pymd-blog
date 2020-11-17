---
layout: post
title: Hiding a transparent DIV with jQuery
published-on: April 17, 2020
---

#
So this is a problem which is related to a project I have been working on for a few weeks now and the project itself will be an entire other post of itself but before that I wanted to share a little bit of a CSS workaround I stumbled upon.  
  
The problem is simple, it is hard to hide something behind a DIV with a background that is transparent. z-index does not help here unfortunately and after trying numerous things with little success I ended up with a compromise!  
  
This is the result:

![](https://1.bp.blogspot.com/--7o6TSGUgoE/XpivNKD1UNI/AAAAAAAARkI/A-vsQuJ6elY92Xq5PqtZ_9tihIyWS5rYACLcBGAsYHQ/s1600/slidegif.gif)

And the simple workaround was simply making the DIV go from 0 to 300px using jquery.

  

**CSS:**

  
```css
#table-wrapper{
	position:absolute;
	right:-115px;  
	top:115px;  
	height:300px;  
	width:0px;  
	transition:0.5s;  
	background-color: rgba(0, 0, 0, 0.2);
}

#table{  
	padding-top:10px;  
	background-color:none;  
	transition:0.5s;  
	color:rgba(255, 255, 255, 0);  
	font-weight:normal;  
	text-align:left;  
	font-size:12px;  
	border-spacing: 0px;  
	border-collapse: separate;  
	padding-left:3px;  
	float:left;  
	width:1px;  
	white-space: nowrap;  
}
```
#
**JQuery:**  
  
```javascript
$('#archive-button').on('click', function(){  
	$('#table-wrapper').css('right', '-405px');  
	$('#table-wrapper').css('width', '290px');  
	$('#table').css('width', '290px');  
	$('#table').css('color','rgba(255, 255, 255, 1)');  
	$('#archive-button-element').css('transform', 'rotate(90deg)')
});
```