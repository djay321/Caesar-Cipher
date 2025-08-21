# List of all lowercase alphabets used for shifting letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']

# A flag to control whether the program should keep running
should_run = True

# Loop until the user decides to exit
while should_run == True:

    # Ask the user if they want to encode, decode, or exit
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt and 'exit' to STOP:\n").lower().strip()
    
    # Create an empty list to store the final result (encoded/decoded characters)
    output_text = []

    # If the user wants to encode or decode
    if direction == "encode" or direction == "decode": 
        
        # Function to perform the Caesar Cipher operation
        def encrypt():
            # Ask the user for the text and shift value
            original_text = input("Type your message:\n").lower()
            shift_number = int(input("Type the shift number:\n"))
            
            # Loop through each character in the text
            for word in original_text:
                if word in alphabet:  # If it's an alphabet letter
                    if direction == "encode":
                        # Shift forward by shift_number and wrap around using modulus
                        output_text.append(alphabet[(alphabet.index(word) + shift_number) % len(alphabet)])
                    elif direction == "decode":
                        # Shift backward by shift_number
                        output_text.append(alphabet[(alphabet.index(word) - shift_number) % len(alphabet)])
                else:
                    # Keep spaces and symbols unchanged
                    output_text.append(word)
            
            # Print the final result as a single string
            print(f'Here is your {direction}d result: {"".join(output_text)}')

        # Call the function
        encrypt()

    # If the user chooses to exit
    elif direction == "exit":
        break

    # If user enters something invalid
    else:
        print("Enter a valid input!")
