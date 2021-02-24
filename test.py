import module
import pyautogui

api = module.KBA()

query = pyautogui.prompt('Kelime:')

for kelime in api.KelimeBul(query):
    print(kelime)
