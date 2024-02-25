# Secured and monitored web infrastructure diagram


![ 2-secured_and_monitored_web_infrastructure]( https://github.com/SaidLamghari/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.jpg)

# **Some specifics about this infrastructure:**

### 1. Reasons for Additional Elements:
* **Firewalls:** Firewalls are used to protect the infrastructure from unauthorized access. They are configured to allow only authorized traffic to pass through.
* **SSL Certificate:** An SSL certificate is used to serve the website over HTTPS. This encrypts the data transmitted between the user's browser and the web server, protecting it from eavesdropping.
* **Monitoring Clients:** Monitoring clients are used to collect data for Sumologic or other monitoring services. This data can be used to identify and resolve problems before they affect the website.

### 2. Purpose of Firewalls:
   Firewalls act as a barrier between a trusted internal network and untrusted external networks (e.g., the internet). They control and monitor incoming and outgoing network traffic based on predetermined security rules. Firewalls help prevent unauthorized access, protect against network threats, and enforce security policies.

### 3. Importance of Serving Traffic over HTTPS:
   Serving traffic over HTTPS ensures secure transmission of data between the web servers and user web browsers. HTTPS encrypts the data, preventing unauthorized parties from intercepting or tampering with it. This encryption is particularly crucial when transmitting sensitive information, such as login credentials, payment details, or personal data, as it protects against eavesdropping and data tampering.

### 4. Role of Monitoring:
   Monitoring is used to keep track of the infrastructure's performance, availability, and health. It involves collecting and analyzing various metrics, logs, and events related to the servers, applications, and other components. Monitoring helps identify issues, detect anomalies, and provide insights for proactive management, capacity planning, and troubleshooting.

### 5. Data Collection by Monitoring Tools:
   Monitoring tools collect data from various sources, including system metrics (CPU, memory, disk usage), application logs, network traffic, error logs, and performance metrics. This data is collected using agents, scripts, or API calls and is sent to the monitoring tool's data collector or agent installed on the servers. The monitoring tool then processes and analyzes the data to provide insights and visualizations.

### 6. Monitoring Web Server QPS:
   To monitor web server QPS (Queries Per Second), you can configure your monitoring tool to collect the relevant web server metrics, such as the number of requests or transactions processed per second. These metrics can be obtained from server logs, server-side monitoring agents, or by integrating with web server software. By monitoring and analyzing these metrics, you can track the web server's performance, detect any sudden spikes or drops in traffic, and take appropriate actions.

# **Issues with the Infrastructure:**
* **SSL Termination at Load Balancer:** Terminating SSL at the load balancer level is an issue because it means that the load balancer is able to decrypt the traffic. This is a security risk, as it means that the load balancer could be compromised and the decrypted traffic could be intercepted.
* **Single MySQL Server for Writes:** Having only one MySQL server capable of accepting writes is an issue because it means that the database is a single point of failure. If the MySQL server fails, the website will be unable to accept any new writes.
* **Servers with All Components:** Having servers with all the same components (database, web server, and application server) might be a problem because it means that the servers are not specialized. This can lead to performance problems, as the servers may not be able to handle the load of all of the different components.

