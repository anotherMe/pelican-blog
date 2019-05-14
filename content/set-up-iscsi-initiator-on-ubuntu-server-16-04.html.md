Title: Set up iSCSI initiator on Ubuntu Server 16.04
Date: 2017-04-17
Category:
Author: Marco
Tags: linux, ubuntu, iscsi
Status: draft

Install needed packages:

\# apt-get install vmfs-tools open-iscsi

Connect to iSCSI target :

\# iscsiadm -m discovery -t st -p <ISCSI.TARGET.IP.HERE>
# iscsiadm -m node --login

Mount VMFS filesystem:

$ mkdir /root/iscsi\_sdd
# vmfs-fuse /dev/sdd1 /root/iscsi\_sdd/

Additional notes
----------------

To unmount the VMFS filesystem:

\# fusermount -u /root/iscsi\_sdd/

To check a VMFS filesystem spanning on multiple extents ( 5 in our example ):

\# fsck.vmfs /dev/sdc1 /dev/sde1 /dev/sdf1 /dev/sdg1 /dev/sdh1
