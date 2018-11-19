import binascii

def xor(x, y):
	return hex(int(x, 16) ^ int(y, 16))[2:-1]


x = '1c0111001f010100061a024b53535009181c'
y = '686974207468652062756c6c277320657965'

print xor(x, y)

