#Andrew Griner Lab06
def encode_password(password):
# Convert the password to a string
    password_str = str(password)

# Initialize an empty string to store the encoded password
    encoded_password_str = ''

# Loop through each character in the password string
    for char in password_str:
# Convert the character to an integer, shift it by 3, and take the remainder when divided by 10
        encoded_char = str((int(char) + 3) % 10)

# Add the encoded character to the encoded password string
        encoded_password_str += encoded_char

# Convert the encoded password string back to an integer and return it
        encoded_password = int(encoded_password_str)
    return encoded_password

def main():
    while True:
        print("Menu \n-------------\n1. Encode\n2. Decode \n3. Quit\n")
        userinput = int(input("Please enter an option:"))
        if userinput ==1:
            password = int(input("Please enter your password to encode:"))
            encode_password(password)
            print("Your password has been encoded and stored!")
        #if userinput ==2

        if userinput ==3:

            break



if __name__=='__main__': #main function as needed
    main()