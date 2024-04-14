""" Hashlib module or secure hashes and messages digests. As the official documentation explains: This module implements a common interface to many different secure hash and message digest algorithms. https://docs.python.org/3/library/hashlib.html#module-hashlib"""

import hashlib


# If wanted to see the algorithms implemented by this modules, we just print'em. 
print(hashlib.algorithms_available)
""" Output: {'sha3_224', 'blake2s', 'sha512_256', 'sha3_512', 'blake2b', 'sha512_224', 'sha3_256', 'sha224', 'sha3_384', 'shake_128', 'sm3', 'md5-sha1', 'sha384', 'sha256', 'sha1', 'md5', 'sha512', 'shake_256'}
"""

#Creating a new hashlib object with any implementation (in this case, i used md5):
hslib = hashlib.new("md5")



# Using the update method with a byte (using b flag before) string inside as argument, i may use this object. Let me show you:
hslib.update(b"Cat's out of the bag. A penny for your thoughts")



""" The resulting digest is a hexadecimal string or a sequence of bytes. It uniquely represents the input data in a compact form. In Python, the digest is usually accessed as a hexadecimal string using the .hexdigest() method of the hash object.
"""

print(hslib.digest()) # It will print the hashed string.
#Output: b'\x16\xa8\xbe2\x7f\xc3\x07b\x9a>\xef\xfc\xd8\x10\xf5\xe1'




# if wanna print it in a hexadecimal way, we use this:
print(hslib.hexdigest())
#Output: 16a8be327fc307629a3eeffcd810f5e1
