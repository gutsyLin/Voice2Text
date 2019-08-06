from pynput import keyboard

is_press = False
def on_press(d):
    if str(d) == 'Key.enter':
        global is_press
        is_press = True

keyboard_listener=keyboard.Listener(on_press=on_press)
keyboard_listener.start()

def is_enter_press():
    global is_press
    return is_press
