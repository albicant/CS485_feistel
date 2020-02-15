import key_generator as KG

def printHex(he):
    h_str = "0x"
    for h in he:
        h_str += hex(h)[2:]
    print(h_str)

def stringToHex(str):
    s_hex = []
    for c in str:
        s_hex.append(ord(c))
    return s_hex


original_key = int(0xabcdef0123456789)

keys = KG.generateKeys(original_key)
KG.printKeys(keys)

print()

plain_text = "security"
pt_hex = stringToHex(plain_text)
printHex(pt_hex)