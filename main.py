import psu_crypt
import key_generator as KG
import sys



original_key = int(0xabcdef0123456789)

def stringToHex(str):
    s_hex = []
    for c in str:
        s_hex.append(ord(c))

    h_str = ""
    for h in s_hex:
        h_str += format(h, "02x")
    return h_str


print()

plain_text = "security"
pt_hex = stringToHex(plain_text)

key_generator = KG.KeyGenerator(original_key)

psu_cr = psu_crypt.PSUCrypt(key_generator)
cipher_hex = psu_cr.encrypt(pt_hex)


print("DECRYPTION\n")
print(pt_hex)
print(cipher_hex)
plain_text = psu_cr.decrypt(cipher_hex)


def main():
    argv = sys.argv[1:]
    print(len(argv))

if __name__ == '__main__':
    main()