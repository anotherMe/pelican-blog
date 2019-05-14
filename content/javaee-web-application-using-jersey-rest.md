Title: JavaEE Web Application using Jersey REST
Date: 2017-07-18
Category: Coding
Author: Marco
Tags: java, jersey, rest
Status: draft

**Jersey** is the reference implementation for the JSR 311 specification, also called JAX-RS (The Java API for RESTful Web Services). _Java Specification Request (JSR)_ 311, defines the Java REST support API.

### Add dependencies

Using **Maven**, we just need to add the following two dependencies

*   com.sun.jersey : jersey-sevlet ( version 1.19.4 atow )
*   com.sun.jersey.jersey-json ( version 1.19.4 atow )

**NOTE**: At time of writing, version 2.x of this libraries ( migrated to group org.glassfish.jersey ) seems not to be viable option.

Other needed dependencies will be added auto-magically.

### Configuration

To package our _RESTful Web service_ as part of a _web application_ ( servlets + JSPs style application)_, w_e need to define the components of the RESTful Web service and to configure the servlet and mappings. In doing so, we have two options:

1.  define a class that extends `javax.ws.rs.core.Application`
2.  update the `web.xml` deployment descriptor

#### Extend Application class

Option _one_ involves creating a class inheriting from `javax.ws.rs.core.Application`:

import javax.ws.rs.core.Application;
import javax.ws.rs.ApplicationPath;
...
@ApplicationPath("restapi")
public class MyApplication extends Application {

   @Override
   public Set<Class<?>> getClasses() {
   Set<Class<?>> s = new HashSet<Class<?>>();
   s.add(MyResource1.class);
   s.add(MyResource2.class);
   ...
   return s;
 }
}

**NOTE**: the use of `ApplicationPath` annotation to define the base URI pattern that gets mapped to the servlet.

#### Update web.xml

Option _two_ involves modifying ( or creating, if not present ) the `web.xml` deployment descriptor.

...
 <servlet>
 <servlet-name>Jersey Web Application</servlet-name>
 <servlet-class>com.sun.jersey.spi.container.servlet.ServletContainer</servlet-class>
 <init-param>
 <param-name>com.sun.jersey.config.property.packages</param-name>
 <param-value>com.example.restapi</param-value>
 </init-param>
 <load-on-startup>1</load-on-startup>
 </servlet>
 <servlet-mapping>
 <servlet-name>Jersey Web Application</servlet-name>
 <url-pattern>/restapi/\*</url-pattern>
 </servlet-mapping>
...

**NOTE**: the `<param-value>it.gas.restapi</param-value>`, which points to the package containing our resources.

### Create a new resource

package com.example.restapi;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

/\*\*
 \* Root resource (exposed at "myresource" path)
 \*/
@Path("myresource")
public class MyResource {

    /\*\*
     \* Method handling HTTP GET requests. The returned object will be sent
     \* to the client as "text/plain" media type.
     \*
     \* @return String that will be returned as a text/plain response.
     \*/
    @GET
    @Produces(MediaType.TEXT\_PLAIN)
    public String getIt() {
        return "Hello world";
    }
}

### References

*   [Oracle Help Center - Packaging and Deploying RESTful Web Services](https://docs.oracle.com/cd/E24329_01/web.1211/e24983/configure.htm#RESTF179)
*   [Jersey documentation - Getting started](https://jersey.github.io/documentation/latest/getting-started.html)
*   [Vogella - REST with Java (JAX-RS) using Jersey - Tutorial](http://www.vogella.com/tutorials/REST/article.html)
