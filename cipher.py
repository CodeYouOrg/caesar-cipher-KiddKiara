def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

if __name__ == "__main__":
    user_input = input("Please enter a sentence: ")
    encrypted_text = caesar_cipher(user_input, 5)
    print("The encrypted sentence is:", encrypted_text)

