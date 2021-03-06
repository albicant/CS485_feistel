# Gennadii Sytov - CS485 - Winter2020 - Project 1 "PSU_CRYPT"

import psu_crypt
import key_generator as KG
import sys


def stringToHex(str):
    s_hex = []
    for c in str:
        s_hex.append(ord(c))

    h_str = ""
    for h in s_hex:
        h_str += format(h, "02x")
    return h_str

def getKeyFromFile(key_file):
    try:
        file = open(key_file, 'r')
    except IOError:
        print("Error: Can't open the \"" + key_file + "\" file.")
    with file:
        key = file.readline()
        try:
            key = int(key, 16)
            key = format(key, "016x")
            if(len(key) > 16):
                key = key[:16]
        except ValueError:
            print("Error: Can't parse the key")
        
        return key

def getSrcFromFile(src_file, mode):
    try:
        file = open(src_file, 'r')
    except IOError:
        print("Error: Can't open the \"" + src_file + "\" file.")
    with file:
        hex_strings = []
        counter = 0
        i = -1
        while True:
            c = file.read(1)
            if not c:
                break
            if counter % 16 == 0:
                hex_strings.append("")
                i += 1
            if mode == "-e":
                c = format(ord(c), "02x")
                counter += 1
            counter += 1
            hex_strings[i] += c

        if i < 0:
            raise ValueError("Error: the source file is empty!")
        hex_strings[i] = format(int(hex_strings[i], 16), "016x")
        return hex_strings

def saveResultsToFile(dest_file, results, mode):
    try:
        file = open(dest_file, 'w')
    except IOError:
        print("Error: Can't create the \"" + dest_file + "\" file.")
    with file:
        counter = 0
        char_tup = ""
        for r in results:
            if mode == "-e":
                file.write(r)
            else:
                for c in r:
                    char_tup += c
                    counter += 1
                    if(counter == 2):
                        value = int(char_tup, 16)
                        if value != 0:
                            char_tup = chr(value) 
                            file.write(char_tup)
                        counter = 0
                        char_tup = ""


def main():
    argv = sys.argv[1:]
    if len(argv) < 4:
        print("Missing command line arguments!")
        return
    elif len(argv) > 4:
        print("Unknown command line arguments!")
        return

    key_file = argv[0]
    src_file = argv[1]
    dest_file = argv[2]
    mode = argv[3]
    if mode != "-e" and mode != "-d":
        print("Uknown encryption mode. Must be either \'-e\' or \'-d\'")
        return

    key = getKeyFromFile(key_file)
    src = getSrcFromFile(src_file, mode)

    key_gen = KG.KeyGenerator(key)
    cipher = psu_crypt.PSUCrypt(key_gen)
    results = []

    for s in src:
        if mode == "-e":
            results.append(cipher.encrypt(s))
        else:
            results.append(cipher.decrypt(s))

    # print(results)
    saveResultsToFile(dest_file, results, mode)

    process = ""
    if mode == "-e":
        process = "encryption"
    else:
        process = "decryption"
    print("The " + process + " has finished successfully. The result has been saved to the \"" + dest_file + "\" file.")


if __name__ == '__main__':
    main()