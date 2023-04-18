Challenge Name: "Hidden Treasures"

Description: You've stumbled upon an image file that appears to be a normal JPEG, but upon closer inspection, it seems to be hiding something. Your task is to extract the hidden treasure from the image. 


Hint: You can get passphrase in file.

flag: ApoorvCTF{834ut1ful_7r345ur3}


file password: 0p3n_51m_51m_1234 (hidden in Owner Name)

Write Up: The hidden data can be extracted using the command "stegseek --seed Challenge_3.jpg" (link: https://github.com/RickdeJager/stegseek#detection-and-passwordless-extraction-cve-2021-27211") which would dump the hidden data.
Copy the series of hex data and google "hex to ascii converter" or make one yourself to get the flag.

Points:  200 (medium)

Author : ForensicsBlaize

