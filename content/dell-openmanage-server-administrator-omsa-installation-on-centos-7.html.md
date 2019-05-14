Title: Dell OpenManage Server Administrator (OMSA) installation on CentOS 7
Date: 2017-01-18
Category:
Author: Marco
Tags: linux, centos, omsa, dell
Status: published

**Hardware**: DELL Poweredge 2950

Install pre-requisites:

    yum install wget
    yum install perl

Set up repository:

    wget -q -O - http://linux.dell.com/repo/hardware/dsu/bootstrap.cgi | bash

Install OMSA:

    yum update
    yum install srvadmin-all

Start OMSA:

    /opt/dell/srvadmin/sbin/srvadmin-services.sh start

If everything went the right way, you should find OMSA listening on port 1311:

**_https://YOURSERVERIP:1311_**

Note that it's _https_ and not _http_.

### References

[Dell OMSA Linux Repository](http://linux.dell.com/repo/hardware/omsa.html)
