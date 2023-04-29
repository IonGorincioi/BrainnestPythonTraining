'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It
encrypts letters by shifting them over by a
certain number of places in the alphabet. We
call the length of shift the key. For example, if the
key is 3, then A becomes D, B becomes E, C becomes
F, and so on. To decrypt the message, you must shift
the encrypted letters in the opposite direction. This
program lets the user encrypt and decrypt messages
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

from functions import caesar_cypher

should_continue = True
while should_continue:
    try:
        direction = input("Do you want to (e)ncrypt or (d)ecrypt\n")
        shift = int(input("Please enter the key (0 to 25): "))
        text = input("\nEnter your message:").lower()

        # when using a very large shift, it will be divided by 26
        # (the number of letters in alphabet), and the reminder
        # will be the actual shift
        shift = shift % 26
        caesar_cypher(initial_text=text, key=shift, cypher=direction)

        decision = input("Type 'y' if you want to go again. Otherwise type 'n'\n")

        if decision == 'y':
            continue
        elif decision == 'n':
            should_continue = False
            print("Goodbye!")
        else:
            print("Type 'y' if you want to go again. Otherwise, type 'n'\n")

    except ValueError:
        print("ERROR! Please use only numbers as a key.\n")
