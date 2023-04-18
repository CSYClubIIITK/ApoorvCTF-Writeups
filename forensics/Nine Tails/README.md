Challenge Name: The nine tailed fox.

Description: We found a few suspicious individuals with this image. It looks like the image has been encoded using several different techniques. Find out what they are up to.

Points: 200

Hint: 1. A 'fox' might solve your problems (cost= 0)

Answer/Flag: ApoorvCTF{flag_hunter_41e2gf}

tags: Cryptography and Forensics

Write-up:
The image contains a text file hidden using image staganography. Use tools like Opensteg to get a file named 'dump.txt'. The text file contains a string starting with 'n0_f1ag_h3r3' hidden within the paragraphs as zero width unicode characters using text steganography. Within the string, a base64 string is enclosed by two closing brackets 'QXBvb3J2Q1RGe2ZsYWdfaHVudGVyXzQxZTJnZn0='. Decoding it will give you the flag.

Tools used: Opensteg, https://330k.github.io/misc_tools/unicode_steganography.html, https://www.base64decode.org/

Author : ForensicsAnsh