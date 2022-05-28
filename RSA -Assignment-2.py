chiper = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?<>@#$%^&*()_-+=;:0123456789, "
public_key = 0

secret_key = 0
plain_text = ""
encrypted_text = ""
word = ""
key_word = ""
key_number = 1
run = True




while run:
    print("|------------------------------------------|")
    print("| Welcome to the RSA ENCRYPTION/DECRYPTION |")
    print("|------------------------------------------|\n\n")
    print("Please Enter the Odd Numbers if not then \n software update the number by it self\n\n >> Number Chose greater than 100 << \n gives more acurate result because bits are maximum \n --[Example is: 191 201]--")
    print("")
    p, q = input("Enter two key numbers seperated by space:\n#> ").split(" ")
    p = int(p)
    q = int(q)
    if(p%2 == 0):
       p=p+1
    if(q%2 == 0):
       q=q+1
    n = p * q
    z = (p-1) * (q-1)

    for i in range(1, 10000):
        if 0 != z % i:
            public_key = round(i)
            break

    for j in range(0, 10000):
        d = 1 + (j * z)
        d2 = d / public_key
        if 0 == d % public_key:
            secret_key = round(d2)
            break

    start = True
    while start:
        print("\n")
        print("|---------------|")
        print("|   p = ",p,"   |")
        print("|   q = ",q,"   |")
        print("|---------------|")
        print("  module=",n)
        print("|---------------|\n\n")
        print("public key=",public_key)
        print("secret key=",secret_key)
        print("COMMANDS")
        print("en   > Encrypt plain text")
        print("de   > Decrypt encrypted text")
        print("exit > Exit the program\n")
       
        word = input("#>")

        if "exit" in word:
            start = False

        if "en" in word:
            plain_text = input("Enter plain text: ")
            encrypted_text = ""
            for k in plain_text:
                m = 0
                for l in chiper:
                    if k == l:
                        if m < 10:
                            m = m + 00
                        encrypted_text = encrypted_text + (str((m ** public_key) % n)) + " "
                        break
                    m += 1
            print("encrypted text: ",encrypted_text)
            input("press enter")

        if "de" in word:
            encrypted_text = input("Enter encrypted text: ")
            plain_text = ""
            for s in encrypted_text.split(" "):
                for k in chiper:
                    m = 0
                    for l in chiper:
                        if k == l:
                            if s == (str((m ** public_key) % n)):
                                plain_text = plain_text + l
                            break
                        m += 1
            print("plain text: ",plain_text)
            input("press enter")

        if "exit" in word:
            run = False
