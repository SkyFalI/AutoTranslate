import keyboard
import pyautogui
import time
import pyperclip
from deep_translator import GoogleTranslator


def OnOffFunc():
    global enabled
    if enabled == "off":
        enabled = "on"
    else:
        enable = "off"

def foo():
    global text
    global lang
    global enable
    if enabled == "on":
        time.sleep(0.05)
        text = pyperclip.paste()
        try: 
        if text[0] in symbolsRU:
            lang = "en"
        if text[0] in symbolsENG:
            lang = "ru"        
        pyperclip.copy(GoogleTranslator(source='auto', target=lang).translate(text))
        print("Coped! foo")
        print(text)
        text = ""
        except:
            print('Eror find symbols')
    else:
        print("off Script")

text = ""
lang = ""
enabled = "off"

symbolsENG = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
              'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
symbolsRU = ['й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю',
             'Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Х','Ъ','Ф','Ы','В','А','П','Р','О','Л','Д','Ж','Э','Я','Ч','С','М','И','Т','Ь','Б','Ю',]

keyboard.add_hotkey('Ctrl + Alt', OnOffFunc)
keyboard.add_hotkey('Ctrl + C', foo)

print("Soft start!")

keyboard.wait('Ctrl + Q')
