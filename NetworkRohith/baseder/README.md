Name: Baseder

Description: Find the flag in the pcap file.

Points: 200 (medium)

Hint: Encoding schemes similar to base64, but using different bases exist. (costs 50 points)

Flag: ApoorvCTF{=_=_b4s3_64?_n07_41way3}

Category: Network

Solution:
Find encrypted flag when you follow one of the TCP streams:
wzW97314gRUenZUJLwd2hN8yxK8Urc45x2MGksDShLXdjxjgpcyXnmVjUx18ssPKPXafGQXY8xYmbejWooy9662PqTMuBd2ZvnUYXCuS1RN84vkjkJHW91Ak5NpPYXodgXbCstWoEJnsnDiMn5fBn9

There are hints in the other TCP streams that suggest that this is base58 encoded.
Decode to get:
"base(5*17): 6#L3UASu$mDJ()9Bln#2FD,5.B5_^!+E)'D3Zq:%6?Zfo8hs6u;Fb;E0kO6_3GD5Z9mTof=YNZ,3H\%aA7eS)7Pe1LCO0Si4Zr"

Base85 decode to get:
"And ending with the good ol': QXBvb3J2Q1RGez1fPV9iNHMzXzY0P19uMDdfNDF3YXkzfQ=="

Base64 decode to get:
ApoorvCTF{=_=_b4s3_64?_n07_41way3}
