Title: SVN+SSH on Windows with SlikSVN and KiTTY
Date: 2020-04-13
Category: Tips & tricks
Author: Marco
Tags: windows, svn, ssh
Status: published

## Problem

Checkout code hosted on an **SVN** server, accessible only through **SSH** ( SVN+SSH ).

## Tools

We are going to need both an *SVN client* and an *SSH client*. In this document we'll use:

- [SlikSVN](https://sliksvn.com/)
- [KiTTY](http://www.9bis.net/kitty/)


### KiTTY

From KiTTY [download page](http://www.9bis.net/kitty/#!pages/download.md) grab:

- `kitty.exe` ( the main executable)
- `klink.exe` ( the command line SSH client )

Launch `kitty.exe` and create and configure a new session, according to your needs.

In the session you'll save the target server address and port, username, password
or private key, etc.

Save the session, let's call it **my-kitty-session**.

**NOTE** that Windows 10 come with its own SSH client, which is the one you call when issuing
the `ssh` command in a command prompt. In the next step we'll instruct *SlikSVN* ( and only it ) to use *klink* executable as a replacement.

### SlikSVN

Download and install the *SlikSVN* installer from [here](https://sliksvn.com/download/).

We now need to tell SlikSVN which SSH client to use when asked for an SVN+SSH session.

SlikSVN configuration file, on a standard Windows 10 installation is found under:

`C:\Users\YOURUSER\AppData\Roaming\Subversion`

Edit the `config` file, modifying the **tunnels** section, adding the path where you saved
the **klink** executable:

```ini
[tunnels]
ssh = $SVN_SSH C:/opt/kitty/klink.exe
```

## Checkout

With all the tools in place, you should now be able to check the code with something like:

```batch
svn co svn+ssh://YOURUSER@my-kitty-session/path/to/svn/repository/project/
```

**NOTE** that above we provide the name of the KiTTY session we saved previously ( **my-kitty-session** )
instead of the target server address.