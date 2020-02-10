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
        byte = "0x" + block[i - 2: i]
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
            keys.append("")
            counter += 1

        b = x % 8
        keys[counter] = keys[counter] + byte_arr[b] + " "
        x += 1
    
    return keys
        







original_key = int(0xabcdef0123456789)
# new_key = shiftBitLeft(original_key)
# key_array = createKeyArray(original_key)
# print(len(key_array))

print(hex(original_key))

keys = generateKeys(original_key)
for key in keys:
    str1 = key
    print(str1)
# print(hex(new_key))
# print(hex(key_array[2]))

# test_key = key_array[63]
# print(hex(test_key))

# block = int(0xabcdef01234567890)
# block = breakHexIntoChunks(block)
# print(len(block))
# str1 = ""
# for i in range(0, len(block)):
#     str1 += block[i] + " "
# print(str1)
# print("BreakHexIntoChunks:" + block)