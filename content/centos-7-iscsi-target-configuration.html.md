Title: CentOS 7 – iSCSI target configuration
Date: 2017-01-16
Category:
Author: Marco
Tags: linux, centos, iscsi
Status: published

Following are instructions for configuring an iSCSI target using [targetcli](http://linux-iscsi.org/wiki/Targetcli) on a **CentOS 7** minimal installation. The underlying hardware is a **DELL Poweredge 2950** server with six 2TB SATA HDDs configured as a whole RAID5 volume of about 10TB.

**IMPORTANT NOTE**: On my first configuration attempt on the DELL PERC 57i RAID controller, keeping the RAID write policy setting to it's default value ( _write through_ ), I was stuck with disk write speeds between 5 MB/sec and 10 MB/sec; only turning on _write back_, I was able to write to disk at speeds between 45 MB/sec and 50 MB/sec ( for details and risks of different write policy see [here](http://www.computerweekly.com/feature/Write-through-write-around-write-back-Cache-explained) )

The first 66,9GB of the disk have been used to install OS. This is parted -l\* output:

Model: DELL PERC 5/i (scsi)
Disk /dev/sda: 9999GB
Sector size (logical/phyisical): 512B/512B
Partition table: gpt
Flag: pmbr\_boot

Number Start End Dimension File system Name Flag
 1 1049kB 2097kB 1049kB bios\_grub
 2 2097kB 1076MB 1074MB xfs
 3 1076MB 66,9GB 65,8GB lvm

Using _parted_ ( to be able to deal with GPT partition table ), we create a new partition ( will be sda4 ), from the end of the last pre-existent partition to the max available size:

\# parted /dev/sda
# parted -a optimal /dev/sda mkpart primary 66,9GB 100%

NOTE: you possibly have to disable / reconfigure SELINUX to complete following instruction.

\# yum install -y targetcli
# systemctl enable target

Launch targetcli interactive console:

\# targetcli

Let's create:

1.  a new _block backstore_,
2.  a new _iscsi target_
3.  and a new lun.

Note that "iqn.2017-01.com.example" is the name we choose for our target machine, "t1" is the nome we choose for our target.

/> backstores/block/ create block1 /dev/sda4
/> iscsi/ create iqn.2017-01.com.example:t1
/> /iscsi/iqn.2017-01.com.example:t1/tpg1/luns create /backstores/block/block1

Now we need to set up ACLs, one for every initiator that will be connecting to our target. You have to provide the correct initiator name ( for an ESXi server, it's the iSCSI adapter's World Wide Name, aka WWN ).

In the following example we add three different initiators:

/> cd iscsi/iqn.2017-01.com.example:t1/tpg1/acls/
/> create iqn.1998-01.com.vmware:machine01-31bf6b8f
/> create iqn.1998-01.com.vmware:machine02-37e477e0
/> create iqn.1998-01.com.vmware:machine03-30905fb0

Delete the portal created by default, and add new one setting specific network interface:

/> cd iscsi/iqn.2017-01.com.example:t1/tpg1/
/> portals/ delete 0.0.0.0 3260
/> portals/ create 10.255.2.230 3260

Adjust firewall to enable iSCSI traffic ( port 3260 ):

\# firewall-cmd --zone=public --add-service=iscsi-target --permanent # open port 3260

Authentication
--------------

Authentication per CHAP should be enabled by default for your targets. To check authentication status:

/> cd iscsi/iqn.2017-01.com.example:t1/tpg1/
/> get attribute authentication

If authentication is indeed enabled, above command output would be:

authentication=1

In the ( unfortunate) case you want to disable authentication:

/> cd iscsi/iqn.2017-01.com.example:t1/tpg1/
/> set attribute authentication=0

Troubleshooting
---------------

When troubleshooting, remember that debug messages are sent to kernel log:

tail -f /var/log/messages

References
----------

*   [A guide to configure iSCSI on RHEL7](https://www.certdepot.net/rhel7-configure-iscsi-target-initiator-persistently/)
*   [Linux SCSI Target wiki](http://linux-iscsi.org/wiki/Main_Page)

Misc
----

In case you would want to delete everything to start all over again:

targetcli clearconfig confirm=True
