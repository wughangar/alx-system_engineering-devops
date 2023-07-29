Infrastructure Explanation
Server - Its a physical machine or virtual instance that hosts the entire web infrastructure.Its responsible for:
    database
    serving web pages
    processing requests
    managing the application

Domain name - is a human readable address/text used to access the website. ie foobar.com. it is the configured to a systems public ip adress. 

DNS record type- 'www':
    its a DNS CNAME record. its an alias the points to the main/ root domain. CNAME record allows users to access websites from alias and root name, ir- www.foobar.com or foobar.com

Web Server (Nginx):
The web server (Nginx) handles incoming HTTP requests from the users' web browsers. It serves static content and forwards dynamic requests to the application server.

Application Server:
The application server executes the web application code and generates dynamic content based on user requests. It communicates with the database to fetch and store data.

Database (MySQL):
The database (MySQL) stores the website's data, such as user information, posts, or any other information required by the web application.

Communiaction from user to server computor
The server communicates with users' computers using HTTP (Hypertext Transfer Protocol) over the internet. The user's web browser sends HTTP requests to the server, which processes the requests and sends back HTTP responses containing the requested web pages or data.


Issues with the Infrastructure:
Single Point of Failure (SPOF):
The entire infrastructure is dependent on a single server. If the server experiences hardware failure or crashes, the website will become inaccessible until the issue is resolved.

Downtime during Maintenance:
During maintenance tasks like deploying new code or updating the web server, the website may experience downtime. Restarting the web server, for example, may lead to temporary unavailability.

Limited Scalability:
This one-server setup has limited capacity to handle a significant increase in incoming traffic. If the website experiences a traffic surge, it may lead to performance degradation or downtime.

These issues can be addressed by:
Load balancing to disribute traffic
scalable infrastructure 
