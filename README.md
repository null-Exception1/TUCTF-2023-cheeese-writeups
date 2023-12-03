# TUCTF-2023-cheeese-writeups

# Bludgeon the Booty
don't think you'll be needing this one
just a basic brute force of rotations, they changed the challenge halfway by making it a 3 spin instead of a 4 spin lock

# Cube 2023

this one was pretty good. 

so the basic idea is that we go through every single cell in the cube grid (which was 10x10x10 but it got changed to 6x6x6) and store the faces (labels) from inside every cell. you also need to get the back faces of every cell by doing a R and an L for every new cell you visit. it doesn't matter if you know where you start from because the entire grid is just an infinite treadmill, you can keep going 

then we find all the coprimes and loop through all the cells (you can pathfind to the coprime cells if you want to) and insert 'C' to check them all

on how to find the coprimes - 
we basically go to every cell, find the cells next to it (or if they're over the boundary on the opposite side). then we find the faces facing the original cell from the cells next to the cell, check if all of the faces are coprime with each other, and if yes then put the position in memory.

i tried to half-ass it and didn't get the flag for a solid hour because i kept forgetting to recognize the flag with all my `recvuntil`'s and whatnot

don't be me. become better.

# Hacker Typer

if you go to dev console you can see there's requests being sent to the server and back. just post request of the word directly instead of even typing it. no need for simulating keypresses here. if you get a large enough streak you'll be given the flag (which is present in of the response only)

# Hidden Value

this was not interesting, just a simple BOF challenge

i recommend [this](https://ir0nstone.gitbook.io/notes/types/stack/shellcode) to learn how to do BOF

# Custom ECB

this is an interesting one. 

so what the encryption function `transform` is essentially did, is that it separated 4 byte blocks of the original flag, converted them to integers, did convert() on them, and added the block to the ciphertext.

so nothing goes wrong with the blocks here. you'll be able to separate 4 byte blocks from the cipher text aswell, it'll be done.

the convert function looks like this
```
def convert(msg):
    msg = msg ^ msg >> x
    msg = msg ^ msg << 13 & 275128763
    msg = msg ^ msg << 20 & 2186268085
    msg = msg ^ msg >> 14
    return msg
```

now the XOR (^) operator is a non-destructive operator. meaning - 

if there are 2 numbers, a and b and XOR(a,b) = c then
XOR(a,c) = b
XOR(b,c) = a

it's easily reversible.

however i was unsure of what >> or << does to this reversibility, turns out if you just run this in a shell you'll figure out the answer easily

```
>>> msg = 2390409
>>> msg = msg ^ msg >> 14
>>> msg
2390296
>>> msg = msg ^ msg >> 14
>>> msg
2390409
>>> msg = msg ^ msg >> 14
>>> msg
2390296
>>> msg = msg ^ msg >> 14
>>> msg
2390409
```

i dont know the explanation behind this to be very honest, i was just testing things out till i was like "alright" and put this in.

the & (AND) operator also got me too, it's a destructive operator and the fact that it's acting on XOR made me think i'll have to brute force all the possible results just to somehow reverse the & operator.

but nope, just tested it out

```
>>> msg = 23904093924
>>> msg = msg ^ msg << 20 & 2186268085
>>> msg
23933454052
>>> msg = msg ^ msg << 20 & 2186268085
>>> msg
23904093924
```

admittedly i have no idea how this works, i'm sure it's because of the >> or << operator that this & operator somehow seems to comply with.

```
def reverse_convert(msg):
    global x

    # the order of the operations is reversed, the operations are the same
    for i in range(3):
        msg = msg ^ msg >> 14

    for i in range(1):
        msg = msg ^ msg << 20 & 2186268085
    
    for i in range(1):
        msg = msg ^ msg << 13 & 275128763
    
    for i in range(3):
        msg = msg ^ msg >> x


    return msg
```

hence this formed and i solved the chall. the flag was unrecognizable though, it was really hard to distinguish it till i just submitted to my instincts and entered it as the actual flag. the cipher text cropped the flag format, which made it harder to find it than it would've, but i guess that's because people could've just used shortcuts to find a decryption algorithm by comparing the flag format and the cipher text




praying i don't fail in my exam tommorow

peace.


