The sneaky librarian has hidden the flag inside this library. You have been appointed by the IIITK Bureau of Investigation to find it ASAP!

200pts(med)
apoorvCTF{1dor5_ar3_ea5y_p3Asy}
hint cost: 50pts
hint: try to access books beyond what is shown.
web exploitation
#web #IDOR

Writeup:
Accessing books beyond what is shown that is /books/11 or /books/12 and so on seem to valid.
We can automate this bruteforcing task using burp intruder.
Intercept the request to any of the book details and send to intruder.
Mark the portion after /books/ in the URL as the target and set payloads to numbers from 1-100.
Also set grep - match under intruder settings to "ApoorvCTF" and start attack.
You will see that it is matched for /books/32 and has the flag in the authors name section.