#!/usr/bin/env python3

#definiendo las librerias
import i3ipc
import time
import os
import sys
import pyfiglet

#haciendo la conexion con i3
i3 = i3ipc.Connection()

#definiendo escritorios
ws1 = "1: "
ws2 = "2: "
ws3 = "3:󰈹 "
ws4 = "4:󰓇 "
ws5 = "5: "
ws6 = "6: "
ws7 = "7: "
ws8 = "8: "
ws9 = "9: "
ws10 = "10: "

#titulos
Central = pyfiglet.figlet_format("Central", font="cosmic")
Term = pyfiglet.figlet_format("Term", font="cosmic")
Apps = pyfiglet.figlet_format("Apps", font="cosmic")

OpcionesCentral = ["""
1) Modo estandar
2) Solo terminales
3) Programacion
4) Notas
5) Apps individuales
6) comming son...
99) Exit
"""  
]

OpcionesTerm = ["""
1) Terminal ws1
2) Terminal ws2
3) Terminal ws1 y ws2
99) salir
"""
]

OpcionesApps = ["""
1) firefox
2) spotify
3) vscode
4) obsidian
99) Exit
"""
]

#Separador
separador = "_" * 64

#salidas para el titulo
TituloCentral = f"{Central}\n{separador}\nEscoga un modo\n{separador}\n" + "\n".join(OpcionesCentral) + f"\n{separador}"
TituloTerm = f"{Term}\n{separador}\nEscoga un modo\n{separador}\n" + "\n".join(OpcionesTerm) + f"\n{separador}"
TituloApps = f"{Apps}\n{separador}\nEscoga un modo\n{separador}\n" + "\n".join(OpcionesApps) + f"\n{separador}"

#definiendo funciones
def Termcava():
    i3.command(f'workspace {ws1}')
    i3.command('exec kitty')
    #Esperar a que la terminal se abra
    time.sleep(0.5)
    # Dividir la ventana horizontalmente
    i3.command('split v')
    #Abrir otra terminal con cava en la parte inferior
    i3.command('exec kitty -e cava')
    time.sleep(1) #Esperar a que se abra
    #fijar la terminal de arriba y cambiara el tamaño
    i3.command ('focus up')
    i3.command ('resize shrink height -420 px')
    i3.command('split h')

def Termcava2():
    i3.command(f'workspace {ws2}')
    i3.command('exec kitty')
    #Esperar a que la terminal se abra
    time.sleep(0.5)
    # Dividir la ventana horizontalmente
    i3.command('split v')
    #Abrir otra terminal con cava en la parte inferior
    i3.command('exec kitty -e cava')
    time.sleep(1) #Esperar a que se abra
    #fijar la terminal de arriba y cambiara el tamaño
    i3.command ('focus up')
    i3.command ('resize shrink height -420 px')
    i3.command('split h')
    
def firefox():
    # Abrir Firefox en la workspace 3
    i3.command(f'workspace {ws3}')
    i3.command('exec firefox')
    time.sleep(1)

def spotify():
    # Abrir Spotify en la workspace 4
    i3.command(f'workspace {ws4}')
    i3.command('exec spotify')

def vscode():
    #abrir vscode :)
    i3.command(f'workspace {ws9}')
    i3.command('exec code')
    time.sleep(1)
    
def obsidian():
    i3.command(f'workspace {ws5}')
    i3.command('exec obsidian')
    time.sleep(1)

#comienza el script
try:
    os.system("clear")
    print(TituloCentral)
    
    while True:  # Bucle para evitar que el programa termine con entradas inválidas
        try:
            Seleccion = int(input("[+] Escoge una opción: "))
            break  # Si la entrada es válida, salimos del bucle
        except ValueError:
            print("\n[!] Error: Ingresa un número válido.")

    if Seleccion == 1:
        Termcava()
        firefox()
        spotify()
        print("[+] Ejecutando...")
        
    elif Seleccion == 2:
        os.system("clear")
        print(TituloTerm)

        while True:
            try:
                Terminal = int(input("[+] Escoge un modo de terminal: "))
                break
            except ValueError:
                print("\n[!] Error: Ingresa un número válido.")

        if Terminal == 1:
            Termcava()
        elif Terminal == 2:
            Termcava2()
        elif Terminal == 3:
            Termcava()
            Termcava2()
        elif Terminal == 99:
            print("[+] Saliendo... ")

    elif Seleccion == 3:
        navegador = input("¿Necesitas Firefox? (s/n): ").strip().lower()
        if navegador == "s":
            Termcava()
            firefox()
            spotify()
            vscode()
        elif navegador == "n":
            Termcava()
            spotify()
            vscode()
        print("[+] Ejecutando... ")

    elif Seleccion == 4:
        Termcava()
        firefox()
        obsidian()
        print("[+] Ejecutando...")

    elif Seleccion == 5:
        os.system("clear")
        print(TituloApps)

        while True:
            try:
                App = int(input("[+] Escoge una opción: "))
                break
            except ValueError:
                print("\n[!] Error: Ingresa un número válido.")

        if App == 1:
            firefox()
        elif App == 2:
            spotify()
        elif App == 3:
            vscode()
        elif App == 4:
            obsidian()
        elif App == 99:
            print("[+] Saliendo... ")

    elif Seleccion == 6:
        print("Comming soon...")

    elif Seleccion == 99:
        print("[+] Saliendo... ")

except KeyboardInterrupt:
    print("\n[+] Saliendo... (Ctrl+C detectado)")
    sys.exit(0)
