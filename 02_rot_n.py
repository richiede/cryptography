# rot_n.py
""" A cryptography program using the rot ciphers. This program will accept
a rot number and text input. It will either encrypt or decrypt depending on
the user requirement.
Example ROT13
Plaintext	abcdefghijklmnopqrstuvwxyz
Ciphertext	nopqrstuvwxyzabcdefghijklm """

def create_alphab(n):
    """
    Creates the rot n alphabet
    """
    alpha_n = alpha0[n:] + alpha0[0:n]
    return alpha_n

def encrypt(n, text):
    """
    Encrypts data using the rot-n specified and text
    """
    alpha_n = create_alphab(n)
    message = ''
    for i in range(len(text)):
        if text[i] in alpha0:
            index = alpha0.index(text[i])
            message += alpha_n[index]
        else:
            message += text[i]
    return(message)

def decrypt(n, text):
    """
    Decrypts data using the rot-n specified and text
    """
    alpha_n = create_alphab(n)
    message = ''
    for i in range(len(text)):
        if text[i] in alpha_n:
            index = alpha_n.index(text[i])
            message += alpha0[index]
        else:
            message += text[i]
    return(message)
    
    
alpha0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
