# ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Disclaimer
Documents and associated codes are intended for educational purposes only.
Any actions and or activities related to the material contained within this
repository is solely your responsibility. The misuse of the information in
this repository can result in criminal charges brought against the persons in
question. The authors of tutorials will not be held responsible in the event
any criminal charges be brought against any individuals misusing the
information in this repository to break the law.

---

# ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Goal

Transform a switch into a hub.

# ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) Explanations
## What is the difference between a switch and a hub?
When it receive a frame a hub repeat it on all its ports and a switch will
send it on the port where the destination is, as illustrated below.
### Example:
![Hub operation](https://github.com/lyonaify/network_attacks/raw/master/mac_flooding/img/hub.png "Hub operation")
![Switch operation](https://github.com/lyonaify/network_attacks/raw/master/mac_flooding/img/switch.png "Switch operation")

So the next question is how the switch does that?

## How a switch works?
Compare to the hub, a switch contains a correspondence table between mac
addresses and ports called learning table. When a frame arrive in the
switch,the switch looks at the destination address of the frame, then deducts
the corresponding port in the learning table. And to fill this table, the
switch knows where the frame come from. For remember, an Ethernet frame
contain the source and the destination as shown below. There is more in Ethernet frame, but this is not necessary for this exercise.

| Destination MAC @ | Source MAC @ | Type |
| --- | --- | --- |

The switch have just to take the source and the port where it come from and put both together in the table.

### Example:
Refer to the previous picture, when **"A"** send a frame to **"B"** with a switch in the architecture. Imagine the switch has its table on the following state :

| MAC | Port |
| --- | --- |
| Mac@ B | Port 2 |
| Mac@ C | Port 3 |

When receiving the frame, it will see that it come from the **port 1** and the frame contain the **mac@ A in source** and **mac@ B in destination**.  The table is update :

| MAC | Port |
| --- | --- |
| Mac@ B | Port 2 |
| Mac@ C | Port 3 |
| Mac@ A | Port 1 |
 
And as the destination is mac@B, **the frame is sent to port 2.**

## So how to transform a switch into a hub?
The main idea is to saturate the learning table. So the attacker (you) will send lots of random MAC address in order to fill this table.
The switch goes to *fail-open* mode and starts acting as a hub and broadcasts the frames to all ports as MAC Address Table is full and it is unable to save new MAC addresses.

## What are benefits of the attacker?
As the attacker is a part of the network, the attacker will also get the data packets intended for the victim machine. So that the attacker will be able to steal sensitive data from the communication of the victim and other computers.


# ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) A possible implementation
In our case, we use the switch **Cisco Catalyst 2950** and the Python library [Scapy](https://scapy.net/). We will make ARP responses send in Ethernet with random source MAC addresses. It does not matter what do you put inside your Ethernet frame, the most important thing is that the frame is correct. We use ARP for educational purpose as we will use weakness of this protocol for next exercises.

## Scapy
Before starting, some explication about Scapy. Scapy is used via a command-line interactive mode or inside Python scripts.Scapy has its own syntax, so you don’t need to know much Python to get started. As some of Scapy functions dealing with sending traffic, you will need to be able to run Scapy as root. You should be able to run it from the terminal (`sudo scapy`), just like we did with Python, and get something that looks like this:

![Start scapy and ls](https://github.com/lyonaify/network_attacks/raw/master/mac_flooding/img/scapy-lscmd.png "Start scapy and ls")

As you can see, you can run the ls() function to see the fields and default values for any protocol as shown previously in the screenshot for ARP and Ethernet (`ls(ARP)`, `ls(Ether)`). 

**If you have multiple network interfaces on your computer**, you might have to double check which interface Scapy will use by default. Run scapy from the terminal and run the `conf` command. See what interface Scapy will use by default by looking at the `iface` value:
```
conf.iface
```
If the default interface is not the one you will use, you can change the value like this:
```
conf.iface="eth0"
```
*Instead of `eth0`, use the interface you want to be your default*

If you are constantly switching back and forth between interfaces, you can specify the interface to use in argument when you run Scapy commands.

## ARP
We assume that a computer connected to a computer network wishes to transmit an Ethernet frame to another computer of which it is not familiar. 
than the IP address of the latter and is placed in the same subnetwork.

In this case, this computer will put its transmission on hold and make an ARP request for a level 2 broadcast (Ethernet). 

He will ask "What is the MAC address of this IP address, answer me at this address" to all the elements on the network.
To do this, it will fill the ARP operation field with 01 which corresponds to a request (02 being a response), the source MAC and source IP field with its MAC and IP, the destination IP field with the IP of the computer where it wants the MAC address and finally the destination MAC which will simply be the broadcast address.

Since this is a broadcast, all computers in the segment will receive the request. By observing its content, they will be able to determine the IP address to which the search relates. The machine that has this IP address will be the only one to respond by sending the sending machine an ARP response such as "I am IP address, my MAC address is MAC address". To send this response to the right computer, it creates an entry in its ARP cache from the data contained in the ARP request it has just received.

The machine that made the ARP request receives the response, updates its ARP cache and can therefore send the message that it had put on hold to the computer concerned.

---

# Authors
* **[Aliona DANGLA](https://github.com/Lyonaify)**

See also the list of [contributors](https://github.com/Lyonaify/network_attacks/contributors) who participated in this project.
