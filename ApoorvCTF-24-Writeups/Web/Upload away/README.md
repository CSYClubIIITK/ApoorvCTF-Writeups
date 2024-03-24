## Description:
Ted's made a website for Barney to upload all his photos, but he doesn't realise that Barney is really good at breaking things. Help Ted fix his website.

Hint: Burp's your friend :))

Author: Kumarjit\
Points : 200

## Writeups:
upload php rev-shell but its not allowed so you need to use burpsuite to content-type:  to any valid content eg:(jpg,image/jpg,png etc) ex: content-type: image/jpg 
after that your file uploaded on http://uploadchal.apoorvctf.xyz/@@shell_name@@.php 
then execute it.
you find flags in /var/flag.txt  
