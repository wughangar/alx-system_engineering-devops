Specifics about the Infrastructure:
SSL Certificate (HTTPS):
An SSL certificate is added to serve www.foobar.com over HTTPS. This ensures secure, encrypted communication between users' browsers and the web servers, protecting sensitive data during transmission.
Reason for adding this feature: HTTPS is used to encrypt data transmitted between users and the website, preventing eavesdropping and ensuring data confidentiality.
Firewalls:
The three firewalls are added to protect each server component, ensuring only authorized traffic is allowed to pass through and enhancing the overall security of the infrastructure.
Reason for adding this feature: Firewalls are added to enforce security policies and protect the servers from unauthorized access and potential security threats.
Monitoring Clients (Data Collectors):
Three monitoring clients (data collectors) are installed on each server. These agents collect performance metrics and send data to the monitoring service (e.g., Sumo Logic) for real-time monitoring and analysis.
Reason for this feature: Monitoring agents are installed to track server performance, health, and availability, enabling proactive issue detection and troubleshooting.

Monitoring and Data Collection:

Monitoring is used to track server performance, resource utilization, and application behavior. The monitoring clients collect data from various sources on the servers, including CPU usage, memory, disk space, network traffic, and application-specific metrics. This data is sent to the monitoring service, where it is analyzed and visualized for insights into the infrastructure's health and performance.

Monitoring Web Server QPS:

To monitor web server QPS (Queries Per Second), the monitoring agent should collect request/response data from the web server. The monitoring service can then use this data to calculate the average number of queries served per second over a specific time interval.

Issues with this Infrastructure:
Single MySQL Server for Writes:
Having only one MySQL server capable of accepting writes creates a single point of failure. If this server goes down or experiences performance issues, it can disrupt write operations and affect the website's functionality.

Terminating SSL at the Load Balancer Level:
Terminating SSL at the load balancer exposes decrypted data within the internal network, potentially increasing security risks. It's better to use end-to-end encryption from clients to web servers.

Servers with Identical Components:
Using servers with all the same components (database, web server, and application server) might lead to inefficient resource utilization. It can also cause difficulties in scaling or maintaining individual components separately, limiting flexibility and resource management.

Remedies:
Implementing SSL termination at the web servers (end-to-end encryption).
Considering a more modular infrastructure with dedicated servers for different roles to enhance scalability and maintainability
setting up database replication for high availability
Implementing a robust monitoring system helps identify and address potential issues proactively.
