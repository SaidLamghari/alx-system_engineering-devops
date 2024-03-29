# 0x09. Web infrastructure design

**Tasks**

## 0. Simple web stack
- **Design a one server web infrastructure that hosts the website that is reachable via www.foobar.com.**
	***Used:***
	* 1 server
	* 1 web server (Nginx)
	* 1 application server
	* 1 application files (your code base)
	* 1 database (MySQL)
	* 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

## 1. Distributed web infrastructure
- **Design a three server web infrastructure that hosts the website www.foobar.com.**
	**Add:**
	* 2 servers
	* 1 web server (Nginx)
	* 1 application server
	* 1 load-balancer (HAproxy)
	* 1 set of application files (your code base)
	* 1 database (MySQL)

## 2. Secured and monitored web infrastructure
- **Design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.**
	***Add:***
	* 3 firewalls
	* 1 SSL certificate to serve www.foobar.com over HTTPS
	* 3 monitoring clients (data collector for Sumologic or other monitoring services)
## 3. Scale up
- ***Add:***
	* 1 server
	* 1 load-balancer (HAproxy) configured as cluster with the other one
	* Split components (web server, application server, database) with their own server



