## Description

I think its pretty secure now - my roomates aren't all that happy now. I don't think even you can break this now. I'll give you the source code too :))

Author: errorxyz\
Points: 300

## Writeup

1. We're now given the sourcecode for the backend.
1. We see that value of the stockid paramter in the /get_price endpoint is added to the URL of the internal endpoint
1. Visit (here)[https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#Syntax] to learn more about the syntax of a URL.
1. So, in a URL, anything before "@" if its present before the first "/" will be interpreted as credentials and the part
between "@" and "/" is interpreted as the domain name.
1. Vist "/get_price?stockid=@fbi.com:5002/" to get the flag

flag: apoorvctf{CONGRat5_yOU_ARE_s$Rf_ExpERt}
