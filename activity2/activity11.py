def decode_ascii_message(encoded_text):
    try:
        ascii_values = encoded_text.split()
        decoded_text = ''.join(chr(int(value)) for value in ascii_values)
        return decoded_text

    except:
        return "Invalid Decoding"
