Title: How to change domain of your WordPress installation
Date: 2019-07-23
Category: Tips & tricks
Author: Marco
Tags: wordpress
Status: published

Migrating an existing WordPress installation from one domain to another is an
operation involving some tweaking. This is because, when you perform the initial
WP setup, the name of your domain is hard-coded in the WP database.

So in order to replace the old domain with the new one you'll have to issue some
SQL commands:

```sql

UPDATE wp_options SET option_value = 'http://NEW.DOMAIN.COM' where option_name in ( 'siteurl', 'home' );

UPDATE wp_posts SET guid = replace(guid, 'http://OLD.DOMAIN.COM', 'http://NEW.DOMAIN.COM');

UPDATE wp_posts SET post_content = replace(post_content, 'http://OLD.DOMAIN.COM', 'http://NEW.DOMAIN.COM');

UPDATE wp_postmeta SET meta_value = replace(meta_value,'http://OLD.DOMAIN.COM', 'http://NEW.DOMAIN.COM');

```
