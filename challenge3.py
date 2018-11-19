import binascii
import re

def score(string):
	freqs = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772,
				4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
	
	string = string.upper()
	sum = 0.0
	for i in range(len(string)):
		if string[i] == ' ':
			sum += 23.20
		elif string[i] >= 65 and string[i] <=90:
			sum += freqs[string[i] - 65]
		else:
			sum += 0
	return sum




x ='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
x_1 = binascii.unhexlify(x)

best_score = 0
ans = ''

for i in range(256):
	
	y = chr(i) * len(x_1)
	new_str = "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(x_1, y)])

	if score(new_str) > best_score:
		best_score = score(new_str)
		ans = new_str

print ans