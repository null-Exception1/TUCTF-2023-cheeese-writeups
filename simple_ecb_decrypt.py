from Crypto.Util import number

flag = b"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


c = "e34a707c5c1970cc6375181577612a4ed07a2c3e3f441d6af808a8acd4310b89bd7e2bb9"
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

def reverse_transform(new_message):

    # pretty much the same transform function, nothing much

    message = b''
    for i in range(int(len(new_message) / 4)):
        
        block = new_message[i * 4 : i * 4 +4]
        
        # only slicing cuz i dont know where extra bytes were coming from
        r = number.long_to_bytes(reverse_convert(number.bytes_to_long(block)))[-5:] 
        
        message+=r
    
    return message

for i in range(0,31): # 9th is the flag, put it in TUCTF{} format
    x = i
    print(x,reverse_transform(bytes.fromhex(c)))