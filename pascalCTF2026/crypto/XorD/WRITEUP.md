**OVERVIEW**

The challenge starts off by giving us the description "I just discovered bitwise operators, so I guess 1 XOR 1 = 1?" 

We also get access to two files: xord.py and output.txt

Here are the contents of xord.py: 

`import os`
`import random`

`def xor(a, b):`
    `return bytes([a ^ b])`

`flag = os.getenv('FLAG', 'pascalCTF{REDACTED}')`
`encripted_flag = b''`
`random.seed(1337)`

`for i in range(len(flag)):`
    `random_key = random.randint(0, 255)`
    `encripted_flag += xor(ord(flag[i]), random_key)`

`with open('output.txt', 'w') as f:`
    `f.write(encripted_flag.hex())`

The script's functionality works like this: 

First, the python modules os and random are defined and imported. After they're imported, the function xor is defined and it returns the parameters as bytes between the values of 0 and 255. Then, we define the 'flag' variable. Inside 'flag' we are trying to retrieve an environment variable with the 2 parameters 'FLAG' and 'pascalCTF{REDACTED}'. 

After this, it constructs a for loop where it iterates over each character in the flag string by index. 'random_key' is generating a pseudo-random 8 bit integer. 

The vulnerability we run into with this script is that 'random.seed(1337)' is defined. This causes the Python `random` module to be deterministic when seeded.  

Due to this, instead of the script generating a true random value each time, it generates values using the same value '1337', making it extremely easy to reverse and decrypt the XOR output. 

We then can use a solve script that XORs again to decrypt the "flag" and get the correct output for our challenge. 

flag : `pascalCTF{1ts_4lw4ys_4b0ut_x0r1ng_4nd_s33d1ng}`

solved by godlyavenger, writeup by clouddddddd