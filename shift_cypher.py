#!/usr/bin/python
import argparse
from array import *

"""
This program is being designed to decrypt a cyphertext created by using the English alphabet and a shift cypher. Using a brute force approach, all possible output strings will be outputted to a file.

--encrypt will take an input string and encrypt it with a random shift key. It will return the cyphertext and the key.

--decrypt will take an input cyphertext and key decrypt it.

--brute-force will take an input cyphertext and return all possible returns
"""

#This is the english alphabet that the shift cypher will use
english_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Pseudocode
'''
def brute_force():
	read input string and convert to lowercase
	translate each char to its english_alphabet index (ie: a=0,b=1,...,z=25)
	for int i=0 to 25:
		shift input string +i and store in new array
		translate new array from english_alphabet index to english_alphabet
		output potential string to output file
'''

def encrypt(message, key):	
	#print ("Encrypt function")
	message = message.replace(" ", "")
	message = message.lower()

	message_length = len(message)
	int_array = [None] * message_length
	cyphertext = ""
	
	i = 0
	while i < message_length:
		int_array[i] = (english_alphabet.index(message[i]) + key) % 26 
		cyphertext = cyphertext + english_alphabet[int_array[i]]		
		i = i + 1

	print (cyphertext)

def decrypt(cyphertext, key):
	#print ("Decript function")
	cyphertext = cyphertext.replace(" ", "")
	cyphertext = cyphertext.lower()
	
	cyphertext_length = len(cyphertext)
	int_array = [None] * cyphertext_length
	message = ""
	
	i = 0
	while i < cyphertext_length:
		int_array[i] = (english_alphabet.index(cyphertext[i]) - key) % 26 
		message = message + english_alphabet[int_array[i]]		
		i = i + 1

	print (message)

def brute_force(cyphertext):
	key = 0
	while key < 25:
		print ("With key: " + str(key))
		decrypt(cyphertext, key)
		key = key + 1
		print ("")

def main():

	#Create argparse object and arguments
	parser = argparse.ArgumentParser()
	#parser.add_argument('--input', help='Enter a message or cyphertext as input')
	parser.add_argument('--encrypt', help='Encrypts a given message with a random key. Requires --input. Outputs the cyphertext and the key.')
	parser.add_argument('--decrypt', help='Decrypts a given cyphertext using a given key. Requires --input and --key. Outputs the message.')
	parser.add_argument('--brute-force', help='Computes every possible message derivable from the cyphertext. Requires --input. Outputs every message and its associated key.')
	parser.add_argument('--key', help='Enter the key for the shift cypher. Either encrypts the message with the key or decrypts the cyphertext using the key. Outputs the decrypted/encrypted message.')
	args = parser.parse_args()

	#Determine functionality
	if args.encrypt or args.decrypt:
			if not args.key:
				print ("You must enter a key to encrypt or decrypt. --key <key>")
			else:
				try:			
					key = int(args.key)
					if key < 0:
						key = key * -1
					#print (isinstance(key, int))
					#print ("Key: " + str(key))
				except:
					print ("The key must be a positive integer.")
					quit()

	if args.brute_force and (args.encrypt or args.decrypt):
		print ("The brute-force algorithm cannot be run with any other flags.")
		quit()

	if args.encrypt:
		mode_encrypt = True
		#key = args.key
		message = args.encrypt
		encrypt(message, key)
		#print ("Message: " + message)

	if args.decrypt:
		mode_decrypt = True
		#key = args.key
		cyphertext = args.decrypt
		decrypt(cyphertext, key)
		#print ("Cyphertext: " + cyphertext)
	
	if args.brute_force:
		mode_brute_force = True
		cyphertext = args.brute_force
		brute_force(cyphertext)
		#print ("Cyphertext: " + cyphertext)

main()







