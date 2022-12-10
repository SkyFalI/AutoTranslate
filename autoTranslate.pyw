from pynput import keyboard
import pyautogui
import time
import pyperclip
import sys
from deep_translator import GoogleTranslator


symbolsENG = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
              'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
symbolsRU = ['й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю',
             'Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Х','Ъ','Ф','Ы','В','А','П','Р','О','Л','Д','Ж','Э','Я','Ч','С','М','И','Т','Ь','Б','Ю',]

text = ""
lang = ""
enabled = "off"

def onoff_state():
    print('Нажато сочетания клавиш: <ctrl>+<alt>')
    global enabled
    if enabled == "off":
        enabled = "on"
        print('Scirpt on')
    else:
        enabled = "off"
        print('Script off')

def on_quit():
    print('Нажато сочетание клавиш: <ctrl>+q')
    sys.exit()

def on_copy():
    print('Нажато сочетание клавиш: <ctrl>+c')
    global text
    global enabled
    global lang
    if enabled == "on":
        time.sleep(0.05)
        text = pyperclip.paste()
        try: 
            if text[0] in symbolsRU:
                lang = "en"
            if text[0] in symbolsENG:
                lang = "ru"        
            translatedtext = GoogleTranslator(source='auto', target=lang).translate(text)
            pyperclip.copy(translatedtext)
            print(f'Translated! \n{text} -> {translatedtext}')
            text = ""
        except:
            print('Eror find symbols')
    else:
        print("Script is off")

print('soft started!')
with keyboard.GlobalHotKeys({
        '<ctrl>+c': on_copy,
        '<ctrl>+q': on_quit,
        '<ctrl>+<alt>': onoff_state}) as listener:
    listener.join()
