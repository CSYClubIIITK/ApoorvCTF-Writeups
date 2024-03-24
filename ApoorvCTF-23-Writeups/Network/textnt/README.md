Name: textnt

Description: Find the flag in the pcap file.

Hint: Follow the TCP stream (costs 100)

Points:  200(medium)

Flag: ApoorvCTF{audioflag}

Category: Network

Solution:
Open the pcap file using wireshark.
You will find a long TCP conversation.
Right click on any of the TCP packets and follow the TCP stream.
Save this stream as raw binary.
Running the 'file' command on the saved binary reveals that its and mp3 file.
Open the file using an audio player and listen to the audio to get the flag.
ApoorvCTF{audioflag}
