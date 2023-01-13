

def shift_encode(message, position):
    encoded_message = ''
    for letter in message:
        encoded_message += chr(ord(letter)+position)
    return encoded_message

def shift_decode(message, position):
    decoded_message = ''
    for letter in message:
        decoded_message += chr(ord(letter)-position)
    return decoded_message

def main():
    user_message = input()
    print(shift_encode(user_message, 10))
    print(shift_decode(shift_encode(user_message, 10), 10))


if __name__ == '__main__':
    main()
