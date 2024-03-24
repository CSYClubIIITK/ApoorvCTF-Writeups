Challenge Name: Bits are Significant
Difficulty: easy: 100
Author: Abhinav Yadav
Category: Forensics

Description: Hidden inside the delicate variations of sound waves is confidential information that can only be accessed by those with the knowledge to decipher.

Solution:
### Step 1:
As the Name of question suggests, Challenge has to do something with Least Significant bits and Most Significant bits.
We can check Meta data as-well for any other hints, But we already have enough to work with.

### Step 2:
Trying to extract Least Significant Bits.

```python

import wave
import struct
def extract_message(input_wav):
    with wave.open(input_wav, 'rb') as wav_in:
        frames = wav_in.readframes(wav_in.getnframes())
        samples = struct.unpack('<' + 'h' * (len(frames)//2), frames)
        binary_message = ''.join(str(sample & 1) for sample in samples)
        message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
        return message

if __name__ == "__main__":
    input_wav_file = "beats.wav"
    extracted_message = extract_message(input_wav_file)

    print("Extracted message:", extracted_message)
```

### Step 3:
Taking the output of this Program into a file.
![[Pasted image 20240324082056.png]]
opening `output.txt` file
![[Pasted image 20240324082139.png]]

##### Final Flag: apoorvctf{H@rm0Ny_0f_LSB_N0te&}