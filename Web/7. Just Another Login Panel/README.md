Just Another Login Panel

Jason has decided to host a login portal just after learning about a new technology, but he has made a blunder. Help him realise his mistake.
link: https://jwtlog-yymsncndoq-uc.a.run.app/

You are provided with the source code of the application.

300pts(hard)
ApoorvCTF{dOn7_exp053_yOur_K3yS}
no hints
web exploitation
#web

Writeup:
If you're new to JWT refer to this article: https://jwt.io/introduction

A weird text can be seen in the source code of the index page, we'll note it down for future use.
From the source code, we can see that test:test would allow us to login.
Upon logging in, we are assigned a JWT signed using RS256(arriving at this conclusion from source code)
Search for jwt parsers on google -> click on jwt.io and paste your jwt
So we now need to change username to admin in order to get the flag.
Analyzing the dashboard function in app.py from the source code, we see that the server accepts RS256 signed and HS256 signed keys.
Now since RS256 uses public private keys, and we dont have access to it, it is difficult to alter it if we use that algorithm for signing it
Instead, HS256 might be more likely to be exploitable since it uses a single key for encryption and decryption and the weird text that we saw might very likely be the secret key
On the jwt.io website, after pasting the assigned JWT, change algo value to HS256 and username value to admin and put the secret key in the appropriate field to get the new JWT
Change your cookie to the new JWT and access /dashboard/admin to get the flag