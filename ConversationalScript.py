# This file will contain information related to a prompted conversation with Python. We are building a conversational bot for interested technical topics!

print("Hello, welcome to CloudLinuxSQL! Where we teach the basics of Cloud, Linux, SQL, Networking, and more to help you get started in your journey in technology!")

name = input("What is your name?\n")

topics = "Cloud, Linux, SQL, or Networking\n\n"

topic = input("Hi " + name + "! Welcome to CloudLinuxSQL! What technical topics are you interested in learning about today?\n\n" + topics).upper()

if topic == "CLOUD":
    print("\nCloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider like Amazon Web Services (AWS).\n\n")
    
    cloudtopic = "Compute, Storage, Database, or IAM.\n\n"

    cloud = input("Which Cloud topics would you like more information about today? " + cloudtopic).upper()

    if cloud == "COMPUTE":
        print("\nCompute power is a virtual machine that represents a physical server for you to deploy your applications. Instead of purchasing your own hardware and connecting it to a network, the Cloud Service Provider gives you nearly unlimited virtual machines to run your applications while they take care of the hardware.")

    elif cloud == "STORAGE":
        print("\nCloud storage is a cloud computing model that enables storing data and files on the internet through a cloud computing provider that you access either through the public internet or a dedicated private network connection. The provider securely stores, manages, and maintains the storage servers, infrastructure, and network to ensure you have access to the data when you need it at virtually unlimited scale, and with elastic capacity. Cloud storage removes the need to buy and manage your own data storage infrastructure, giving you agility, scalability, and durability, with any time, anywhere data access.")

    elif cloud == "DATABASE":
        print("\nA cloud database is a database that is deployed, delivered, and accessed in the cloud. Cloud databases organize and store structured, unstructured, and semi-structured data just like traditional on-premises databases. However, they also provide many of the same benefits of cloud computing, including speed, scalability, agility, and reduced costs.")

    elif cloud == "IAM":
        print("\nIdentity and Access Management (IAM) lets administrators authorize who can take action on specific resources, giving you full control and visibility to manage Cloud Service Provider resources centrally. For enterprises with complex organizational structures, hundreds of workgroups, and many projects, IAM provides a unified view into security policy across your entire organization, with built-in auditing to ease compliance processes.")

elif topic == "LINUX":
    print("\nLinux® is an open source operating system (OS). An operating system is the software that directly manages a system’s hardware and resources, like CPU, memory, and storage. The OS sits between applications and hardware and makes the connections between all of your software and the physical resources that do the work.\n\n")

    linuxtopic = "Servers, Mobile, IoT, or Super Computing.\n\n"

    linux = input("Which Linux topics would you like to learn more information about today? " + linuxtopic).upper()
    
    if linux == "SERVERS":
        print("\nA Linux server is a server running a variant of the Linux open source operating system (OS). It is designed to handle the most demanding business applications, such as web services and databases. Linux servers provide a strong foundation for complex, enterprise-level data centers and workload environments, ranging from bare metal to virtual machines, and containers, including private or public clouds. They can also guide your digital transformation journey and cloud app development, with the capability to increase productivity, deliver services faster, and incorporate software innovations like cloud, containers, and configuration automation.")

    elif linux == "MOBILE":
        print("\nLinux for mobile devices, sometimes referred to as mobile Linux, is the usage of Linux-based operating systems on portable devices, whose primary or only Human interface device (HID) is a touchscreen. It mainly comprises smartphones and tablet computers, but also some mobile phones, personal digital assistants (PDAs) portable media players that come with a touchscreen separately. Mobile Linux is a relatively recent addition to the Linux range of use, with Google's Android operating system pioneering the concept.")

    elif linux == "IOT":
        print("\nLinux OSs account for the majority of IoT operating systems. Linux was the first open-source operating system, designed to be as versatile and capable as possible. It runs equally well on mainframes, servers, and tiny devices like Raspberry Pis. It’s one of the most-used server OSs because of this. (Nearly every successful OS now owes a lot to Linux: Windows and Mac OS are both based on it, and Android is a skin over a Linux kernel.)")

    elif linux == "SUPER COMPUTING":
        print("\nSupercomputers are used for data-intensive and computation-heavy scientific and engineering purposes such as quantum mechanics, weather forecasting, oil and gas exploration, molecular modeling, physical simulations, aerodynamics, nuclear fusion research and cryptoanalysis. Early operating systems were custom made for each supercomputer to increase its speed. In recent years, supercomputer architecture has moved away from proprietary, in-house operating systems to Linux. Although most supercomputers use a Linux-based operating system, each manufacturer optimizes its own Linux derivative for peak hardware performance. In 2017, half of the world’s top 50 supercomputers used SUSE Enterprise Linux Server.")

elif topic == "SQL":
    print("\nStructured query language (SQL) is a programming language for storing and processing information in a relational database. A relational database stores information in tabular form, with rows and columns representing different data attributes and the various relationships between the data values. You can use SQL statements to store, update, remove, search, and retrieve information from the database. You can also use SQL to maintain and optimize database performance.\n\n")

    sqltopic = "Datatypes, Relational Databases, Clauses, or Data Structure.\n\n"

    sql = input("Which SQL topics would you like to learn more information about today? \n\n" + sqltopic).upper()

    if sql == "DATATYPES":
        print("\nDatatypes in SQL are used to define the type of data that can be stored in a column of a table, like, INT, CHAR, MONEY, DATETIME etc. They provide guidelines for SQL to understand what type of data is expected inside each column, and they also identify how SQL will interact with the stored data. The datatype specification, hence, prevents the user from entering any unexpected or invalid data.")

    elif sql == "RELATIONAL DATABASES":
        print("\nA relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables. In a relational database, each row in the table is a record with a unique ID called the key. The columns of the table hold attributes of the data, and each record usually has a value for each attribute, making it easy to establish the relationships among data points. Some of the most well-known RDBMSs include MySQL, PostgreSQL, MariaDB, Microsoft SQL Server, and Oracle Database.")

    elif sql == "CLAUSES":
        print("\nA clause in SQL is a built-in function that helps to fetch the required records from a database table. A clause receives a conditional expression, i.e. a column name or some terms involving the columns. The clause calculates the result based on the given statements in the expression. The main clauses are SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, INSERT, UPDATE, DELETE, and JOIN. Each clause has a syntax and its own set of rules and options. They can also be used in combination to create complex queries.")

    elif sql == "DATA STRUCTURES":
        print("\nData structures are a fundamental part of any digital system, providing a way to organize and store data in an efficient manner. They help reduce the time it takes to access and use data, as well as the amount of memory needed to store it. By using data structures, data can be quickly searched, sorted, and retrieved. They are a fundamental component of computer science and software engineering.")

elif topic == "NETWORKING":
    print("\nComputer networking refers to interconnected computing devices that can exchange data and share resources with each other. These networked devices use a system of rules, called communications protocols, to transmit information over physical or wireless technologies.\n\n")

    networkingtopic = "DNS, Network, IP Addressing, or Route Tables.\n\n"

    network = input("Which Network topics would you like to learn more information about today? \n\n" + networkingtopic).upper()

    if network == "DNS":
        print("\nThe Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources. Each device connected to the Internet has a unique IP address which other machines use to find the device. DNS servers eliminate the need for humans to memorize IP addresses such as 192.168.1.1 (in IPv4), or more complex newer alphanumeric IP addresses such as 2400:cb00:2048:1::c629:d7a2 (in IPv6).")

    elif network == "NETWORK":
        print("\nIn information technology, a network is defined as the connection of at least two computer systems, either by a cable or a wireless connection. The simplest network is a combination of two computers connected by a cable. This type of network is called a peer-to-peer network. There is no hierarchy in this network; both participants have equal privileges. Each computer has access to the data of the other device and can share resources such as disk space, applications or peripheral devices (printers, etc.). Today’s networks tend to be a bit more complex and don’t just consist of two computers. Systems with more than ten participants usually use client-server networks. In these networks, a central computer (server) provides resources to the other participants in the network (clients).")

    elif network == "IP ADDRESSING":
        print("\nAn IP address is a 32-bit number. It uniquely identifies a host (computer or other device, such as a printer or router) on a TCP/IP network. IP addresses are normally expressed in dotted-decimal format, with four numbers separated by periods, such as 192.168.123.132. To understand how subnet masks are used to distinguish between hosts, networks, and subnetworks, examine an IP address in binary notation. For example, the dotted-decimal IP address 192.168.123.132 is (in binary notation) the 32-bit number 11000000101010000111101110000100. This number may be hard to make sense of, so divide it into four parts of eight binary digits. These 8-bit sections are known as octets. The example IP address, then, becomes 11000000.10101000.01111011.10000100. This number only makes a little more sense, so for most uses, convert the binary address into dotted-decimal format (192.168.123.132). The decimal numbers separated by periods are the octets converted from binary to decimal notation.")

    elif network == "ROUTE TABLES":
        print("\nA routing table is a set of rules, often viewed in table format, that's used to determine where data packets traveling over an Internet Protocol (IP) network will be directed. The main purpose of a routing table is to help routers make effective routing decisions. Whenever a packet is sent through a router to be forwarded to a host on another network, the router consults the routing table to find the IP address of the destination device and the best path to reach it. The packet is then directed to a neighboring router -- or the next hop listed in the table -- until it reaches its final destination.")

else:
    print("Please reach out to don@cloudlinuxsql.com to see if CloudLinuxSQL teaches that topic, if that topic will be taught in the future, or if there are no plans to teach that topic.")