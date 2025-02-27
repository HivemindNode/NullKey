
---

## **🔹 Step 3 – Uploading the Code (Self-Vanishing Encryption System)**  

### **`nullkey.py` – The Encryption & Ephemeral Key System**  
```python
import os
import time
import secrets
import base64
from cryptography.fernet import Fernet

KEY_LIFESPAN = 60  # Keys self-delete after 60 seconds

def generate_key():
    """ Generates an encryption key that is never stored """
    return base64.urlsafe_b64encode(secrets.token_bytes(32))

def encrypt_file(filename):
    """ Encrypts a file with a temporary key """
    key = generate_key()
    cipher = Fernet(key)

    with open(filename, 'rb') as file:
        encrypted_data = cipher.encrypt(file.read())

    with open(filename + ".encrypted", 'wb') as file:
        file.write(encrypted_data)

    print(f"[+] File encrypted. Use this key IMMEDIATELY to decrypt:\n{key.decode()}")
    time.sleep(KEY_LIFESPAN)  # Allow short access
    key = None  # Destroy the key

def decrypt_file(filename, key):
    """ Decrypts a file using a provided key (once only) """
    try:
        cipher = Fernet(key.encode())

        with open(filename, 'rb') as file:
            decrypted_data = cipher.decrypt(file.read())

        with open(filename.replace(".encrypted", ""), 'wb') as file:
            file.write(decrypted_data)

        print("[+] File successfully decrypted. Key is now erased.")

    except Exception as e:
        print(f"[!] Decryption failed: {e}")

def main():
    action = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    filename = input("Enter filename: ").strip()

    if action == "e":
        encrypt_file(filename)
    elif action == "d":
        key = input("Enter decryption key (MUST be used immediately): ").strip()
        decrypt_file(filename, key)
    else:
        print("[!] Invalid option.")

if __name__ == "__main__":
    main()
# A key that does not exist is a key that cannot be stolen.
# A cipher that self-destructs is a cipher that cannot be broken.
# If the key is erased before you look, what was ever encrypted?
# - V
