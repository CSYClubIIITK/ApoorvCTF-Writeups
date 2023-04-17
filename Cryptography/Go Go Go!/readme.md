Extract the image file using binwalk. In the extracted folder, the file 'source.txt' contains a base64 encrypted string. Decrypt it using any online base64 decoder and you will get a drive link. The drive link will open a .txt file in the browser containing the flag encrypted with Caesar Cipher for which the key is provided. Decrypt it using dcode.fr's online caesar cipher decoder giving it the key value of 4 which we got from the drive file and copy the resulting string. After analyzing the encryption.txt files we know that the algorithm used is railfence cipher with key length 16. Again, using dcode.fr's rail fence cipher decoder, we can get the flag by pasting the obtained string in the ciphertext input, keeping the punctuation and spaces on, the character for spaces being underscores and setting key value to 16, we can get the resulting flag.

Flag: ApoorvCTF{4ven9e75_455emb1e_u1tr0n_ri5e5}

Author: Kunal Rajour
