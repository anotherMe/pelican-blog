Title: Install Cacti on Ubuntu Server 16.04 LTS
Date: 2017-02-03
Category:
Author: Marco
Tags: linux, ubuntu, cacti
Status: published

### ![A cactus in the middle of the desert](images/cactus-754882.jpg)

### Install LAMP server

    sudo apt-get install apache2 mysql-server php libapache2-mod-php

During install, you'll be asked for a password for MySQL root user: set one and note it.

### Install RRDtool

    sudo apt install rrdtool

### Install Cacti

Here we install Cacti with his alternate poller, [Spine](http://www.cacti.net/spine_info.php).

    sudo apt-get -y install cacti cacti-spine

During Cacti installation process:

1.  ignore message about _**libphp-adodb**_ include path,
2.  choose **_apache2_** as web server,
3.  let _**dbconfig-common**_ configure your database for you

Access Cacti web interface at _**http://YOURHOSTIP/cacti**_ to complete installation process ( default _**admin**_ password is _**admin**_ ).

###### Reference

[Unixmen](https://www.unixmen.com/install-cacti-ubuntu-14-04/)
