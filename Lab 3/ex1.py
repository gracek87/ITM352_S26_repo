from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

encodedText = cipher_suite.encrypt(b"This is a really secret message.")
print(f"Encoded Text: {encodedText}")

# Use the cryptography library to code and decode a message 

decodedText = cipher_suite.decrypt(encodedText)
print(f"Decoded Text: {decodedText.decode('utf-8')}")

