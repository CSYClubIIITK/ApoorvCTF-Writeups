import hashlib


def custom_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode("utf-8"))
    return sha256.hexdigest()


def verify_key(key):
    if len(key) != 8:
        return False

    part1 = key[:4]
    part2 = key[4:]

    hash1 = custom_hash(part1)
    hash2 = custom_hash(part2)

    target_hash1 = ""  # lower case letters and special characters
    target_hash2 = ""  # numbers and lower case letters

    with open("hash.txt", "r") as file:
        for i, line in enumerate(file, 1):
            if i == 1:
                target_hash1 = line.strip()
            if i == 2:
                target_hash2 = line.strip()

    if hash1 == target_hash1 and hash2 == target_hash2:
        return True
    else:
        return False


def decrypt(input_file, output_file, key):
    with open(input_file, "rb") as f_input:
        with open(output_file, "wb") as f_output:
            ciphertext = f_input.read()

            repeated_key = key * ((len(ciphertext) // len(key)) + 1)

            plaintext = bytes(
                [ciphertext[i] ^ repeated_key[i] for i in range(len(ciphertext))]
            )

            f_output.write(plaintext)


if __name__ == "__main__":

    while True:
        your_input = input("Enter your password: ")

        if verify_key(your_input):
            print("Password Verified!!!\n")
            encrypted_file = "encrypted.txt"
            decrypted_file = "decrypted.txt"
            key = your_input.encode()
            decrypt(encrypted_file, decrypted_file, key)
            print("File Recovered Successfully!")
            break

        else:
            print("Incorrect Password!!!\n")
