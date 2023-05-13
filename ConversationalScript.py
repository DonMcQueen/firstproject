# This file will contain information related to a prompted conversation with Python. We are building a conversational bot for interested technical topics!

print("Hello, welcome to CloudLinuxSQL! Where we teach the basics of Cloud, Linux, SQL, Networking, and more to help you get started in your journey in technology!")

name = input("What is your name?\n")

topics = "Cloud, Linux, SQL, or Networking\n\n"

topic = input("Hi " + name + "! Welcome to CloudLinuxSQL! What technical topics are you interested in learning about today?\n" + topics)

if topic == "Cloud":
    print("Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider like Amazon Web Services (AWS).\n\n")
    
    cloudtopic = "Compute, Storage, Database, or IAM."

    cloud = input("Which cloud topics would you like more information about today?" + cloudtopic)

    if cloud == "Compute":
        print("Compute power is a virtual machine that represents a physical server for you to deploy your applications. Instead of purchasing your own hardware and connecting it to a network, the Cloud Service Provider gives you nearly unlimited virtual machines to run your applications while they take care of the hardware.")

    elif cloud == "Storage":
        print("Cloud storage is a cloud computing model that enables storing data and files on the internet through a cloud computing provider that you access either through the public internet or a dedicated private network connection. The provider securely stores, manages, and maintains the storage servers, infrastructure, and network to ensure you have access to the data when you need it at virtually unlimited scale, and with elastic capacity. Cloud storage removes the need to buy and manage your own data storage infrastructure, giving you agility, scalability, and durability, with any time, anywhere data access.")

    elif cloud == "Database":
        print("A cloud database is a database that is deployed, delivered, and accessed in the cloud. Cloud databases organize and store structured, unstructured, and semi-structured data just like traditional on-premises databases. However, they also provide many of the same benefits of cloud computing, including speed, scalability, agility, and reduced costs.")

    elif cloud == "IAM":
        print("Identity and Access Management (IAM) lets administrators authorize who can take action on specific resources, giving you full control and visibility to manage Cloud Service Provider resources centrally. For enterprises with complex organizational structures, hundreds of workgroups, and many projects, IAM provides a unified view into security policy across your entire organization, with built-in auditing to ease compliance processes.")

elif topic == "Linux":
    print("Linux® is an open source operating system (OS). An operating system is the software that directly manages a system’s hardware and resources, like CPU, memory, and storage. The OS sits between applications and hardware and makes the connections between all of your software and the physical resources that do the work.\n\n")

elif topic == "SQL":
    print("Structured query language (SQL) is a programming language for storing and processing information in a relational database. A relational database stores information in tabular form, with rows and columns representing different data attributes and the various relationships between the data values. You can use SQL statements to store, update, remove, search, and retrieve information from the database. You can also use SQL to maintain and optimize database performance.\n\n")

elif topic == "Networking":
    print("Computer networking refers to interconnected computing devices that can exchange data and share resources with each other. These networked devices use a system of rules, called communications protocols, to transmit information over physical or wireless technologies.\n\n")

else:
    print("Please reach out to don@cloudlinuxsql.com to see if CloudLinuxSQL teaches that topic, if that topic will be taught in the future, or if there are no plans to teach that topic.")