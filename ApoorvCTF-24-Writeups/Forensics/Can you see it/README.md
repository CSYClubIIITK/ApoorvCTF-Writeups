Challenge Name: Can you see it
Difficulty: medium: 200
Author: Abhinav Yadav
Category: Forensic

Description: I recently received my degree from the Secret Agent School. I was given my first assignment today that required me to read a file but I don't remember how to read it. HELP!

Note: Flag format apoorvctf{...}

Solution:
The main idea to find the flag is to open file using Python.

### Step 1:

We are given `README.txt`. When I tried a simple `cat README.txt`, it gave me a blank space.\
![](images/Pasted%20image%2020240324073848.png)\
but actually opening the file in Hex Editor gave me idea on how to approach.\
![](images/Pasted%20image%2020240324073919.png)

- here we saw blank space and dots could be morse or binary, we can try putting it in morse decoder but nothing useful comes out, now 2nd approach converting it into binary.

### Step 2:

Now, we saw all, `.` and spaces, so I replaced them with `1` and `0`. I wrote `exploit.py` to get the result:

```python

#! usr/bin/python3
file = open("README.txt", "r").read()
result = ""
for char in file:
	if ord(char) == 32:
		result += "0"
	else:
		result += "1"
print(result)
```

### Step 3:

After running `exploit.py` we get a binary output.
![](images/Pasted%20image%2020240324074525.png)
![](images/Pasted%20image%2020240324074617.png)

### Step 4:

We can take this binary and use any online convertor to convert binary to text.
![](images/Pasted%20image%2020240324075332.png)

##### Final Flag: apoorvctf{If_y0u_r3@d_thi5_you_pa553d}
