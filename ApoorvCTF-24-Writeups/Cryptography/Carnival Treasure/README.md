Challenge Name: Carnival Treasure
Difficulty: Easy - 100
Author: Cybertooths
Category: Cryptography


Description:
Welcome to the Carnival Treasure Challenge!
Unravel the mysteries of the carnival and unlock hidden riches by solving the password mystery. Dive into a world of cryptic puzzles and enigmatic clues to claim the coveted treasure that lies within. Are you ready to embark on this thrilling adventure and become the ultimate treasure hunter?


Tags: 
1. SHA256
2. Vernam


Hints: 
1. Tried other tools than just wordlist?


Solution:
The challenge comes with 3 files with names "enc.py" which can be utilised to decipher the encrypted string in "encryption.txt"
The enc.py uses 2 hashes which can be found in hash.txt to confirm if the password for decryption is correct.
Now if we see the decryption script, we find that the password length is of 8 characters and it gets spit into 2 parts of size 4 characters each. 
Also, the comments in front of the hash variables tells the combination of characters used in the password.
To decode the hash, we can use the following tool: https://10015.io/tools/sha256-encrypt-decrypt
Here, we can specify the length of the password and combination to reverse the hash.
From the 1st part of the hash, we get "thr!"
And from the 2nd part of the hash, we get "133r"
Hence, we get our password to be "thr!113r"

Now we can run our original script "enc.py" and enter this password to get the flag decoded: "apoorvCTF{3ncrypt!n9_th3_P4r4d3_F35t!v!t!5}"