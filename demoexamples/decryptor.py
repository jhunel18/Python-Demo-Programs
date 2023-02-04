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