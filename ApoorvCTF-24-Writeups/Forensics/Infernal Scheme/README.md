Challenge Name: Infernal Scheme
Difficulty: medium: 200
Author: Abhinav Yadav
Category: Forensics

Description: Lucifer is planning something big, he has broken something into several fragments. Can you find it without getting lost ?

(hints are optional, max: 3)
Hint1: If you are lost, follow the stream
Hint1 cost: 15
Hint2: Have you ever crafted a web request ?
Hint2 cost: 30

Solution:
We are presented with a pcap file capturing traffic on the lucifer's machine.

### Step 1:

Firstly we gotta remove all the noise in the pcap file, like too many pings, arp requests, etc.
with `((((!(_ws.col.protocol == "ARP")) && !(_ws.col.protocol == "ICMP")) && !(_ws.col.protocol == "ICMPv6")) && !(_ws.col.protocol == "MDNS")) && !(_ws.col.protocol == "IGMPv3")` we can filter out all the noise captured in the pcap.
after that we are left with TCP, UDP and some HTTP traffic.

### Step 2:

In wireshark we can right click and then follow a TCP stream and we a bunch of basse64 strings.
![](images/Pasted%20image%2020240324122938.png)
which after deciphering gives out a conservation

```
mr.nobody: Status report. Did you find anything on Project, Lucifer?

Lucifer: I got in, Mr. Nobody. But their security is tight. They have got multiple layers of encryption, and everything is compartmentalized.

mr.nobody: Patience, Lucifer. We knew this would not be a walk in the park. Focus on their core systems. Finance, R&D, anything that might house something valuable.


Lucifer: That's what I've been doing. I finally found a restricted folder called "IT_核心资料" (IT_CoreData). Needs another level of clearance, though.


mr.nobody: Core data, huh? That sounds promising. Can you crack it?


Mole: I might be able to brute force it, but it'll take time and risk tripping an alert. There is another file within that folder called "flag.txt" that is flagged as highly confidential. That could be what we are looking for.


mr.nobody: Interesting. flag.txt, huh? Sounds like they are hiding something important. Do whatever you can to get that file, Lucifer. But be cautious. If things get too hairy, abort the mission.


Lucifer: Understood. I will see what I can do. But if this flag.txt is that important, they will have serious security measures in place. I might need further assistance.


mr.nobody: We'll discuss that when the time comes. Focus on getting that file for now. Remember, Lucifer, CLEAR all the traces of "drive links".


Lucifer: I will do so and I'll get you that flag.txt. One way or another.
```

In conversation its been discussed to delete the traces of drive link. flag must be retrieved from that drive link.

### Step 3:

There are some UDP packets as-well we must check them as-well.
We can see in them multiple base-64 strings are transmitted, which on deciphering gives out fake multiple flags.

- apoorvctf{try_harder}
- apoorvctf{ThI$_iS_n0T_(0rr3ct_f1@g}

### Step 4:

In another Stream of TCP we can see some file transfer has been done. As the transmission wasn't encrypted so we are able to read the content of the shared file.
![](images/Pasted%20image%2020240324130238.png)
File contains the browsing history of the employees. In that we found a 2/2 part of link in base-64 encoding.
after decoding se get `Jh0HwpTfv1ygQDtC4OSy5-4eXWvEM/view`

### Step 5:

Now only Http traffic is left to be analyzed, we can filter out the HTTP traffic.
![](images/Pasted%20image%2020240324130842.png)
There we found the 1/1 part of the link needed to get the flag.

### Step 6:

combining the both parts, we get: https://drive.google.com/file/d/1MmZJh0HwpTfv1ygQDtC4OSy5-4eXWvEM/view
going to this link gives out the Flag.
![](images/Pasted%20image%2020240324131504.png)

##### Final Flag: `apoorvctf{P@ck3t_$n1ff1Ng_I$_fuN}`
