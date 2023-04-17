# Write-up: 

Get the metadata of the png .jpeg file and get the key. As the description in the metadata says, 'Decode it and then use it to decrypt the flag' it means this is the key to decrypt the flag and not the passphrase for 'Steghide.' This is the most confusing part. Either use Steghide to get the flag without passphrase, or use any online tools. Decrypt the base64 encrypted key and use it to decrypt the flag which was encrypted as 'Variant Beaufort Cipher' which is a variant of Vigener CIpher.

Flag: ApoorvCTF{th!s_f14g_w45_enc0ded_by_Vict0ri0u5_Kn!9ht}

Author: Kunal Rajour
