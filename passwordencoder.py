# Daniel Moody Lab 6

def encode(password):
    encode_pass = ""

    for i in password:
        digit = int(i) + 3
        encode_pass += str(digit)[-1]

    return encode_pass


def main():

    while True:

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        user_option = int(input("Please enter an option: "))

        if user_option == 1:
            user_password = input("Please enter your password to encode: ")
            pass_encoded = encode(user_password)
            print("Your password has been encoded and stored!")
            print()
        elif user_option == 2:
            pass
        elif user_option == 3:
            break


if __name__ == '__main__':
    main()
