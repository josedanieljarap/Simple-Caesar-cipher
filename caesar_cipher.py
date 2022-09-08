def main():
    message = input("What is your plain text: ")
    print("Caesar's cipher will be used...")
    while True:    
        try:
            key = int(input("What is the key:"))
            break
        except ValueError:
            print("key must be an integer, please try again")

    print(encrypt(message, key))


alphabet = 'abcdefghijklmnopqrstuvwxyz'

## string, int -> string
## return encrypted text using Caesar's cipher
## (shift each character k places backward)
def encrypt(plaintext, k):
    cipher_text = []
    ab_len = len(alphabet)

    for c in plaintext:
        index = alphabet.index(c)
        new_index = index - k
        if new_index < 0:
            new_index = ab_len + new_index
        cipher_text.append(alphabet[new_index])

    cipher_text = "".join(cipher_text)

    return cipher_text


if __name__ == "__main__":
    main()
