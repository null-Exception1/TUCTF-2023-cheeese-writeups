from pwn import *


p = remote('chal.tuctf.com',30002)
def rot_key(n):
    p.send(b'1\n')
    p.recvline()
    p.send(str(n).encode()+b'\n')
    p.recvline()
    p.send(b'+\n')
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
    print(p.recvline())
print(p.recvline())
txt = p.recvuntil(b'exit\n')

# me when brute force
for b in range(10):
    for c in range(10):
        for d in range(10):
            rot_key(3)
        rot_key(2)
    rot_key(1)
