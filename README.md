# CS485 Feistel cipher
This program is my implementation of a Feistel cipher using a 64 bit block size and a 64 bit key for the CS485 Cryptography elective, Winter 2020 term at Portland State University.

How to build and use the program:
The following project was implemented using Python 3.7.6

In order to run the program the user has to call the main function and provide command line arguments in this order:
    ```python3 main.py <key_file> <source_file> <destination_file> <option>```
* <key_file> - is a text file that contains a key. The key has to be represented in a hex format, without the leading "0x"
* <source_file> - is a text file, that either contains plain text (for encryption), or cipher text in a hex format (for decryption)
* <destination_file> - is a name of the text file where the program will save the result
* \<option> - specifies the behavior of the program. Use "-e" for encryption, and "-d" for decryption.

Examples of valid use would be the following: 
* For ecnryption:  ```python3 main.py key.txt plain.txt cipher.txt -e```
* For decryption:  ```python3 main.py key.txt cipher.txt plain.txt -d```

The following program contains 3 files:
* 1. main.py - contains the main() function. Parses command line arguments, reads from and saves to text files, creates objects of the KeyGenerator and PSUCrypt classes.
* 2. key_generator.py - contains the implementation of the KeyGenerator class. Generates 16 subkeys from a 64-bit key.
* 3. psu_crypt.py - contains the implementation of the PSUCrypt class. Performs encryption and decryption of a 64-bit block.
