# the ciphertext
ct = 'πππππππππππππΏπππππππΏπππΏπππππ'

# get the diff value
diff = ord(ct[0]) - ord('u')

# reconstruct the plaintext
pt = []

for c in ct:
    char_value = ord(c) - diff
    pt.append(chr(char_value))

print(''.join(pt))
