# rot13.py
""" A cryptography program using the rot13 cipher. This program will accept text
input will either encrypt or decrypt depending on the user requirement.
Example ROT13
Plaintext	abcdefghijklmnopqrstuvwxyz
Ciphertext	nopqrstuvwxyzabcdefghijklm """

def rotate(text):
    """
    text is the string for encryption/decryption.
    """
    message = ''
    for i in range(len(text)):
        if text[i] in alpha0:
            index = alpha0.index(text[i])
            message += alpha13[index]
        else:
            message += text[i]
    return(message)
    
    
alpha0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alpha13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e',
           'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
