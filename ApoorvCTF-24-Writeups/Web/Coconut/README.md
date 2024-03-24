## Description

Coconuts are hard on the outside but soft in the inside!

Author: errorxyz\
Points: 100

## Writeup

1. After analyzing the source files we see that our input is encoded using the encode_me function and then compared to the SECRET variable in app.py
1. Our input is first reversed, then modified using the myfunc2 function
1. If we analyze the myfunc2 carefully, we see that it is nothing but base64 encoding
1. After base64 encoding, the code then does a ROT13 and then returns the resultant string
1. To solve the challenge, we'll have to do the above steps in reverse for the SECRET variable
1. Google ROT13 decode and enter the SECRET value on the website
1. Get resultant string from above website and base64 decode it
1. Reverse the string to get the answer to our input
1. Answer comes out to be: dGx8dVYv7lJkOVhwCn6Ye0H986x90tpt76udD4AJ9Wtc3GIbno76umNsNRdDfcc
1. Submitting this value gives us the flag

flag: apoorvctf{y0u_Kn0w_7h3_53cr37}
