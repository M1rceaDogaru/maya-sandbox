import tkinter
import time
import random

# Aceasta este o clasa.
# O clasa reprezinta o colectie de proprietati (cum ar fi fun sau hunger) si metode (ca feed)
# care actioneaza asupra proprietatilor si le schimba valoarea.
# Clasa este doar o descriere. Pentru a o folosi ai nevoie de o instanta.
class Cat:
    # Aceasta metoda este apelata automat cand cream o instanta de Cat
    # dand valori initiale celor 3 proprietati
    def __init__(self):
        self.fun = 109
        self.hunger = 100
        self.thirst = 109

    # Folosim metoda asta pentru a scadea valorile proprietatilor pisicii
    # aratand astfel ca i se face foame/sete/chef de distractie.
    # O valoare random previne scaderea lor la fel si o face mai interesanta.
    def update(self):
        self.fun -= random.choice([1, 2, 3])
        self.hunger -= random.choice([1, 2, 3])
        self.thirst -= random.choice([1, 2, 3])

    # Cu aceasta metoda hranim pisica
    def feed(self):
        self.hunger += 15

    def have_fun(self):
        self.fun += 15

# Aceasta este o instanta a unei clase.
# O instanta ii spune programului sa aloce memorie si executa metoda __init__ dand valori 
# celor 3 proprietatie pe care Cat le are.
# Poti crea mai multe instante de Cat si fiecare va avea proprietatile si metodele proprii.
my_cat = Cat()

# Acesta este un click handler cum ai mai folosit si in butonul.py
def on_feed_pressed(event):
    my_cat.feed()

def on_play_pressed(event):
    my_cat.have_fun()

# Acesta este cod de infrastructura, luat in mare parte din minge.py
canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()

# Acest text va contine o descriere a starii pisicii
cat_status_text = tkinter.StringVar()
# Acest text va afisa valorile proprietatilor pisicii
cat_properties_text = tkinter.StringVar()

# Cu aceasta metoda verificam proprietatile pisicii pentru a determina starea
def check_cat():
    if my_cat.hunger < 50:
        cat_status_text.set("I'm getting hungry. Feed me!")
    elif my_cat.fun < 50:
        cat_status_text.set("Play with me, I'm sad!")
    else:
        cat_status_text.set("I'm perfect. MIAU!")

# Cu aceasta metoda verificam daca am pierdut jocul si afisam un mesaj relevant.
# Metoda trebuie sa returneze True pentru a incheia jocul.
def is_fail_condition():
    if (my_cat.hunger <= 0):
        cat_status_text.set("Oh no, your cat died of hunger!")
        return True

    if my_cat.fun <= 0:
        cat_status_text.set("Oh no, your cat died of sadness!")
        return True

    return False

# Cu aceasta metoda actualizam textul care afiseaza proprietatile
def update_cat_properties_text():
    cat_properties_text.set("Hunger: " + str(my_cat.hunger) + " --- Thirst: " + str(my_cat.thirst) + " --- Fun: " + str(my_cat.fun))

# Cu aceasta metoda initializam interfata
def initialize():
    canvas = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
    canvas.pack()

    # Asa incarcam poza cu pisica. Poza trebuie sa se afle in acelasi folder cu fisierul .py
    cat_image = tkinter.PhotoImage(file="cute.cat.png")
    # Folosim o clasa Label din tkinter pentru a afisa poza
    cat_label = tkinter.Label(image=cat_image)
    cat_label.image = cat_image
    cat_label.pack()

    tkinter.Label(canvas, textvariable=cat_status_text, text="Rouge", fg="red").pack()
    tkinter.Label(canvas, textvariable=cat_properties_text, text="Rouge", fg="green").pack()

    # Configurarea butonului cu care hranim pisica
    feed_button = tkinter.Button(canvas, text="Feed me", width=40, background="pink")
    feed_button.bind("<ButtonRelease->", on_feed_pressed)
    feed_button.pack()

    play_button = tkinter.Button(canvas, text="Play with me", width=40, background="pink")
    play_button.bind("<ButtonRelease->", on_play_pressed)
    play_button.pack()
    
def main_loop():
    is_game_ended = False
    while is_game_ended == False:
        my_cat.update()
        check_cat()
        update_cat_properties_text()

        is_game_ended = is_fail_condition()
        window.update()
        time.sleep(0.2)

    time.sleep(3)

initialize()
main_loop()