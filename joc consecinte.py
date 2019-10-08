woman = ["A scientst", "A qeen", "A pirate", "A giant rabbit"]
man = ["a police officer", "an artist", "your grandfather", "a killer robot"]
place = ["on Pluto.", "at the superarket.", "in a spooky, bat-filled cave."]
sheWore = ["scuba diving gear.", "fairy wings.", "a paper bag"]
heWore = ["a purple suit", "a shark costume.", "a beach towel."]
womanSays = ["Who are you?", "How many beans make five?", "Why?"]
manSays = ["Beep boop!", "Don't eat frogs!", "What time do you call this?"]
consequence = ["World peace.", "chaos", "a giant foot squashed them.", "rainbows."]
worldSaid = ["Errant nonsense!", "Cheese is trending now.", "I'm melting!"]
import random
while True:
    print(random.choice(woman), "met", random.choice(man), random.choice(place))
    print("She was wearing", random.choice(sheWore))
    print("He was wearing", random.choice(heWore))
    print("She said,", random.choice(womanSays))
    print("He said,", random.choice(manSays))
    print("The consequence was", random.choice(consequence))
    print("The world said,", random.choice(worldSaid))
    print()
    input("Press enter to play again.")
    print ()