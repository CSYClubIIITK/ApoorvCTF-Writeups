Challenge Name: Forensic Jedi Quest
Difficulty: hard: 300
Author: Abhinav Yadav
Category: Forensic

Description: Jedi masters have transmitted a encoded message, decipher it with caution, young one, as the Force guides its concealed wisdom.

Solution:
The main idea to find the flag is Brute Force, Basic scripting and Base64.

### Step 1:

After downloading the `StarWars.jpg`, I try basic `strings`, `binwalk`, `exiftool` etc. to get as much info as possible.\

- running strings command presents us with 3 base 64 strings.
  ![](images/Pasted%20image%2020240324091618.png)
  which deciphering gives - Right Approach Try others. - May the Force Be With you - Steganography is such a beautiful and intriguing art
  This doesn't reveals much apart from giving we have to apply some Stegno tool.
- running `binwalk` doesn't give any info
- Now checking metadata using `exiftool` prints out
  ![](images/Pasted%20image%2020240324092030.png)

we could see a passwd field, with some base64 value translating to `Z7#B28@Uma7!EDdcQ4`

### Step 2:

Using steghide tool and the given password we can extract `MasterYoda.jgp`
![](images/Pasted%20image%2020240324092312.png)

### Step 3:

Again we are presented with another picture which we have to analyze with tools like `strings`,`binwalk`, `exiftool`
![](images/Pasted%20image%2020240324092502.png)

running `binwalk` give out that image contains a zipped folder containing `flag.txt`
Now using binwalk to extract the embedded zipped folder and the file.
![](images/Pasted%20image%2020240324092740.png)
but we get some errors, now we try opening that extracted zipped folder.
![](images/Pasted%20image%2020240324092838.png)
but the extracted zipped folder is password protected and trying the previously discovered password doesn't open it.

### Step 4:

we need to look for other details in the `MasterYoda.jpg` and best place is the meta data.
![](images/Pasted%20image%2020240324093510.png)
Here we find a hint telling that the password is `apoorvctf******` , where `*` is a number meaning our password lies between apoovctf000000-apoorvctf999999. Now only way to get the correct password is by brute forcing.

### Step 5:

python script for brute-forcing.

```python

#!usr/bin/python3
import pyzipper

def extract_zip(zip_file, wordlist):
    with open(wordlist, 'r') as wordlist_file:
        passwords = wordlist_file.readlines()
        for password in passwords:
            password = password.strip()
            try:
                with pyzipper.AESZipFile(zip_file) as zf:
                    zf.pwd = password.encode()
                    zf.extractall(pwd=password.encode())
                print(f"Success! Password found: {password}")
                return True
            except Exception as e:
                print(f"Failed with password: {password}. Error: {str(e)}")
                continue
        print("Failed to crack the password.")
        return False

if __name__ == "__main__":
    zip_file = "ZIP_FILE_NAMW.zip"
    wordlist = "wordlist.txt"
    extract_zip(zip_file, wordlist)
```

![](images/Pasted%20image%2020240324104506.png)
using this password we can decrypt the zipped file and extract flag.txt
![](images/Pasted%20image%2020240324104936.png)
Now deciphering this base64 string gives out the flag.

##### Final Flag: apoorvctf{m@Y_The_brute_f0rCe_be_wIth_Y0u}
