## Description

I think I've figured out what's wrong. Or have I?

Author: errorxyz\
Points: 200

## Writeup

1. If we try to use the same method for stocks1, we see that we receive a message: "Haha not gonna happen again :)"
1. So probably, we have some URL filtering occuring in the backend.
1. Trying to use "http://127.0.0.1:5002/" also fails
1. So probably, strings refering to localhost are being blocked.
1. Instead if we use some domain that resolves to 127.0.0.1, we can use that to access the login panel - fbi.com resolves
to 127.0.0.1
1. So now if we visit "/get_price?url=http://fbi.com:5002/" we get the flag

flag: apoorvctf{Dn$_1snt_dNSinG}
