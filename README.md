# NullKey  
_A self-vanishing encryption system for absolute security._  

### What It Does:  
- **Encrypts data using a key that is never stored**  
- **Keys exist only in volatile memory and disappear after decryption**  
- **Ensures files can only be decrypted once—then they are permanently locked**  
- **Prevents forensic recovery by eliminating key persistence**  

### Who Is It For?  
_"An encryption key that cannot be found  
Is an encryption key that cannot be stolen."_  

### How to Use:  
1. Encrypt a file with **NullKey**:  
   ```bash
   python3 nullkey.py --encrypt secret.txt
