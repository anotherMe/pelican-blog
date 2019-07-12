Title: Ubuntu 16.04 NetworkManager – disable DNSMasq
Date: 2017-05-07
Category:
Author: Marco
Tags: linux, ubuntu, networkmanager
Status: published

I am facing DNS resolving issue when I connect to my office VPN ( OpenVPN ) using Network Manager: it seems I cannot use my company DNS.

In spite of my efforts trying to force the use of my company DNS, either trying to modify openvpn config file or trying to set DNS in network-manager GUI, still /etc/resolv.conf present no trace of wanted DNS servers.

I managed to resolve this issue by editing the file:

```
/etc/NetworkManager/NetworkManager.conf
```

and commenting out the \*dnsmasq\* line:

```
[main]
plugins=ifupdown,keyfile,ofono
#dns=dnsmasq

[ifupdown]
managed=false
```
