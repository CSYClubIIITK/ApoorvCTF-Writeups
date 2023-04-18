Name: dementia

Description: The user forgot about the existence of HTTPS. Wonder why...

Hint: Search for GET requests (costs 100)

Points:  250 (medium-difficult)

Flag: ApoorvCTF{wH#_£v€N_u53s_H]|p}

Category: Network

Solution:
Challenge description hints that the flag is hidden in some HTTP request. Open the given pcap file in wireshark and type http in the display filter to view only http requests/responses. Now sort it by info to group the http requests. We can now see the URL encoded flag in the third http request. Decode it using some online URL decoder tool to get the flag.

Author: Rohith