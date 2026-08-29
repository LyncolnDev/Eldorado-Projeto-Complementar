import subprocess
import time
from turtledemo.round_dance import stop

import pyautogui
import pandas as pd
import os
import glob

# ==============================
# CONFIGURAÇÕES
# ==============================

caminho_exe = r"C:\Program Files (x86)\ATSLog Tecnologia em Logística\Launcher.exe"
argumentos = "-xClient -ATSJORNADA"
diretorio_trabalho = r"C:\Program Files (x86)\ATSLog Tecnologia em Logística"

#pasta_download = r"C:\Users\usuario\Downloads\PASTA DE USO DE TRABALHO"

# ==============================
# 1. ABRIR SISTEMA
# ==============================

print("Abrindo o ATS Jornada...")
subprocess.Popen(f'"{caminho_exe}" {argumentos}', cwd=diretorio_trabalho, shell=True)
time.sleep(5)

# ==============================
# 2. LOGIN
# ==============================

print("Fazendo login...")
pyautogui.write("@at0101", interval=0.1)
pyautogui.press("enter")
time.sleep(20)

# ==============================
# 3. EXPORTAÇÃO
# ==============================

print("Exportando os dados...")
pyautogui.press("alt")
time.sleep(1)


for i in range(0):  # tenta várias vezes
    pyautogui.press("tab")
    time.sleep(5)



# tenta interagir como se fosse tabela
pyautogui.hotkey("alt","down")
time.sleep(5)

for i in range(5):  # tenta várias vezes
    pyautogui.press("tab")
    time.sleep(5)

for i in range(1):  # tenta várias vezes
        pyautogui.press("down")
        time.sleep(2)

pyautogui.hotkey("shift", "f10")
time.sleep(2)

pyautogui.hotkey("shift", "f10")
time.sleep(2)

for i in range(7):  # tenta várias vezes
    pyautogui.press("down")
    time.sleep(5)

# tenta acessar exportar
pyautogui.write("exportar")
time.sleep(0.5)

pyautogui.write("asdados_exportados")
time.sleep(1)

pyautogui.press("enter")
time.sleep(2)
print("Vou parar aqui")
exit()  # ou quit()

