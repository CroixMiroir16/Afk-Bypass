import time
from pynput.keyboard import Controller

keyboard = Controller()

key_avant = 'z'
key_retour = 's'

interval = 2 # En secondes

time.sleep(3)
try:
    print("Boucle lancée avec succès.")
    while True:
        keyboard.press(key_avant)
        time.sleep(1)
        keyboard.release(key_avant)

        time.sleep(interval)
        keyboard.press(key_retour)
        time.sleep(1)
        keyboard.release(key_retour)

        time.sleep(interval)

except KeyboardInterrupt:
    print("\nBouclé mis a l'arrêt.")

# Pour arrêter le code, il suffit de faire : Ctrl + C ou simplement de cliquer sur Stop.
