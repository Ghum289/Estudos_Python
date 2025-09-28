import os
'''
import datetime
import pyautogui


print(os.listdir("arquivos"))

print(datetime.date.today())

pyautogui.press("win")
pyautogui.write("chrome")


pandas - trabalhar com arquivos em excel como uma base de dados

openpyxl - edita arquivos em excel

pyautogui - controla o mouse

# Não se preocupar com quais bibliotecas existem, já que
podemos aprender com o tempo
'''
lista_arquivos = os.listdir("arquivos")
#os.rename("arquivos/abr22.txt", "arquivos/22/abr22.txt")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")            
        elif "23" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")
