Title: How to slow down my Razer mouse on Ubuntu
Date: 2019-06-15
Category: Tips & tricks
Author: Marco
Tags: linux, mouse, ubuntu
Status: published

I'm using a Razer DeathAdder left-handed mouse for my Windows box, that's my main coding / playing stattion. Sometimes,
but definetely in the summer,  when it's too hot to turn on my playing rig, I usually plug in my Ubuntu laptop to the
monitor, mouse and keyboard of the main station.

Problem is the Razer mouse pointer has got far too much acceleration and it doesn't seem possible to slow it down to
sensible speeds with Ubuntu control center.

After somme googling I ended up with a little hacky solution: **xinput** comes to the rescue.


Using **xinput** you can list all of your input devices and their IDs:

```
xinput list
```

Which gives the following output on my laptop (some lines omitted):

```
...
⎜   ↳ Razer Razer DeathAdder                  	id=16	[slave  pointer  (2)]
...
```

Once we know the device ID, we can interrogate it for the available properties:

```
xinput list-props 16
```

Which, in turn, gives this output:

```
...
libinput Accel Speed (292):	-0.000000
libinput Accel Speed Default (293):	0.000000
libinput Accel Profiles Available (294):	1, 1
libinput Accel Profile Enabled (295):	1, 0
libinput Accel Profile Enabled Default (296):	1, 0
...
```

After some trial and error, searching for the possible settings, I've managed to slow down the mouse pointer to an
acceptable speed with:

```
xinput set-prop 16 "libinput Accel Speed" -1
```
