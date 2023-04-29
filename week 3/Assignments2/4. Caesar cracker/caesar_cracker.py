"""
This program can hack messages encrypted
with the Caesar cipher from the previous project, even
if you don‚Äôt know the key. There are only 26
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and dis play the results to the user. In cryptography, we call
this technique a brute-force attack.
"""
from functions import get_alphabet, decrypted_message

message = input("Enter message to crack: ")

alphabet = get_alphabet()
for key in range(0, 26):
    potential_messages = decrypted_message(message.lower(), alphabet, key)
    print(f'Key: {key}\t| Text: {potential_messages}')
