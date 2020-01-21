# ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Disclaimer
Documents and associated codes are intended for educational purposes only.
Any actions and or activities related to the material contained within this
repository is solely your responsibility. The misuse of the information in
this repository can result in criminal charges brought against the persons in
question. The authors of tutorials will not be held responsible in the event
any criminal charges be brought against any individuals misusing the
information in this repository to break the law.

---

# ![#c5f015](https://placehold.it/15/fcdd16/000000?text=+) ![#c5f015](https://placehold.it/15/fcdd16/000000?text=+) Goal

Transform a switch into a hub.

# ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) Explanations
## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Requirements
<details>
<summary>What is the difference between a switch and a hub?</summary>

---
When it receive a frame a hub repeat it on all its ports and a switch will
send it on the port where the destination is, as illustrated below.
### Example:
![Hub operation](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/hub.png "Hub operation")

---

![Switch operation](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/switch.png "Switch operation")

So the next question is how the switch does that?

---
</details>

<details>
<summary>How a switch works?</summary>

---
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
 
And as the destination is mac@B, **the frame is sent to port 2**

---
</details>

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) So how to transform a switch into a hub?
The main idea is to saturate the learning table. So the attacker (you) will send lots of random MAC address in order to fill this table.
When the MAC Address Table is full and it is unable to save new MAC addresses, the switch goes to *fail-open* mode and starts acting as a hub and broadcasts the frames to all ports.

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) What are benefits of the attacker?
As the attacker is a part of the network, the attacker will also get the data packets intended for the victim machine. So that the attacker will be able to steal sensitive data from the communication of the victim and other computers.
Before the attack the switch work as shown below:

![Switch conventional use](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/switch-conventionnal-use.png)

After the attack the switch work as shown below:

![Switch after attack](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/switch-after-attack.png)

# ![#c5f015](https://placehold.it/15/f963a1/000000?text=+) ![#c5f015](https://placehold.it/15/f963a1/000000?text=+) A possible implementation
## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Requirements
<details>
<summary>Scapy</summary>

---
Before starting, some explication about [Scapy](https://scapy.net/). Scapy is used via a command-line interactive mode or inside Python scripts.Scapy has its own syntax, so you don’t need to know much Python to get started. As some of Scapy functions dealing with sending traffic, you will need to be able to **run Scapy as root**. You should be able to run it from the terminal (`sudo scapy`), just like we did with Python, and get something that looks like this:

![Start scapy and ls](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/scapy-lscmd.png "Start scapy and ls")

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

To know your interfaces (for Ubuntu) run `ip a`

---
</details>

<details>
<summary>ARP</summary>

---
The principle of ARP (Address Resolution Protocol) is just to have a correspondence table between L2 addresses and L3 addresses. 
L2 addresses are usually used to communicate in a local network and L3 addresses are usually used to communicate in internet.

### Example:
To illustrate the functioning, the next sketch illustrate briefly an architecture with all ARP tables. All computers known their MAC@ and IP@, and we suppose that all computers know the other IP@ (lines without MAC@ in tables are just for the illustration, in a real context there is no line with an empty field).
Also, there is possibly more address in the ARP tables (for example, the default gateway), but we will ignore them as we do not need them for the explication.

![ARP architecture example](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/arp-empty-table-archi.png)

We assume that a computer (A) connected to a computer network wishes to transmit an Ethernet frame to another computer (B).
**It only has the IP address and is placed in the same subnetwork.** (In our exemple, we will ping B with A and we will use A for the IP 192.168.1.12 and B for 192.168.1.58.)

![Ping](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/ping-58.PNG)

![Ping in Wireshark](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/ping-wireshark.PNG)


In this case, this computer (A) will hold its transmission and make an ARP request for a level 2 broadcast (Ethernet). 

He will ask "What is the MAC address of this IP address, answer me at this address" to all the elements on the network.

![ARP request in Wireshark](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/arp-ask1.PNG)

To do this, it will fill the ARP **operation field** with **01 which corresponds to a request (02 being a response)**, the source MAC and source IP field with its MAC and IP, the destination IP field with the IP of the computer where it wants the MAC address and finally the destination MAC which will simply be the broadcast address.

![ARP request detail](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/arp-detail1.png)

Since this is a broadcast, all computers in the segment will receive the request. By observing its content, they will be able to determine the IP address to which the search relates. The machine that has this IP address will be the only one to respond by sending the sending machine an ARP response such as "I am IP address, my MAC address is MAC address". To send this response to the right computer, it creates an entry in its ARP cache from the data contained in the ARP request it has just received.

![ARP reply in Wireshark](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/arp-reply1.png)

![ARP reply detail](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/arp-detail2.png)

The machine that made the ARP request receives the response, updates its ARP cache and can therefore send the message that it had put on hold to the computer concerned.
As you can see in our exemple, the ARP table does not contain B (192.168.1.58):

![ARP table before ping](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/arp-table.png)

After the table as been updated:

![ARP table after ping](https://github.com/adangla/network_attacks/raw/master/mac_flooding/img/arp-with-58.png)

---
</details>

## ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Our environment
In our case, we use the switch **Cisco Catalyst 2950** and the Python library [Scapy](https://scapy.net/). We will make ARP responses send in Ethernet with random source MAC addresses. It does not matter what do you put inside your Ethernet frame, the most important thing is that the frame is correct. We use ARP for educational purpose as we will use weakness of this protocol for next exercises.

---

# Authors
* **[Aliona DANGLA](https://github.com/adangla)**

See also the list of [contributors](https://github.com/adangla/network_attacks/contributors) who participated in this project.
