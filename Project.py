MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:

            cipher += ' '

    return cipher


def decrypt(message):


    message += ' '

    decipher = ''
    citext = ''
    for letter in message:


        if (letter != ' '):


            i = 0


            citext += letter


        else:

            i += 1


            if i == 2 :


                decipher += ' '
            else:


                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    return decipher


def main():
	print("1. Encrypt English to Morse Code")
	print("2. Decrypt Morse Code to English")
	check = int(input("Choose an option : "))
	if check == 1:
		message = input("Enter message to be encrypted in English : ")
		result = encrypt(message.upper())
		print(result)
	elif check == 2:
		message = input("Enter message to be decrypted in Morse Code : ")
		result = decrypt(message)
		print(result)
	else:
		print("Invalid Option !!!!!!!!!!")


if __name__ == '__main__':
    main()
