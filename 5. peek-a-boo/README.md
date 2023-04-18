Name: Peek-a-boo

Desc: I tried to organize a hide & seek tournament but it failed spectacularly. Good players are hard to find.
Anyway, can you find the flag hidden in here somewhere.

Hard level, 300 points

Tags: Binary , C , Reverse eng

hints: Try decompiling it

second hint : Look for the strings

Writeup:
Given a binary file, we need to decompile it. Many tools out there as Ghidra being one of the disassembler. Search defined strings , there we can find some strings related to flag. Jump to the fuction by the address referenced by those strings, decompile the following function. We will see 3 if statements. Each taking a hexadecimal value, each containing a hex encoded string. The 2nd if statement has the encoded string which will emit the flag 

ApoorvCTF{g0tch4_y0u_li77l3_sh117} from hex encoded 41 70 6f 6f 72 76 43 54 46 7b 67 30 74 63 68 34 5f 79 30 75 5f 6c 69 37 37 6c 33 5f 73 68 31 31 37 7d

Author : REAryan