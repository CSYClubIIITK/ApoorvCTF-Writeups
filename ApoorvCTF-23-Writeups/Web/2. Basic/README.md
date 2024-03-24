Our developer has made an online Linux shell with only basic commands - see if you can break it?

100pts(easy)
ApoorvCTF{c0mMAnd_INjEc7iON_f7w}
hint cost: 50pts
hint: the websites seems to be validating user input only on the client side. See if you can bypass it.
web exploiation
#web #commondinjection

Writeup:
if you're not familiar with burp suite and intercepting requets read: https://www.geeksforgeeks.org/what-is-burp-suite/

The website takes user input and executes it on the server and returns its output.
The commands allowed to run seem to be limited and whitelised on the client side(using javascript which can be analyzed from the browser tools)
We can try intercepting one of the requests using burp suite and change the value of command to "cat flag.txt" and access the flag.