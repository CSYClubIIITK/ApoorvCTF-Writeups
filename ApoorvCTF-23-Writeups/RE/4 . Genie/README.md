Name: Genie


The genie protects the flag here & only the worthy ones will be allowed to pass. Do you have what it takes? 
Or can you find a way to trick him ?


Medium category, 200 points

tags: Binary exploitation, Buffer 
hint: A mighty name might have an effect on genie

Writeup:
if the length of the name exceeds the maximum length 22, it calls the decrypt_file function to decrypt the contents of the flag.enc file and write the result to a new file called flag.txt.
any string greater than 22 will call that function

ApoorvCTF{b3at_th3_g3n13_5fz9}