from pwn import *
import math

p = remote('chal.tuctf.com',30009)

def pairwise_coprimes(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if gcd(arr[i], arr[j]) != 1:
                return False
    return True

def gcd(a, b):
    return math.gcd(a,b)

def go(arg): # it does an extra R and L just to look back to add the label on it's back
    txt = p.recvuntil(b'Action: ').decode()
    numbers = []
    for i in txt.split(' '):
        try:
            numbers.append(int(i))
        except:
            pass

    
    p.send(b'R\n')
    txt = p.recvuntil(b'Action: ').decode()
    n = []
    for i in txt.split(' '):
        try:
            n.append(int(i))
        except:
            pass
    numbers.append(n[3])
    p.send(b'L\n')
    txt = p.recvuntil(b'Action: ').decode()
    
    p.send(arg.encode()+b'\n')
    return numbers # up, left, forward, right, down, behind

def check():
    txt = p.recvuntil(b'Action: ').decode()
    print(txt)
    p.send('C\n')
    return 0 # up, left, forward, right, down, behind


d = [] # cubes

for i in range(6):
    d.append([])
    
    # to clear one layer in F and U dimensions, we do 6 times U per 6 times F
    for j in range(6):
        d[-1].append([])
        for k in range(6):
            d[-1][-1].append([])
            up,left,forward,right,down,behind = go('F')
            d[-1][-1][-1].append([up,left,forward,right,down,behind])
            print(i,j,k)
        go('U')
    
    # turn right, move forward, turn left (amazing way to move right i know)
    go('R')
    go('F')
    go('L')

print(d) # got all the cubes

cubes = d

def find(a,b,c): # a,b,c are the coord of the box, finding all the faces of the boxes in this func
    global cubes

    # for the sake of boundary crossing
    # getting the cube next to this cube, to get the face of this cube from the perspective of that one

    if c+1 != 6:
        f = cubes[a][b][c+1][0][-1] 
    else:
        f = cubes[a][b][0][0][-1]
    if b+1 != 6:
        d = cubes[a][b+1][c][0][4]
    else:
        d = cubes[a][0][c][0][4]
    if a+1 != 6:
        l = cubes[a+1][b][c][0][1]
    else:
        l = cubes[0][b][c][0][1]
    

    m = []
    m.append(d)
    m.append(cubes[a-1][b][c][0][3])
    m.append(f)
    m.append(l)
    m.append(cubes[a][b-1][c][0][0])
    m.append(cubes[a][b][c-1][0][2])
    return pairwise_coprimes(m)


t = 0
coprimes = []
for i in range(len(cubes)):
    for j in range(len(cubes[i])):
        for k in range(len(cubes[i][j])):
            if find(i,j,k): # find whether coprime or not
                coprimes.append([i,j,k])
                t+=1

#print(t) 
print(coprimes) # position of all the coprime boxes


# iterated one by one, didn't try to pathfind to the coprimes
o = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            #print(i,j,k)
            #print(coprimes)
            print(" GOT ",o) # reassurance
            if [i,j,k] in coprimes: # if a coprime
                o += 1
                check()
                if o == 26:
                    p.interactive() # found the flag

                
            go('F')
        go('U')
    go('R')
    go('F')
    go('L')


    



