constant_64bit = pow(2, 63)

def shiftBitLeft(block):
    if block >= constant_64bit:
        block -= constant_64bit
        block = block << 1
        block += 1
    else:
        block = block << 1
    return block

def createKeyArray(block):
    key_array = []
    for i in range(0, 64):
        block = shiftBitLeft(block)
        key_array.append(block)

    return key_array

def breakHexIntoChunks(block):
    block = hex(block)[2:]
    if(len(block) > 16):
        block = block[:16]
    else:
        while(len(block) < 16):
            block = "0" + block

    block_list = []
    i = len(block)
    while(i > 0):
        byte = block[i - 2: i]
        block_list.append(byte)
        i -= 2
    return block_list
         
def generateKeys(key):
    row_keys = createKeyArray(key)
    keys = []
    counter = -1
    x = 0
    while(x < 192 and counter < 16):
        i = x % 64
        byte_arr = breakHexIntoChunks(row_keys[i])
        if(x % 12 == 0):
            keys.append([])
            counter += 1

        b = x % 4
        if counter % 2 == 1:
            b += 4
        keys[counter].append(byte_arr[b])
        x += 1
    
    return keys
        
def printKeys(keys):
    # add asertions that keys have size of 16x12
    for key in keys:
        for b in key:
            print(b, end = ' ')
        print()







original_key = int(0xabcdef0123456789)
# new_key = shiftBitLeft(original_key)
key_array = createKeyArray(original_key)
# print(len(key_array))

print(hex(original_key))

keys = generateKeys(original_key)
printKeys(keys)
