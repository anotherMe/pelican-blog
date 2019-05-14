Title: Proxying Tomcat through Apache on Debian
Date: 2017-09-21
Category:
Author: Marco
Tags: tomcat, apache
Status: published

**GOAL**: Point your browser to your machine port 80 ( eg: **http://yourhost.com/yourapp** ) and have Apache seamless redirect to an instance of Tomcat running on the same machine ( eg: **http://yourhost.com:8084/yourapp** )

## Install mod_proxy

If not already done, we need to enable **mod_proxy** on Apache:

```bash
# a2enmod proxy
# a2enmod proxy_http
# service apache2 restart
```

## Configure Apache

Then we must tell Apache about the web application we wish to forward to Tomcat. We do this by creating a new configuration file:

```bash
  # vi /etc/apache2/conf-available/YOURFANCYNAME.conf
```

containing the following lines:

  ProxyPass /yourapp http://localhost:8084/yourapp
  ProxyPassReverse /yourapp http://localhost:8084/yourapp

In this example, we suppose to have a Tomcat instance listening on port _8084_ and running the application _yourapp_.

Finally, we have to enable the newly created configuration:

```bash
  # a2enconf YOURFANCYNAME  
  # service apache2 restart
```

## Configure Tomcat

Just one final step, tell Tomcat about the proxying:

```bash
  # vi /opt/apache-tomcat/conf/server.xml
```

or, if you are running Tomcat through Netbeans:

```bash
  $ vi ~/.netbeans/8.1/apache-tomcat-8.0.27.0_base/conf/server.xml
```

changing the connector line like this:

```html
  <!--<Connector URIEncoding="utf-8" connectionTimeout="20000" port="8084" protocol="HTTP/1.1" redirectPort="8443"/>-->
  <Connector URIEncoding="utf-8" connectionTimeout="20000" port="8084" protocol="HTTP/1.1" redirectPort="8443" proxyPort="80"/>
```

### References

[Apache Tomcat 8 Documentation - Proxy Support HOW-TO](https://tomcat.apache.org/tomcat-8.0-doc/proxy-howto.html)
