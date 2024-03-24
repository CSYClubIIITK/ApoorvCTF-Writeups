Challenge Name: "Photo Evidence"

Description: A suspect's phone was confiscated by law enforcement and a photo was found on the device that is believed to contain important metadata. Your task is to extract information from the photo and find the answer to the challenge.

Hint: Use a forensic tool to examine the photo and look for any information that might be useful.

Flag: ApoorvCTF{M3t4d4t4_3xtr4ct1on_1s_Fun}

Write Up: The hidden data can be extracted using the command "stegseek --seed Challenge_3.jpg" (link: https://github.com/RickdeJager/stegseek#detection-and-passwordless-extraction-cve-2021-27211") which would dump the hidden data.
Copy the series of hex data and google "hex to ascii converter" or make one yourself to get the flag.


Proposed score: 100
