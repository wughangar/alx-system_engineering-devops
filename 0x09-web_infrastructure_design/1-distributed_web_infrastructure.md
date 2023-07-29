Specifics about the Infrastructure:
Load Balancer (HAproxy):
The load balancer distributes incoming traffic across the two web servers (Nginx) to balance the load and prevent overloading a single server.

Web Servers (Nginx):
Nginx serves as a reverse proxy, handling incoming HTTP requests, and forwarding dynamic requests to the application servers.

Application Servers:
The application servers run the web application code and generate dynamic content based on user requests.

Database (Primary-Replica Cluster - Master-Slave):
The database consists of a Primary (Master) node and a Replica (Slave) node. The Primary node handles write operations, and the Replica node replicates data from the Primary and handles read-only operations.

Differences between Primary node and replica node
primary node handles write opeartions like: POST, PUT AND DELETE.

Replica node/slave node
cant not handle write operations- it only replicates the primary node. Its available for read only requests.

Reasons for Adding Each Element:

Load Balancer (HAproxy): To distribute traffic across multiple web servers and provide high availability and scalability.

Web Servers (Nginx): To handle HTTP requests, load balancing, and reverse proxy for dynamic content.

Application Servers: To execute web application code and process user requests for dynamic content generation.

Database (Primary-Replica Cluster): To provide fault tolerance, high availability, and read scalability.


Load Balancer Distribution Algorithm:

The load balancer (HAproxy) is configured with a Round Robin distribution algorithm. It works by sequentially distributing incoming requests to each server in rotation. Each request is forwarded to the next server in the list, cycling through all available servers.


Active-Active vs. Active-Passive Setup:
Active-Active setup- bot servers atr active. The above load balancer enables the latter, Active-Passive setup, where when one server is receiving and processing traffic, the other remaina dormant, or on standbay to take over incase where the active server fails.This provides redundancy but may lead to underutilization of resources in the passive server.

Issues with this Infrastructure:
SPOF (Single Point of Failure): The load balancer is currently a single point of failure. If the load balancer goes down, the website will become inaccessible, and the traffic won't be balanced between the web servers.
Security Issues: Without firewalls, the servers are more susceptible to unauthorized access, and lacking HTTPS means data transmitted between users and the website is not encrypted, exposing it to potential eavesdropping and man-in-the-middle attacks.
No Monitoring: The absence of monitoring tools means there is no visibility into server health, performance, or potential issues. Monitoring is crucial for proactive issue detection and performance optimization.
