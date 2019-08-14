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
send it on the port where the destination is. So the next question is how the
switch does that?

## How a switch works?
Compare to the hub, a switch contains a correspondence table between mac
addresses and ports called learning table. When a frame arrive in the
switch,the switch looks at the destination address of the frame, then deducts
the corresponding port in the learning table. And to fill this table, the
switch knows where the frame come from. For remember, an Ethernet frame
contain the source and the destination, so switch have just to take the
source and the port where it come from and put both together in the table.
And that enought to understand the attack!

## So how to transform a switch into a hub?
The main idea is to saturate the learning table. So the attacker (you) will send lots of random MAC address in order to fill this table.
The switch goes to *fail-open* mode and starts acting as a hub and broadcasts the frames to all ports.

# ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Solution

---

# Authors
* **[Aliona DANGLA](https://github.com/Lyonaify)**

See also the list of [contributors](https://github.com/Lyonaify/network_attacks/contributors) who participated in this project.
