Name: fuse

Description: Not a very good idea to send the password in plain text right after sending the encrypted file.

Hint: 	1. Follow the TCP streams (costs 50)
	2. There is a zip file split into two parts (costs 100)

Points:  300 (difficult)

Flag: ApoorvCTF{c4t_0r_h4xEd1t03?}

Category: Network

Writeup:
When you go through the pcap file, the TCP packets stand out.
Follow the first stream, and save it as raw binary.
The second stream is a conversation giving a clue about the upcoming packets.
The next stream is the other half of the file. Save this as raw binary too. Concatenate these two files using the linux cat command, or using a hex editor.
This will give you a password protected zip file.
The following TCP packets gives the password in plain text: "pArtalPass". Use this password to unzip the password protected zip, and read the text file containing the flag.
The flag is: ApoorvCTF{c4t_0r_h4xEd1t03?}
