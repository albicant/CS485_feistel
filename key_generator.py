class KeyGenerator:

    constant_64bit = pow(2, 63)

    def __init__(self, key):
        self.original_key = key
        self.keys = self.generateKeys(self.original_key)

    def getKeys(self):
        return self.keys
    
    def getOriginalKey(self):
        return self.original_key

    def shiftBitLeft(self, block):
        if block >= self.constant_64bit:
            block -= self.constant_64bit
            block = block << 1
            block += 1
        else:
            block = block << 1
        return block

    def createKeyArray(self, block):
        key_array = []
        for i in range(0, 64):
            block = self.shiftBitLeft(block)
            key_array.append(block)

        return key_array

    def breakHexIntoChunks(self, block):
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
            
    def generateKeys(self, key):
        row_keys = self.createKeyArray(key)
        keys = []
        counter = -1
        x = 0
        while(x < 192 and counter < 16):
            i = x % 64
            byte_arr = self.breakHexIntoChunks(row_keys[i])
            if(x % 12 == 0):
                keys.append([])
                counter += 1

            b = x % 4
            if counter % 2 == 1:
                b += 4
            keys[counter].append(int(byte_arr[b], 16))
            x += 1
        
        return keys
            
    def printKeys(self, keys):
        # add asertions that keys have size of 16x12
        for key in keys:
            for b in key:
                print(hex(b), end = ' ')
            print()

