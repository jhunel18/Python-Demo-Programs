while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        plainText = input("Enter a one-word, lowercase message: ")
        distance = int(input("Enter the distance value: "))
        code = ""

        for ch in plainText:
            ordValue = ord(ch)
            cipherValue = ordValue+distance

            if cipherValue > ord('z'):
                cipherValue = ord('a') + distance-(ord('z')-ordValue + 1)
            code += chr(cipherValue)
        print(code)

    elif choice == 2:

        code = input("Enter the code text")
        distance = int(input("Enter the distance: "))
        plainText = ""

        for ch in code:
            ordValue = ord(ch)
            cipherValue = ordValue - distance

            if(cipherValue < ord('a')):
                cipherValue = ord('z')-(distance-(ord('a')-ordValue + 1))
            plainText += chr(cipherValue)
        print(plainText)

    else:
        print("Invalid Input ")