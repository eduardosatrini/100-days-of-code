# caesar-cipher

In cryptography, a Caesar cipher, is one of the simplest and most widely known encryption techniques.  

#### Code

```python
from string import ascii_lowercase # ascii letters in lowercase

class CeasarCipher:
    def __init__(self, shift):
        self.shift = shift
        self.alphabeth = ascii_lowercase # normal alphabeth
        self.alphabeth_cipher = self.cipher() # alphabeth with shift
        
        
    def cipher(self):
        new_alphabeth = self.alphabeth[self.shift:]
        return new_alphabeth + self.alphabeth[0:self.shift]
        

    def encrypt(self, msg):
        msg_index = []
        msg_encrypt = ""
        
        for m in msg:
            if m == " ": # verify empty spaces
                msg_index.append(" ")
            else:
                msg_index.append(self.alphabeth.index(m))
                
        for m in msg_index:
            if m == " ":
                msg_encrypt += "#" # add # in emptyspaces
            else:
                msg_encrypt += self.alphabeth_cipher[m] # encrypt msg
            
        return msg_encrypt


    def decrypt(self, msg):
        msg_index = []
        msg_decrypt = ""
        
        for m in msg:
            if m == "#":
                msg_index.append(" ") # remove # in the msg
            else:
                msg_index.append(self.alphabeth_cipher.index(m)) 
            
        for m in msg_index:
            if m == " ":
                msg_decrypt += " " # add empty spaces in the msg
            else:
                msg_decrypt += self.alphabeth[m] # decrypt message
            
        return msg_decrypt

```

```python
cipher = CeasarCipher(shift=1)
print(cipher.encrypt("attack the enemy")) # result buubdl#uif#fofnz
print(cipher.decrypt("buubdl#uif#fofnz")) # result attack the enemy
```
