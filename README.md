# ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) ![#f03c15](https://placehold.it/15/f03c15/000000?text=+) Disclaimer
Documents and associated codes are intended for educational purposes only.
Any actions and or activities related to the material contained within this
repository is solely your responsibility. The misuse of the information in
this repository can result in criminal charges brought against the persons in
question. The authors of tutorials will not be held responsible in the event
any criminal charges be brought against any individuals misusing the
information in this repository to break the law.

---

# Cisco's switch command
## Know how many address is in the table 
`show mac-address-table count`

## Show current time
`show mac-address-table aging-time vlan 1`

## Change time
```
enable
conf t
mac-address-table aging-time <nb>
```
and `CTRL-Z` for quit config mode.

## Clear ARP's table
`enable`
`clear mac-address-table dynamic` 
