def menu ():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    password_encode = ""

    for digit in str(password):
        encoded = str((int(digit) + 3) % 10)
        password_encode += encoded

    return password_encode


if __name__ == '__main__':
    while True:
        menu ()
        option = input("Please enter an option: ")
        if option == "1":
            password = int(input("Please enter your password to encode: "))
            #encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            print(f'The encoded password is {}, and the original password is {}.')
        elif option == "3":
            break

