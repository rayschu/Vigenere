#!/usr/bin/env python
import sys
import string

def encrypt(plain, key):
    plain = plain.replace(" ", "").upper()
    key = key.upper()
    key_index = 0
    cipher = ''
    for i in plain:
        cipher += chr((ord(i)+ord(key[key_index])-2*65) %26 +65)
        if key_index < len(key) - 1:
            key_index += 1
        else:
            key_index = 0
    return cipher

def decrypt(cipher, key):
	cipher = cipher.replace(" ", "").upper()
    key = key.upper()
    key_index = 0
    plain = ''
    for i in cipher:
        plain += chr((ord(i)-ord(key[key_index])-2*65) %26 +65)
        if key_index < len(key) - 1:
            key_index += 1
        else:
            key_index = 0
    return plain


def main():
	decision = ""
	while decision is not "1" and decision is not "2":
		print "Would you like to encrypt or decrypt a message?"
		print "1 - Encrypt message"
		print "2 - Decrypt Message"
		print "\nDecision:"
		decision = raw_input()
	
	if decision == "1":
		print "\nEncrypt Message:"
		print "Enter the message you would like to encrypt:"
		plain = raw_input()
		print "Enter the key:"
		key = raw_input()
		ciphertext = encrypt(plain, key)
		print("The Ciphertext is: ")
		print(ciphertext)

	elif decision == "2":
		print "\nDecrypt Message:"
		print "Enter the message you would like to decrypt:"
		cipher = raw_input()
		print "Enter the key:"
		key = raw_input()
		plaintext = decrypt(cipher, key)
		print("The Plaintext is: ")
		print(plaintext)

	else:
		print "Invalid Entry"

if __name__ == "__main__":
	main()

