def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift #reverses
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


option = input("Would you like to encrypt or decrypt? (Choose e or d): " )

if option == "e":
    
    text= input("Enter text you would like encrypted: ")
    encrypted_text = encrypt(text, 3)
    print("Encrypted: " + encrypted_text)
elif option == "d":
    text= input("Enter text you would like decrypted: ")
  
    decrypted_text = decrypt(text,3) #issue with decryption, shift functionality doesnt work..
    
    print("Decrypted: " + decrypted_text)

else:
    print("Not a valid option. Try again.")


