import os
import random
from pwn import *
print("test")

def xor(a, b):
    return bytes([a ^ b])

flag = os.getenv('FLAG', 'pascalCTF{REDACTED}')
flag = b'\xcb\x35\xd9\xa7\xd9\xf1\x8b\x3c\xfc\x4c\xe8\xb8\x52\xed\xfa\xa2\xe8\x3d\xcd\x4f\xb4\x4a\x35\x90\x9f\xf3\x39\x5a\x26\x56\xe1\x75\x6f\x3b\x50\x5b\xf5\x3b\x94\x93\x35\xce\xec\x1b\x70\xe0'
encripted_flag = b''
random.seed(1337)

for i in range(len(flag)):
    random_key = random.randint(0, 255)
    print(random_key)
    encripted_flag += xor((flag[i]), random_key)

print(encripted_flag)