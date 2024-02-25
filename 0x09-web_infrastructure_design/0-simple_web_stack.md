# Simple web stack diagram

![0-simple_web_stack](https://github.com/SaidLamghari/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack.jpg)

# One-Server Web Infrastructure Description
Design a one server web infrastructure that hosts the website that is reachable via www.foobar.com.

# **How it works:**
### 1. A user types www.foobar.com into their browser.
### 2. The user's DNS resolver queries the DNS for the IP address associated with www.foobar.com.
### 3. The DNS returns the IP address 8.8.8.8.
### 4. The user's browser sends a request to the web server at 8.8.8.8.
### 5. The web server checks if it has the requested web page in its cache.
### 6. If the web page is not in the cache, the web server forwards the request to the application server.
### 7. The application server processes the request and generates the dynamic content for the web page.
### 8. The application server sends the generated content back to the web server.
### 9. The web server caches the content and sends it back to the user's browser.
### 10. The user's browser displays the web page.

# This infrastructure is suitable for small websites with low traffic. It consists of the following components:
### **Server:**
* A server is a computer that provides services to other computers over a network.
* Servers are typically located in data centers, which are facilities that house large numbers of servers and provide them with power, cooling, and security.
* Servers can be either physical (a dedicated computer) or virtual (a software-defined computer that runs on a physical server).
* Servers run an operating system (OS), which is a software that manages the server's hardware and resources.

### **Web Server:**
* A web server is a server that hosts websites.
* Web servers serve static content, such as web pages, images, and videos.
* Web servers typically use the HTTP protocol to communicate with clients (web browsers).

### **Application Server:**
* An application server is a server that hosts web applications.
* Application servers compute dynamic content, such as the results of a search query or the contents of a shopping cart.
* Application servers typically use the Java EE or .NET Framework to develop and deploy web applications.

### **Database:**
* A database is a software that stores and manages data.
* Databases are used to store application data, such as user accounts, products, and orders.
* Databases typically use the SQL language to query and manipulate data.

### **DNS:**
* DNS (Domain Name System) is a hierarchical naming system for computers, services, and other resources connected to the Internet or a private network.
* DNS translates domain names (such as www.foobar.com) into IP addresses (such as 8.8.8.8).
* DNS is essential for the functioning of the Internet, as it allows computers to find each other by name.

### **A Record:**

* An A record is a type of DNS record that maps a domain name to an IPv4 address.
* For example, the A record for www.foobar.com would be 8.8.8.8.

### **Single Point of Failure:**

* A single point of failure is a component in a system that, if it fails, will cause the entire system to fail.
* In the diagram, the server is a single point of failure because there is no redundancy. If the server fails, the website will be unavailable.

### **Deployment Downtime:**
* Deployment downtime is the period of time when a website is unavailable due to the deployment of new code.
* Deployment downtime is typically caused by the need to restart the web server after new code has been deployed.

### **Scalability:**
* Scalability is the ability of a system to handle increasing amounts of traffic or data.
* The infrastructure in the diagram is not scalable because it is based on a single server. If the traffic to the website exceeds the capacity of the server, the website will become slow or unavailable.

### **Network Communication:**
* Servers communicate with each other and with clients over a network.
* The most common network protocol is TCP/IP, which is a suite of protocols that provides reliable and efficient data transmission over networks.

