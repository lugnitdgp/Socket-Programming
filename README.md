# Socket-Programming

A repository on my steps to learn socket programs...This is a set of single user-client programs on a single host computer...further advancements are yet to be made...this is just the beginning.

Feel free to contribute to this repository and report any issues occuring.

**Contributing Guide**
Please see the contributing guide of github.

***

# Socket basics
Programmers use sockets to communicate between proccesses or devices. They are somewhat similar to I/O operations, because they behave similarly to files.
---
Sockets are used in someting called a "client-server" application. A server sends info, then the client interpretes that info and returns some other data. The data flows both ways, of course.

## Types of sockets
There are four types of sockets:
- Stream sockets (delivery is guaranteed, the same goes for order of sent packets. An error is received if the transmission can't be completed)
- Sequenced packets sockets (similar to stream, but allows specifying header data of packets. Additionally, record boundaries are preserved)
- Raw sockets (a socket type with access to underlying protcols. Not intended for the general user, used for developing new protocols)
- Datagram sockets (delivery is, unlike with stream sockets, not guaranteed. These sockets use UDP (User Datagram Protocol))

## Connecting to a server/client
Every host has an IP address that you can connect to. There are many types of IP addresses, which will not be explained here, please refer to [this tutorial](https://www.tutorialspoint.com/unix_sockets/network_addresses.htm).
If you wish to connect to your own machine, there is a special address reserved for that: **127.0.0.1** or **localhost**.
When you're connecting to a socket, you must specify a port number. Ports are like windows but for connections. There is a huge amount of ports available (0-65535). Many are reserved for day-to-day stuff (like 80, for http), so make sure you pick a high-enough number for your socket.

## Speficication
A complete specification for the TCP protocol is available [here](http://www.faqs.org/rfcs/rfc793.html)