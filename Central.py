#!/usr/bin/env python3
import i3ipc
import time
import os
import sys
import pyfiglet
# Conexión con i3
i3 = i3ipc.Connection()
# Definiendo workspaces
workspaces = {
    "ws1": "1: ",
    "ws2": "2: ",
    "ws3": "3:󰈹 ",
    "ws4": "4:󰓇 ",
    "ws5": "5: ",
    "ws6": "6: ",
    "ws7": "7: ",
    "ws8": "8: ",
    "ws9": "9: ",
    "ws10": "10: ",
}
# Función genérica para abrir aplicaciones
def open_app(app, workspace_key):
    if workspace_key in workspaces:
        i3.command(f'workspace {workspaces[workspace_key]}')
        i3.command(f'exec {app}')
        time.sleep(1)
        print(f"[+] {app} abierto en {workspaces[workspace_key]}")
    else:
        print(f"[!] Workspace '{workspace_key}' no definido.")
        
# Función para abrir terminal con Cava
def Terminal(workspace_key):
    if workspace_key in workspaces:
        i3.command(f'workspace {workspaces[workspace_key]}')
        i3.command('exec kitty')
        time.sleep(0.5)
        i3.command('split v')
        i3.command('exec kitty -e cava')
        time.sleep(1)
        i3.command('focus up')
        i3.command('resize shrink height -420 px')
        i3.command('split h')
        print(f"[+] Terminal con Cava en {workspaces[workspace_key]}")
    else:
        print(f"[!] Workspace '{workspace_key}' no definido.")
        
# Opciones de menú
options = {
    1: ("Modo estándar", lambda: [Terminal("ws1"), open_app("firefox", "ws3"), open_app("spotify", "ws4")]),
    2: ("Solo terminales",None),
    3: ("Programación", lambda: [Terminal("ws1"), open_app("code", "ws9"), open_app("spotify", "ws4")]),
    4: ("Notas", lambda: [Terminal("ws1"), open_app("firefox", "ws3"), open_app("obsidian", "ws5")]),
    5: ("Apps individuales", None),  # Manejado aparte
    6: ("Juegos", None),
    7: ("Comming soon...", lambda: print("Comming soon...")),
    99: ("Salir", lambda: sys.exit(0))
}
# Menú dinámico con Figlet
def show_menu():
    os.system("clear")  # Limpia la terminal
    Central = pyfiglet.figlet_format("Central", font="cosmic")  # Crea un texto grande con Figlet
    separator = "_" * 64  # Un separador visual en la terminal
    print(f"{Central}\n{separator}\nEscoge un modo\n{separator}")
    
    # Muestra las opciones de modo
    for key, (name, _) in options.items():
        print(f"{key}) {name}")
    print(separator)
    
# Inicio del script
def main():
    try:
        while True:
            show_menu()  # Muestra el menú dinámico
            try:
                selection = int(input("[+] Escoge una opción: "))  # Solicita una opción al usuario
################ Modulo de terminales
                if selection == 2:
                    separator = "_" * 64
                    os.system("clear")
                    title = pyfiglet.figlet_format("Terminales", font="cosmic")  # Cambié el título para que tenga sentido
                    print(f"{title}\n{separator}\nEscoge una opción\n{separator}")  
                    terminales = {
                        1: ("Solo ws1", lambda: Terminal("ws1")),
                        2: ("Solo ws2", lambda: Terminal("ws2")),
                        3: ("ws1 y ws2", lambda: (Terminal("ws1"), Terminal("ws2")))  # Corregido el error
                    }                 
                    for key, (desc, _) in terminales.items():  # Cambio de variable terminales -> desc
                        print(f"{key}) {desc}")
                    print(separator)
                    terminal_selection = int(input("[+] Escoge una opción: "))
                    # Ejecuta la aplicación seleccionada
                    if terminal_selection in terminales and terminales[terminal_selection][1]:
                        terminales[terminal_selection][1]()  # Ejecutar la función lambda asociada
                    elif terminal_selection == 99:  # Corregido el error de variable incorrecta
                        continue  # Si selecciona 'Salir', regresa al menú principal
                    else:
                        print("[!] Opción no válida.")
                        
################# Modulo de apps individuales
                elif selection == 5:
                    separator = "_" * 64
                    os.system("clear")
                    title = pyfiglet.figlet_format("Apps", font="cosmic")
                    print(f"{title}\n{separator}\nEscoge una aplicación\n{separator}")
                    apps = {
                        1: ("firefox", lambda: open_app("firefox", "ws3")),
                        2: ("spotify", lambda: open_app("spotify", "ws4")),
                        3: ("vscode", lambda: open_app("code", "ws9")),
                        4: ("obsidian", lambda: open_app("obsidian", "ws5")),
                        5: ("PPSSPPSDL", lambda: open_app("PPSSPPSDL", "ws2")),
                        6: ("GBA", lambda: open_app("mgba-qt", "ws2")),
                        99: ("Salir", None)
                    }
                    for key, (app, _) in apps.items():
                        print(f"{key}) {app}")
                    print(separator)
                    app_selection = int(input("[+] Escoge una aplicación: "))
                    # Ejecuta la aplicación seleccionada
                    if app_selection in apps and apps[app_selection][1]:
                        apps[app_selection][1]()  # Ejecutar la función lambda asociada
                    elif app_selection == 99:
                        continue  # Si selecciona 'Salir', regresa al menú principal
                    else:
                        print("[!] Opción no válida.")
                       
################ Modulo de juegos
                elif selection == 6:
                    separator = "_" * 64
                    os.system("clear")
                    title = pyfiglet.figlet_format("Juegos", font="cosmic")
                    print(f"{title}\n{separator}\nEscoge una aplicación\n{separator}")
                    juegos = {
                        1: ("Gba", lambda: open_app("mgba-qt", "ws2"), lambda: open_app("spotify", "ws1")),
                        2: ("PSP", lambda: open_app("PPSSPPSDL", "ws2"), lambda: open_app("spotify", "ws1")),
                    }
                    for key, (juego, _, _) in juegos.items():
                        print(f"{key}) {juego}")
                    print(separator)
                    selection_games = int(input("[+] Escoge una aplicación: "))
                    if selection_games in juegos:
                        # Ejecutar la primera función lambda
                        juegos[selection_games][1]() 
                        # Ejecutar la segunda función lambda
                        juegos[selection_games][2]()  
                    elif selection_games == 99:
                        continue  # Si selecciona 'Salir', regresa al menú principal
                    else:
                        print("[!] Opción no válida.")                    
                elif selection in options and options[selection][1]:
                    options[selection][1]()  # Ejecuta la función asociada a la opción
                else:
                    print("[!] Opción no válida.")
            except ValueError:
                print("\n[!] Error: Ingresa un número válido.")
    except KeyboardInterrupt:
        print("\n[+] Saliendo... (Ctrl+C detectado)")
        sys.exit(0)
# Ejecutar el script
if __name__ == "__main__":
    main()
