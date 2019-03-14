# Simple python reverse cipher encrypt or decrypt
# kss : Tree

# variables
plainMsg = input('Enter message to encrypt/decrypt: \n')
cryptMsg = ''

# loop that will start at the end of the plainMsg and work its way until it is less than or = 0
l = len(plainMsg) - 1
while l >= 0:
    cryptMsg = cryptMsg + plainMsg[l]
    l = l - 1

print('Encrypted/Decrypted Message == : \n\n \t ' + cryptMsg + '\n\n /wave')
