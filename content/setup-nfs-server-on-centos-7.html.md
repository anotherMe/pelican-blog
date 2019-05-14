Title: Setup NFS server on CentOS 7
Date: 2017-01-16
Category:
Author: Marco
Tags: linux, centos, nfs
Status: published

Install:

yum -y install nfs-utils

Start service and enable at boot:

systemctl start nfs-server.service
systemctl enable nfs-server.service

Fix permissions on the folder we want to share ( will be here /var/nfs ):

chown nfsnobody:nfsnobody /var/nfs
chmod 755 /var/nfs

Edit file _/etc/exports_ to export the NFS shares. In the example below, we bind three different client machines:

/var/nfs 192.168.1.101(rw,sync,no\_subtree\_check)
/var/nfs 192.168.1.102(rw,sync,no\_subtree\_check)
/var/nfs 192.168.1.103(rw,sync,no\_subtree\_check)

Reload configuration:

exportfs -a

Add _iscsi-target_ to firewall allowed services:

firewall-cmd --permanent --zone public --add-service mountd
firewall-cmd --permanent --zone public --add-service rpc-bind
firewall-cmd --permanent --zone public --add-service nfs
firewall-cmd --reload

### Reference

\[\[https://www.howtoforge.com/tutorial/setting-up-an-nfs-server-and-client-on-centos-7/|reference\]\]
