# ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) ![#c5f015](https://placehold.it/15/c5f015/000000?text=+) Requirements
* [What is the difference between a hub and a switch?](https://github.com/adangla/network_attacks/blob/master/misc/diff_switch_hub.md)

# ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) ![#1589F0](https://placehold.it/15/1589F0/000000?text=+) How a switch works?
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
 
And as the destination is mac@B, **the frame is sent to port 2

---

# Authors
* **[Aliona DANGLA](https://github.com/adangla)**

See also the list of [contributors](https://github.com/adangla/network_attacks/contributors) who participated in this project.
