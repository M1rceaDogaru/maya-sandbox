aliensDictionary = {"we": "vorag", "come": "thang", "in": "zon", "peace": "argh", "hello": "kodar", 
"can": "znak", "i": "az", "borrow": "liftit", "some": "zum", "rocket": "upgoman", "fuel": "kakboom", "please": 
"selpin", "don't": "baaaaaaaaaaaarn", "shoot": "flabil", "welcome": "unkip", "our": "mandig", 
"new": "brang", "alien": "marangin", "overlords": "bap"}
englishPhrase = input("Please enter an English word or phrase to translate: ")
englishWords = englishPhrase.lower().split()
aliensWords = []
for word in englishWords:
    if word in aliensDictionary:
        aliensWords.append(aliensDictionary[word])
    else:
        aliensWords.append(word)
print ("In aliens, say: ", " ".join(aliensWords))