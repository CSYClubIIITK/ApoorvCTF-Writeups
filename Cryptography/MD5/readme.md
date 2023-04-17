Write-up: 

Extract the md5.png file using 'binwalk -e md5.png' and then extract the zip file. In the zip file, there is a database file containing some MD5 hashes which corresponds to some commonly used passwords which can be searched online. Use MD5 databases online and decrypt the given hashes one by one (brute force). The password for the flag.zip file is 'jacksparrow' which you will get after decrypting the 9th MD5 hash.

Flag: ApoorvCTF{0h_n0_n0w_md5_i5_al50_n0t_secu7e}

Author: Kunal Rajour
