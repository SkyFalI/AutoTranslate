# AutoTranslate
 Automatic text translation when copying ENG <-> RUS <br />
 exe file in dist\autoTranslate\autoTranslateWithOutConsole.exe <br />
 and with Console in dist\autoTranslate\autoTranslateWithConsole.exe
# Requirements
 - Python 3.10+
 - Pynput 1.7.6+
 - PyAutoGUI 0.9.53+
 - pyperclip 1.8.2+
 - deep-translator 1.9.1+
 ```python
from pynput import keyboard
import pyautogui
import time
import pyperclip
import sys
from deep_translator import GoogleTranslator
 ```
# How it work's
 When you press the "Ctrl + Alt" key combination, you enable the auto-translation script. <br />
 The script translates the copied text when pressing the key combination "Ctrl + C" and pastes it into the clipboard. <br />
 Google Translator is used for translation 
```python
 keyboard.GlobalHotKeys({
        '<ctrl>+c': on_copy,
        '<ctrl>+q': on_quit,
        '<ctrl>+<alt>': onoff_state})
```
 To determine the translated text, the script compares the first character of the copied string, so there will be an error when copying an incorrect   character.
 ```python
if text[0] in symbolsRU:
    lang = "en"
if text[0] in symbolsENG:
    lang = "ru"
```
# Peculiarities
- It takes time to translate. Be patient :) 
- Does not translate if the beginning of the copied string is from a character that is not included in the character array
```python
 symbolsENG = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
 symbolsRU = ['й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю',
'Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Х','Ъ','Ф','Ы','В','А','П','Р','О','Л','Д','Ж','Э','Я','Ч','С','М','И','Т','Ь','Б','Ю',]
```

# Future plans
- Develop script status display
- debug everything exception
____
All README was translated using a script :)
____
# Автоперевод
 Автоматический перевод текста при копировании ENG<->RUS
# Требования
 - Python 3.10+
 - keyboard 0.13.5+
 - PyAutoGUI 0.9.53+
 - pyperclip 1.8.2+
 - deep-translator 1.9.1
# Как это работает
 При нажатии комбинации клавиш «Ctrl+Alt» вы включаете скрипт автоперевода. <br />
 Скрипт переводит скопированный текст при нажатии комбинации клавиш "Ctrl+C" и вставляет его в буфер обмена. <br />
 Google Translator используется для перевода
```python
 keyboard.GlobalHotKeys({
        '<ctrl>+c': on_copy,
        '<ctrl>+q': on_quit,
        '<ctrl>+<alt>': onoff_state})
```
 Для определения переведенного текста скрипт сравнивает первый символ копируемой строки, поэтому при копировании неверного символа будет ошибка.
 ```python
if text[0] in symbolsRU:
    lang = "en"
if text[0] in symbolsENG:
    lang = "ru"
```
# Особенности
- Для перевода нужно время, Потерпи :) <br />
- Не переводится, если копируемая строка начинается с символа, не входящего в массив символов.
```python
 symbolsENG = ['q','w','e','r','t','y','u','i','o','p','a','s' ,'d','f','g','h','j','k','l','z','x','c','v','b',' n','m',
              'Q','W','E','R','T','Y','U','I','O','P','A','S','D ','F','G','H','J','K','L','Z','X','C','V','B','N', 'M']
 symbolsRU = ['й','ц','у','к','е','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю',
             'Й','Ц','У','К','Е','Н','Г','Ш','Щ','З','Х','Ъ','Ф','Ы','В','А','П','Р','О','Л','Д','Ж','Э','Я','Ч','С','М','И','Т','Ь','Б','Ю',]
```

# Планы на будущее
- Разработать отображение статуса скрипта
- отлаживать все исключения
____
Весь README был переведен с помощью скрипта :)
____
