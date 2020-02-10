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
    key_array = [block]
    for i in range(0, 63):
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
    
    return [block[i:i+2] for i in range(0, len(block), 2)]
         


original_key = int(0xabcdef0123456789)
new_key = shiftBitLeft(original_key)
key_array = createKeyArray(original_key)
print(len(key_array))

print(hex(original_key))
print(hex(new_key))

test_key = key_array[63]
print(hex(test_key))

block = int(0xabcdef01234567890)
block = breakHexIntoChunks(block)
print(len(block))
# print("BreakHexIntoChunks:" + block)