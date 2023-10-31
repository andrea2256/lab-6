# this function will print out the menu for the user when called
def menu ():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

# this function will encode the message by adding three numbers to the original value
def encode(password):
    # it is stored in a string
    password_encode = ""

    # the loop iterates through the password given by the user and turns the digits into integer values to be added by 3
    for digit in str(password):
        # this variable converts the digit into an integer; adds by three and uses modulo to check the range
        encoded = str((int(digit) + 3) % 10)
        # this stores the encoded value
        password_encode += encoded

    return password_encode


# Gabriel Schreiber
def decode(password):
    # the decoded password is stored here
    password_decoded = ''
    # this for loop changes the encoded password to the original password that was entered by the user
    for value in password:
        # this subtracts three from the value
        decoded = str(int(value) - 3)
        # 10 is added to the decoded values and turned into a string
        if int(decoded) < 0:
            decoded = str(int(decoded) + 10)
        # the decoded password is stored
        password_decoded += decoded

    return password_decoded


if __name__ == '__main__':
    # this loops asking the user for input until they exit out
    while True:
        menu ()
        option = input("Please enter an option: ")
        # encodes the password and stores it
        if option == "1":
            password = int(input("Please enter your password to encode: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        # decodes the password and prints out the encode and decode
        elif option == "2":
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
            print()
        # exits from the program
        elif option == "3":
            break

