Title: Letsencrypt certificates on Apache
Date: 2017-07-06
Category: Coding
Author: Marco
Tags: apache, letsencrypt
Status: draft

Example, stripped down Apache virtual host configuration:

<VirtualHost \*:443>
  ServerName example.com
  SSLEngine on
  SSLProxyEngine On
  SSLCertificateFile    /etc/pki/tls/certs/example.com.cer
  SSLCertificateKeyFile /etc/pki/tls/private/example.com.key
  SSLCACertificateFile  /etc/pki/tls/certs/ca.cer
</VirtualHost>

Your cert is in /root/.acme.sh/geco.gas.it/geco.gas.it.cer  
Your cert key is in /root/.acme.sh/geco.gas.it/geco.gas.it.key  
The intermediate CA cert is in /root/.acme.sh/geco.gas.it/ca.cer  
And the full chain certs is there: /root/.acme.sh/geco.gas.it/fullchain.cer

### Testing your server

You could use [Qualys.com SSL Server Test](https://www.ssllabs.com/ssltest/) ( or have a look at [their documentation](https://www.ssllabs.com/projects/documentation/) )
