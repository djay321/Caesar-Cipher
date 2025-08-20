# List of all lowercase alphabets (used for shifting letters)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
            'w', 'x', 'y', 'z']

# Asking the user what they want to do: encode (encrypt) or decode (decrypt)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()

# Asking the user for the message text
text = input("Type your message:\n").lower()

# Asking the user for the shift value (how many letters to move forward/backward)
shift = int(input("Type the shift number:\n"))

# A list to store the final result (encoded/decoded characters)
output_text = []

# Function to perform encoding or decoding
def encrypt(original_text, shift_number):
    # If user chose "encode"
    if direction == "encode":
        for word in original_text:
            # Check if character is an alphabet letter
            if word in alphabet:
                # Find its position, shift it forward, and add to output
                output_text.append(alphabet[(alphabet.index(word) + shift_number) % len(alphabet)])
            else:
                # If it's not a letter (like space or punctuation), keep it unchanged
                output_text.append(word)

    # If user chose "decode"
    elif direction == "decode":
        for word in original_text:
            if word in alphabet:
                # Find its position, shift it backward, and add to output
                output_text.append(alphabet[(alphabet.index(word) - shift_number) % len(alphabet)])
            else:
                output_text.append(word)

    # If user typed something invalid
    else: 
        print("Enter a valid input!")

    # Print the final joined string as the result
    print("".join(output_text))

# Call the function with user inputs
encrypt(text, shift)
