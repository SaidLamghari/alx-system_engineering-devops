# Distributed web infrastructure diagram

![1-distributed_web_infrastructure](https://github.com/SaidLamghari/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.jpg)

# Distributed web infrastructure
This infrastructure is more scalable and fault-tolerant than the one-server infrastructure.

# How it works:
### 1. A user types www.foobar.com into their browser.
### 2. The user's DNS resolver queries the DNS for the IP address associated with www.foobar.com.
### 3. The DNS returns the IP address of the load balancer.
### 4. The user's browser sends a request to the load balancer.
### 5. The load balancer distributes the request to one of the two servers.
### 6. The server processes the request and generates the dynamic content for the web page.
### 7. The server sends the generated content back to the load balancer.
### 8. The load balancer sends the content back to the user's browser.
### 9. The user's browser displays the web page.

# ** Some specifics about this infrastructure**

* **Load balancer:** The load balancer is added to distribute traffic across the two servers. This ensures that the traffic is evenly distributed and that the website is always available, even if one of the servers fails.
* **Database cluster:** The database cluster is added to provide high availability and scalability for the database. The cluster consists of a primary node and one or more replica nodes. The primary node handles all read and write operations, while the replica nodes handle read operations only. If the primary node fails, one of the replica nodes will be promoted to become the new primary node.

### **Load Balancer Distribution Algorithm:**

The load balancer can be configured with a variety of distribution algorithms, such as:

* **Round robin:** This algorithm distributes traffic evenly across all available servers.
* **Least connections:** This algorithm sends traffic to the server with the fewest active connections.
* **Weighted round robin:** This algorithm assigns a weight to each server, and then distributes traffic based on the weights.

### **Active-Active vs. Active-Passive Load Balancers:**

* **Active-active:** In an active-active setup, all servers are active and handle traffic. This provides the highest level of availability, but it can be more complex to manage.
* **Active-passive:** In an active-passive setup, only one server is active at a time, while the other servers are passive and waiting to take over if the active server fails. This is a simpler setup to manage, but it provides less availability than an active-active setup.

### **Database Primary-Replica Cluster:**

In a database primary-replica cluster, the primary node is the master node and the replica nodes are the slave nodes. The primary node handles all read and write operations, while the replica nodes handle read operations only. If the primary node fails, one of the replica nodes will be promoted to become the new primary node.

### **Difference Between Primary and Replica Nodes:**

* **Primary node:** The primary node is the master node and handles all read and write operations. It is the only node that can make changes to the database.
* **Replica node:** Replica nodes are slave nodes that handle read operations only. They are updated by the primary node, and they cannot make changes to the database.

# **Issues with the Infrastructure:**

### **SPOFs:**

* The load balancer is a single point of failure. If the load balancer fails, the entire website will be unavailable.
* The database primary node is a single point of failure. If the primary node fails, the website will be unavailable until a replica node is promoted to become the new primary node.

### **Security issues:**

* The infrastructure does not have a firewall to protect it from unauthorized access.
* The website is not served over HTTPS, which means that the data transmitted between the user's browser and the web server is not encrypted.

### **Monitoring:**

* The infrastructure is not being monitored, which means that it is difficult to identify and resolve problems before they affect the website.

