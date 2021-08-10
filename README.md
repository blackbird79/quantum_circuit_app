# Quantum Circuit App
In this exercise I implement platform that facilitates execution and analysis of quantum circuits.
1. Api which accepts a QASM file, analyze and return basic properties.
2. Api which accepts a QASM file,simulate it with IBM simulators and return the results (meanwhile in 
json and not histograms)
3. This was done with django framework with ViewSet and Serializer and also with some client side to test 
the server.
4. Log mechanism was added through logging library of django (can be extended with adding logging configuration).
5. Added sample tests of the analyze Api (can be extended with the simulate Api and also with more edge case tests).
Also, I used this github for manual testing (https://github.com/pnnl/QASMBench).
6.Unfortunately I don't have time for dockerfile and authentication. I started the authentication task with 
django authentication but didn't finish it.
7. I chose Django for the following reasons:
- Django includes dozens of functionality which we can use to handle the required development tasks.
- It's easier for to add functionality by integrating external Django applications into the project.
- It's secure by default.
8. Scaling- if we have more clients or intensive resources for each request - we can use load balancer or cache (Memcache or Redis) to store data on another 
server to achieve statelessnes. Also, to achieve horizontal scaling, we can use microservices- splitting applications to individual
services help in scaling them individually as the load increases (in the cost of communication among services).
Another way to reduce the request/response time is by removing the extra middleware that the app is not benefiting from.

