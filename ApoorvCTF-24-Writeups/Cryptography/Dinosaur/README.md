Challenge Name: Dinosaur
Difficulty: Medium - 200
Author: Cybertooths
Category: Cryptography


Description:
Someone was trying to mess with the organizers in the carnival by deploying fake dinosaurs. Somehow we managed to get a file from those fake dinosaurs but we are unable to get any further hints who was the culprit. Can you help us finding where did the dinosaurs came from?
Note: Put the exact location separated by underscores in the standard format. apoorvctf{exact_location_with_city}


Tags: 
1. Classical Cryptography
2. RSA


Solution:
In this challenge, we are provided with 2 files, named as "location.txt" and "encryption.py"

encryption.py
'''def encrypt1(message, e, n, keyword):
    message_bytes = message.encode()
    plaintext_int = int.from_bytes(message_bytes, "big")
    ciphertext_int = pow(plaintext_int, e, n)
    cipher = encrypt2(ciphertext_int, keyword)
    return cipher


def encrypt2(cipher, keyword):
    cipher_text = ""
    cipher = str(cipher)
    keyword_repeated = (keyword * (len(cipher) // len(keyword))) + keyword[
        : len(cipher) % len(keyword)
    ]

    for i in range(len(cipher)):
        encrypted_digit = (int(cipher[i]) + (ord(keyword_repeated[i]) - ord("a"))) % 10
        cipher_text += str(encrypted_digit)

    return cipher_text


keyword = "key"


e = 3
n = 23571113171923293137414347535961677173798389971011031071091131271311371391491511571631671731791811911931971992112232272292332392412512572632692712772812832933073113133173313373473493533593673733793833893974014094194214314334394434494574614634674794874914995035095215235415475575635695715775875935996016076136176196316416436476536596616736776836917017097197277337397437517577617697737877978098118218238278298398538578598638778818838879079119199299379419479539679719779839919971009101310191431936117404941729571877755575331917062752829306305198341421305376800954281557410379953262534149212590443063350628712530148541217933209759909975139820841212346188350112608680453894647472456216566674289561525527394398888860917887112180144144965154878409149321280697460295807024856510864232914981820173542223592901476958693572703687098161888680486757805443187028074386001621827485207065876653623459779938558845775617779542038109532989486603799040658192890612331485359615639748042902366550066934348195272617921683
location = "location"

print(encrypt1(location, e, n, keyword))'''


location.txt
"678759254497815324575921978329118622203404079119748120469586303593053802770346688613496176730389025256858803396119446910730500119533982559544519723255"

The file "encryption.py" was used to encrypt a message which was then stored in the file "location.txt"
Now we need to reverse the "encryption.py" script in order to reach the flag. 
This file contains two functions which found to be "Vigenere Cipher" and "RSA." First the message was encoded using RSA for which the product of the primes "n" and the exponent "e" is hardcoded, then the it was encoded using Vigenere Cipher for which we don't have the key.
Looking around we can guess the key to be "dinosaur" and run decryption by Vigenere on the string given in location.txt. We get the following string:
"395379281663015696237924695949145898403776731112465740496752503865715805497966615889696448492382742876885079596481108913457120146709182821206512440875"

Now we're left with RSA to be solved. For that I'm using the following script:
from Crypto.Util.number import long_to_bytes
from sympy import cbrt

encrypted_integer = "395379281663015696237924695949145898403776731112465740496752503865715805497966615889696448492382742876885079596481108913457120146709182821206512440875"

m = cbrt(int(encrypted_integer))
print(long_to_bytes(m))

Running this script will give an output "b'28.6132428 77.2453003'"

Also, running a combined script can help more of finding the correct result quickly, which is:

from Crypto.Util.number import long_to_bytes
from sympy import cbrt


def vigenere_decrypt(cipher_text, keyword):
    plain_text = ""
    keyword_repeated = (keyword * (len(cipher_text) // len(keyword))) + keyword[
        : len(cipher_text) % len(keyword)
    ]

    for i in range(len(cipher_text)):

        decrypted_digit = (
            int(cipher_text[i]) - (ord(keyword_repeated[i]) - ord("a"))
        ) % 10
        plain_text += str(decrypted_digit)

    return plain_text


encrypted_integer = "678759254497815324575921978329118622203404079119748120469586303593053802770346688613496176730389025256858803396119446910730500119533982559544519723255"
keyword = "dinosaur"
decrypted_integer = vigenere_decrypt(encrypted_integer, keyword)
print("Decrypted long integer:", decrypted_integer)


m = cbrt(int(decrypted_integer))
print(long_to_bytes(m))


Here on running this script you'll get the decoded Vigenere cipher and the coordinates extracted from the RSA encoded string.

Decrypted long integer: 395379281663015696237924695949145898403776731112465740496752503865715805497966615889696448492382742876885079596481108913457120146709182821206512440875
b'28.6132428 77.2453003'

These are the coordinates to the place from where the dinosaurs belong. On searching the coordinates, we find the location to be "National Science Centre Delhi."
According to the format given in the description, the flag would be: "apoorvctf{National_Science_Centre_Delhi}"