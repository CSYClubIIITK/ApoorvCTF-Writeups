Challenge Name: Ask key
Difficulty: easy: 100
Author: Abhinav Yadav
Category: Forensics

Description: Get the flag using Ask Key.

Solution:
From the name we get something ahs to do with "ASCII".

### Step 1:

Opening and analyzing the pcap file given. We can spot many `icmp` packets along with some `arp` packets.
After filtering out `icmp` packets we need to look for some hints for `ASCII`, we can notice the size as it is the only numerical field visible that can be ASCII values.

### Step 2:

Extract the sizes of the icmp packets and covert those to text using ascii to text convertor.

### Step 3:

![](images/Pasted%20image%2020240324085543.png)\
From the decoded string we can see repetition of similar characters, this could mean there are 2 flags and 1 of them is correct.

### Step 4:

Now filter the icmp packet requests and response separately.

- flag from request packet sizes\
  ![](images/Pasted%20image%2020240324090134.png)\
- flag from response packet sizes\
  ![](images/Pasted%20image%2020240324090302.png)\
  In this case flag coming out of request packet size is the correct flag.

##### Final Flag: apoorvctf{SIz<\_M@tt<R}
