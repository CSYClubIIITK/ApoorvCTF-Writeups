Challenge Name: Creepy Husband
Difficulty: Medium - 200
Author: Cybertooths
Category: Cryptography


Description:
We were talking to a lost woman in the carnival on the help desk but lost connection due to network misconfigurations. Before disconnecting she sent us this strange image. Can you help us find what she wanted to say?

Flag Format: apoorvctf{Firstname_Lastname}


Tags: 
1. Base64
2. OSINT


Solution:
The challenge provides us with an image "output.png"
Seeing the tags, which says "OSINT" and "Base64"
Now it's sure we have to try OSINT on this challenge. But not initially.
When we check the metadata of the image, there is a comment which says, "Trying OSINT at this stage? LOL"
This clearly indicates that this isn't the right time for OSINT. So we try using "strings" command on it and we get a strange text which is:
"VDFHOXlaVzBnYVhCemRXMGdJNG10aDNQNHNTdzByZFpHOXNiM0lnYzJsMElHRnRaWFFzSUdOdmJuTmxZM1JsZEhWeUlHRmthWEJwYzJOcGJtY2daV3hwZEN3Z2MyVmtJR1J2SUdWcGRYTnRiMlFnZEdWdGNHOXlJR2x1WTJsa2FXUjFiblFnZFhRZ2JHRmliM0psSUdWMElHUnZiRzl5WlNCdFlXZHVZU0JoYkdseGRXRXVJRVZzYVhRZ2MyTmxiR1Z5YVhOeGRXVWdiV0YxY21seklIQmxiR3hsYm5SbGMzRjFaU0J3ZFd4MmFXNWhjaUJ3Wld4c1pXNTBaWE54ZFdVZ2FHRmlhWFJoYm5RZ2JXOXlZbWtnZEhKcGMzUnBjWFZsSUhObGJtVmpkSFZ6TGlCTlpYUjFjeUJrYVdOMGRXMGdZWFFnZEdWdGNHOXlJR052YlcxdlpHOGdkV3hzWVcxamIzSndaWElnWVNCc1lXTjFjeUIyWlhOMGFXSjFiSFZ0SUhObFpDNGdUbVZqSUdabGRXZHBZWFFnYVc0Z1ptVnliV1Z1ZEhWdElIQnZjM1ZsY21VZ2RYSnVZU0J1WldNZ2RHbHVZMmxrZFc1MExpQk5ZWFIwYVhNZ2NtaHZibU4xY3lCMWNtNWhJRzVsY1hWbElIWnBkbVZ5Y21FZ2FuVnpkRzh1SUVkeVlYWnBaR0VnY1hWcGN5QmliR0Z1WkdsMElIUjFjbkJwY3lCamRYSnpkWE1nYVc0Z2FHRmpJR2hoWW1sMFlYTnpaU0J3YkdGMFpXRXVJRkpwYzNWeklIVnNkSEpwWTJsbGN5QjBjbWx6ZEdseGRXVWdiblZzYkdFZ1lXeHBjWFZsZENCbGJtbHRJSFJ2Y25SdmNpQmhkQ0JoZFdOMGIzSXVJRVZuWlhOMFlYTWdjMlZrSUhObFpDQnlhWE4xY3lCd2NtVjBhWFZ0SUhGMVlXMHVJRkYxYVhNZ2FYQnpkVzBnYzNWemNHVnVaR2x6YzJVZ2RXeDBjbWxqWlhNZ1ozSmhkbWxrWVNCa2FXTjBkVzBnWm5WelkyVWdkWFF1SUVOdmJuTmxZM1JsZEhWeUlIQjFjblZ6SUhWMElHWmhkV05wWW5WeklIQjFiSFpwYm1GeUlHVnNaVzFsYm5SMWJTQnBiblJsWjJWeUlHVnVhVzB1SUZOalpXeGxjbWx6Y1hWbElHWmxjbTFsYm5SMWJTQmtkV2tnWm1GMVkybGlkWE1nYVc0Z2IzSnVZWEpsSUhGMVlXMHVJRUZrYVhCcGMyTnBibWNnWld4cGRDQjFkQ0JoYkdseGRXRnRJSEIxY25WeklITnBkQ0JoYldWMElHeDFZM1IxY3k0Z1FXUnBjR2x6WTJsdVp5QjJhWFJoWlNCd2NtOXBiaUJ6WVdkcGRIUnBjeUJ1YVhOc0xpQlZiSFJ5YVdOcFpYTWdkSEpwYzNScGNYVmxJRzUxYkd4aElHRnNhWEYxWlhRZ1pXNXBiUzRnUlhVZ2JtbHpiQ0J1ZFc1aklHMXBJR2x3YzNWdElHWmhkV05wWW5WeklIWnBkR0ZsSUdGc2FYRjFaWFFnYm1WakxnPT0="

Seeing the "=" at the end, anyone would confirm that it's base64. So we try to solve it and get another strange string: 
"T1G9yZW0gaXBzdW0gI4mth3P4sSw0rdZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdCwgc2VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWduYSBhbGlxdWEuIEVsaXQgc2NlbGVyaXNxdWUgbWF1cmlzIHBlbGxlbnRlc3F1ZSBwdWx2aW5hciBwZWxsZW50ZXNxdWUgaGFiaXRhbnQgbW9yYmkgdHJpc3RpcXVlIHNlbmVjdHVzLiBNZXR1cyBkaWN0dW0gYXQgdGVtcG9yIGNvbW1vZG8gdWxsYW1jb3JwZXIgYSBsYWN1cyB2ZXN0aWJ1bHVtIHNlZC4gTmVjIGZldWdpYXQgaW4gZmVybWVudHVtIHBvc3VlcmUgdXJuYSBuZWMgdGluY2lkdW50LiBNYXR0aXMgcmhvbmN1cyB1cm5hIG5lcXVlIHZpdmVycmEganVzdG8uIEdyYXZpZGEgcXVpcyBibGFuZGl0IHR1cnBpcyBjdXJzdXMgaW4gaGFjIGhhYml0YXNzZSBwbGF0ZWEuIFJpc3VzIHVsdHJpY2llcyB0cmlzdGlxdWUgbnVsbGEgYWxpcXVldCBlbmltIHRvcnRvciBhdCBhdWN0b3IuIEVnZXN0YXMgc2VkIHNlZCByaXN1cyBwcmV0aXVtIHF1YW0uIFF1aXMgaXBzdW0gc3VzcGVuZGlzc2UgdWx0cmljZXMgZ3JhdmlkYSBkaWN0dW0gZnVzY2UgdXQuIENvbnNlY3RldHVyIHB1cnVzIHV0IGZhdWNpYnVzIHB1bHZpbmFyIGVsZW1lbnR1bSBpbnRlZ2VyIGVuaW0uIFNjZWxlcmlzcXVlIGZlcm1lbnR1bSBkdWkgZmF1Y2lidXMgaW4gb3JuYXJlIHF1YW0uIEFkaXBpc2NpbmcgZWxpdCB1dCBhbGlxdWFtIHB1cnVzIHNpdCBhbWV0IGx1Y3R1cy4gQWRpcGlzY2luZyB2aXRhZSBwcm9pbiBzYWdpdHRpcyBuaXNsLiBVbHRyaWNpZXMgdHJpc3RpcXVlIG51bGxhIGFsaXF1ZXQgZW5pbS4gRXUgbmlzbCBudW5jIG1pIGlwc3VtIGZhdWNpYnVzIHZpdGFlIGFsaXF1ZXQgbmVjLg=="

Now here comes the tricky part. If you see the "==" again, you may think it is again encoded with base64 but it isn't. Even if you try to solve it, you'll get a string in non-printable characters.
Hence you need to go another way.
If you closely analyse the decoded base64 string, you'll find that it contains a another string which says, "I4mth3P4sSw0rd" in the beginning of it. Now few people may try to use it to extract the files using steghide, but will fail because it's not the correct password. 
The password that you have to use is the complete decoded string, which is:
"T1G9yZW0gaXBzdW0gI4mth3P4sSw0rdZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdCwgc2VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWduYSBhbGlxdWEuIEVsaXQgc2NlbGVyaXNxdWUgbWF1cmlzIHBlbGxlbnRlc3F1ZSBwdWx2aW5hciBwZWxsZW50ZXNxdWUgaGFiaXRhbnQgbW9yYmkgdHJpc3RpcXVlIHNlbmVjdHVzLiBNZXR1cyBkaWN0dW0gYXQgdGVtcG9yIGNvbW1vZG8gdWxsYW1jb3JwZXIgYSBsYWN1cyB2ZXN0aWJ1bHVtIHNlZC4gTmVjIGZldWdpYXQgaW4gZmVybWVudHVtIHBvc3VlcmUgdXJuYSBuZWMgdGluY2lkdW50LiBNYXR0aXMgcmhvbmN1cyB1cm5hIG5lcXVlIHZpdmVycmEganVzdG8uIEdyYXZpZGEgcXVpcyBibGFuZGl0IHR1cnBpcyBjdXJzdXMgaW4gaGFjIGhhYml0YXNzZSBwbGF0ZWEuIFJpc3VzIHVsdHJpY2llcyB0cmlzdGlxdWUgbnVsbGEgYWxpcXVldCBlbmltIHRvcnRvciBhdCBhdWN0b3IuIEVnZXN0YXMgc2VkIHNlZCByaXN1cyBwcmV0aXVtIHF1YW0uIFF1aXMgaXBzdW0gc3VzcGVuZGlzc2UgdWx0cmljZXMgZ3JhdmlkYSBkaWN0dW0gZnVzY2UgdXQuIENvbnNlY3RldHVyIHB1cnVzIHV0IGZhdWNpYnVzIHB1bHZpbmFyIGVsZW1lbnR1bSBpbnRlZ2VyIGVuaW0uIFNjZWxlcmlzcXVlIGZlcm1lbnR1bSBkdWkgZmF1Y2lidXMgaW4gb3JuYXJlIHF1YW0uIEFkaXBpc2NpbmcgZWxpdCB1dCBhbGlxdWFtIHB1cnVzIHNpdCBhbWV0IGx1Y3R1cy4gQWRpcGlzY2luZyB2aXRhZSBwcm9pbiBzYWdpdHRpcyBuaXNsLiBVbHRyaWNpZXMgdHJpc3RpcXVlIG51bGxhIGFsaXF1ZXQgZW5pbS4gRXUgbmlzbCBudW5jIG1pIGlwc3VtIGZhdWNpYnVzIHZpdGFlIGFsaXF1ZXQgbmVjLg=="

Use it as the password for steghide, and a zip file will be extracted wich the name "ticket.zip" 
Unzip it and you'll again get an image "alternate_indie_pop.png" which is a music genre, a message "message.txt" from the lady mentioned in the description, and a text from the author "note_for_you.txt".

The text from the author says: "Sometimes you may get fooled. I mean, attention is just as important in cryptography as the keys themselves being kept secret. Even if the password is right in front of you, you choose to disregard it."
This says that attention is equally important as the keys being secret, which he may successfully kept a secret even keeping the password for steghide in front of you.

The message from the lady is again encoded using base64. On decrypting it, we get: 
"Helpdesk! My ex-husband and I went to the carnival together. What a creep he is. I chose to pursue a divorce from him due of his actions, which left me in this eerie spot at the carnival. 2020 brought our separation, yet we still go on some new adventures together. I need your help to get my hubby. I cannot disclose you my name for any reason, perhaps related to my previous employment. 
I'll be sending you a screenshot of the music video. I'm really recognized even though I'm not a musician or vocalist. If you recognize me, just look for my husband and ask him privately to get me out of here."

It's clear from this message and flag format that we need to find this lady, and then her ex-husband. Full name of her ex-husband is the flag.
If we do image search on the image we got from ticket.zip we get to know that the song is "Build a B*tch" by Bella Poarch. We dig deeper into the music video and found all the people starring in it we found a list in the description of YouTube video:
STARRING:
Bella Poarch 
Valkyrae
Mia Khalifa 
Dina 
Larray 
ZHC 
Rakhim 
Bretman Rock
Sub Urban

Considering the message from the lady, she said she's not a musician or vocalist and she got divorced with her ex-husband in 2020. Also she mentioned that can't reveal her name for her past employment. It indicates she is "Mia Khalifa"
Now if we look for her ex-husband, we found the name "Robert Sandberg"
Putting this name in the flag format, we get out flag to be: apoorvctf{Robert_Sandberg}