print ("Someone stoll your computer. You arrive to a house. You get in and see a door.")
print ("You entered the computers room.")
print ("Find your computer and write the password. GOOD LUCK!")
print ("---------WELLCOME TO YOUR COMPUTER----------")
password = "password"
while password != "I love cats":
    password = input("-----ENTER PASSWORD-----")
    if password == "I love cats":
        print ("Correct! You won! Run again to guess again")
    else:
        print ("You lose! I'm sorry!")