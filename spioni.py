alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("Please enter a message to encrypt: ")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("Please enter a whole number from 1-25 to be your key."))
encryptedString = " "
for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    encryptedString = encryptedString + alphabet[newPosition]
print ("Your encrypted message is", encryptedString) 