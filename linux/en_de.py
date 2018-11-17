from network_operations import encode as b64encode
from network_operations import decode as b64decode
from Crypto.Cipher import AES, Blowfish, CAST
from Crypto import Random
import pickle
import os

DEFAULT_SCHEME = "AES"
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "crypto.dat")

class encryption_data:
	def __init__(self,scheme,key):
		self.scheme = scheme
		self.key = key

def generate_schema(scheme="AES",key=""):
	# print("Generating scheme - AES")
	if(key == ""):
		key = Random.get_random_bytes(16)
		print("Your scheme is AES")
		print("Your key is",b64encode(key))
		print("As if you will remember your key... Just copy the file 'crypto.dat' in your installation folder for your next login, or change your key")
	else:
		if len(key) >= 16:
			'''
			Key is uniformly 16 bytes, TODO
			'''
			key = b64decode(key[0:16])
		else:
			print("Key too short, enter a 16 character key.")
	d = encryption_data("AES",key)
	f = open(PATH,"wb")
	pickle.dump(d,f)
	print("Generated a scheme")

def load_scheme(path):
	f = open(path,"rb")
	data = file.read()
	f.close()
	f = open(PATH,"wb")
	f.write(data)
	f.close()


def get_schema():
	choice = input("Do you have a config file for the key? (Enter y/n) : \n")
	if choice == "y" or choice == "Y":
		input_path = input("Enter the full path of the file : \n")
		load_scheme(path)
	else:
		schemes = ['AES','Blowfish','CAST']
		index = input("Enter the number corresponding to your encryption scheme :\n\t1. AES \n\t2. Blowfish \n\t3. CAST\n")
		scheme = schemes[int(index)]
		key = input("Enter the key as a string : ")
		generate_schema(scheme,key)


def encrypt(data):
	f = open(PATH,"rb")
	enc_data = pickle.load(f)
	scheme = enc_data.scheme
	key = enc_data.key
	if(scheme == "AES"):
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(key, AES.MODE_CFB, iv)
		return iv + cipher.encrypt(data)
	if scheme == "Blowfish":
		iv = Random.new().read(bs)
		cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
		bs = Blowfish.block_size
		plen = bs - divmod(len(data),bs)[1]
		padding = [plen]*plen
		padding = pack('b'*plen, *padding)
		return iv + cipher.encrypt(data + padding)
	if scheme == 
