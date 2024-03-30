# xorcery

200 points

Author - helix

### Description 

Abracadabra won't work here. 
The true magic word lies within the class itself.


flag - apoorvctf{m4g1c_x0rd_f0und}

## Writeup

The program uses a XOR encryption scheme to hide the given magic word.
Upon decompiling with JADX, we can observe that the program is comparing 
each byte in magicbyte with corresponding byte in mybyte after doing a 
simple XOR operation with 0x77.It returns true if all bytes match indicating
that the magic word itself is a part of the flag

We can write a python script to reverse the operation:


```python
passBytes = [None] * 16

bytes = [
    0x1a, 0x43, 0x10, 0x46, 0x14, 0x28, 0x0f, 0x47, 0x05,
     0x13, 0x28, 0x11, 0x47, 0x02, 0x19, 0x13
]

for i in range(16):
	passBytes[i] =  chr(bytes[i] ^ 0x77)

print("apoorvctf{{{}}}".format(''.join(passBytes)))
```
