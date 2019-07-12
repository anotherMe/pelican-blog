Title: Proxying Tomcat through Apache on Debian
Date: 2017-08-25
Category:
Author: Marco
Tags: java, linux
Status: draft


By default, Java doesn't use anti-aliasing on fonts in AWT applications.
It's been available for some time however, and can be switched on with
the awt.useSystemAAFontSettings setting.

To enable anti-aliased fonts just for Netbeans, add following line to
the end of the ```netbeans\_default\_options```
line in:

```
/usr/share/netbeans/etc/netbeans.conf
```

e.g.:

```
netbeans_default_options="-J-client -J-Xss2m -J-Xms32m -J-XX:PermSize=32m -J-Dawt.useSystemAAFontSettings=on"
```

Alternatively, you can set this globally so that all AWT apps are
affected, by setting the <span class="bbcode_c">\_JAVA\_OPTIONS</span>
environment variable in your
<span class="bbcode_c">.bash\_profile\*</span>:

```
export _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true'
```

This also has Swing equivalent, using the
<span class="bbcode_c">swing.aatext</span> preference. You'll have to
log out and log back in for this to take effect.

\*NOTE: if you're using **openbox**, set \_JAVA\_OPTIONS in:

```
/home/you/.config/openbox/environment
```
