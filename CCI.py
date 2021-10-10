import os
import sys
import time
import webbrowser
def del_last_line():
      #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

print(" ____  ____  ______")
print("/ __/ / __/  \_  _/ Version:1.0")
print("||    ||       ||   Created By:Samuel Padilla")
print("||__  ||__    _||_  Made in: Visual Studio Code")
print("\___\ \___\  /____\ Github: @boogboog1")
print("Starting the System...")
time.sleep(2.5)
del_last_line()

while True:
    cmd = input("User:$")
    if cmd == ("debug"):
        print("Ver 1.0")
    
    elif cmd == ("web"):
        web = input("Type in the desired URL:")
        
        webbrowser.open_new_tab(web)

    elif cmd == ("search"):
        web = input("Google Search:")
        webbrowser.open_new_tab("https://www.google.com/search?q=" + web)

    elif cmd == ("echo"):
        echo = input("echo:")
        del_last_line()
        print(echo)

    elif cmd == (""):
        del_last_line()

    elif cmd == ("cls"):
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')
    
    elif cmd == ("help"):
        with open('help.txt') as f:
            contents = f.read()
            print(contents)

    elif cmd == ("memeofetch"):
        with open('Kneeofetch.txt') as f:
            contents = f.read()
            print(contents)

    elif cmd == ("exit"):
        break