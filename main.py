import keyboard

def on_key_press(event):
    if event.name == 'l':
        
        keyboard.write('gg')

while True==True:
    keyboard.on_press(on_key_press)
    keyboard.wait('esc')