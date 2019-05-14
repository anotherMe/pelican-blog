Title: Install Joomla 3.6 on Ubuntu 16.04
Date: 2017-04-29
Category:
Author: Marco
Tags: linux, ubuntu, joomla
Status: published

### Install LAMP

sudo tasksel install lamp-server

Set a password for MySQL root user and note it.

As of today the tasksel command results in having installed:

*   PHP 7.0.15
*   Apache 2.4.18
*   MySQL 5.7.18

#### Tune PHP installation

Install some more module:

sudo apt install php-cgi php-json php-xml php-mcrypt php-curl php-mysql php-zip

Edit PHP configuration file:

sudo vi /etc/php/7.0/apache2/php.ini

and turn off output buffering:

...
output\_buffering = Off
...

#### Tune Apache installation

sudo a2enmod rewrite

#### Tune MySQL and setup database

Secure MySQL server:

sudo mysql\_secure\_installation

*   Remove anonymous users? \[Y/n\] **yes**
*   Disallow root login remotely? \[Y/n\] **yes**
*   Remove test database and access to it? \[Y/n\] **yes**
*   Reload privilege tables now? \[Y/n\] **yes**

Connect to MySQL:

mysql \-u root \-p

and create a database for Joomla:

mysql> CREATE DATABASE joomladb;
mysql> CREATE USER joomlauser@localhost IDENTIFIED BY 'your-password';
mysql> GRANT ALL PRIVILEGES ON joomladb.\* TO 'joomlauser'@'localhost';
mysql> FLUSH PRIVILEGES;
mysql> quit

### Install Joomla

Download and unpack Joomla:

wget https://fromwhereyouwant/joomla\_3-6-5.tar.gz
tar -xf joomla\_3-6-5.tar.gz -C /var/www/targetdir

Change owner and group:

sudo chown -R www-data:www-data targetdir

Check file permissions, they should already be:

*   folders: 755 or rwx r-x r-x
*   files: 644 or rw- r-- r--

### Create virtual host

Create a new conf file:

sudo vim /etc/apache2/sites\-available/mysite.conf

and edit to something like this:

<VirtualHost \*:80>
ServerAdmin admin@yourdomain.com
DocumentRoot /var/www/yourdomain.com/
ServerName your-domain.com
ServerAlias www.your-domain.com
<Directory /var/www/yourdomain.com/>
Options FollowSymLinks
AllowOverride All
Order allow,deny
allow from all
</Directory>
ErrorLog /var/log/apache2/your-domain.com-error\_log
CustomLog /var/log/apache2/your-domain.com-access\_log common
</VirtualHost>

Then enable the new site:

sudo a2ensite mysite.conf

Restart Apache:

sudo service apache2 restart

You should now be ready to connect to your site and start Joomla configuration ( but you may have to fiddle with you _hosts_ file ).

#### Refernces

This guide is based on the [official Joomla installation guide](https://docs.joomla.org/J3.x:Installing_Joomla).
