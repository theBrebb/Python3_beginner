morse = ['.--.', '-.--', '-', '....', '---', '-.',
         '/', '..', '...', '/', '..-.', '..-', '-.', '-.-.--']


def decode_message(message):
    # Decode the message
    # message = str(message).lower
    morse_to_latin = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
                      ' -.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                      '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                      '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                      '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
                      '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
                      '---..': '8', '----.': '9', '-.-.--': '!', '/': ' '}
    decode = [""]
    for item in message:
        # print(item)
        # return decode
        # print(morse_to_latin[item[::1]])
        decode.append(morse_to_latin[item])

    return ''.join(decode).lower()
    # message = morse_to_latin[item]
    # return message
    # return morse_to_latin


# print(len(message))

print(decode_message(morse))
