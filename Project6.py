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

def decoder(encoded_password): # decoder function by Fabian Estrada 
  encoded_password = list(str(encoded_password)) # turns string into list
  string = ''
  for i in encoded_password: # iterates through the list to subtract 3 from each num
    i = int(i)
    i -= 3
    string += str(i) # adds i to the string
  return string

def main():
    while True: # runs until user quits
        print("\nMenu \n-------------\n1. Encode\n2. Decode \n3. Quit\n")
        userinput = int(input("Please enter an option: "))
        if userinput == 1:
            password = int(input("Please enter your password to encode: ")) # asks user for password
            print("Your password has been encoded and stored!")
        elif userinput == 2: # returns encoded password and og password
          encoded_password2 = encode_password(password)
          original_password = decoder(encoded_password2)
          print(f'The encoded password is {encoded_password2} and the original password is {original_password}.')
        elif userinput ==3: # quits
            exit()

if __name__=='__main__': #main function as needed
    main()
