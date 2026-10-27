def caesar(shift , text , encrypt = True):
    if not isinstance(shift, int) or isinstance(shift, bool):
        return "Shift must be an integer value."

    if shift < 1:
        return "Shift must be a positive integer."
        
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if not encrypt:
        shift = -shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    print(shifted_alphabet)
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, False)

encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)