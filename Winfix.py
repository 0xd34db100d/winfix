from logging import exception
import os
import sys
from ctypes import windll
import psutil
import customtkinter
import tkinter
from readchar import readkey
windll.kernel32.SetConsoleTitleW("Winfix v1.1")

def exit():
    print("\nPress any key to exit...")
    readkey()

def internet():
    os.system("ipconfig /flushdns & ipconfig /release & ipconfig /renew & netsh winsock reset")

def clipboard():
    os.system("dir | clip")
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

def explorer():
    for proc in psutil.process_iter():
        if proc.name() == "explorer.exe":
            proc.kill()

def gui():
    print("Running gui mode! Type: 'Winfix list' or 'Winfix -l' to show cmd options.\nWARNING! YOU WILL SEE ALL COMMANDS OUTPUT, THERE CAN BE YOUR MAC ADDRESSES AND IP`s")
    root = customtkinter.CTk()
    try:
        path_to_icon = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icon/gear.ico')) 
        root.iconbitmap(path_to_icon)
    except:
        pass
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("green")
    root.title("Winfix v1.1")
    root.geometry("300x400")
    root.resizable(False, False)

    def guiclip():
        try:
            clipboard()
        except Exception:
            termf.insert(tkinter.END, "[Clipboard] Error!\n")
            print("[Clipboard] Error!\n")
        termf.insert(tkinter.END, "[Clipboard] Applied!\n")
        print("[Clipboard] Applied!\n")

    def guiinternet():
        try:
            internet()
        except Exception:
            termf.insert(tkinter.END, "[Internet] Error!\n")
            print("[Internet] Error!\n")
        termf.insert(tkinter.END, "[Internet] Applied! I recommend restarting PC.\n")
        print("[Internet] Applied! I recommend restarting PC.\n")

    def guiexplorer():
        try:
            explorer()
        except Exception:
            termf.insert(tkinter.END, "[Explorer] Error!\n")
            print("[Explorer] Error!\n")
        termf.insert(tkinter.END, "[Explorer] Applied!\n")
        print("[Explorer] Applied!\n")

    label = customtkinter.CTkLabel(master=root, text="Welcome to winfix!\nJust click what you want to apply :3\nMade by Exitiale#1024")
    label.pack(pady=10, padx=10)

    clipboardbtn = customtkinter.CTkButton(master=root, text="Clipboard fix", command=guiclip)
    clipboardbtn.pack(pady=10, padx=10)

    internetbtn = customtkinter.CTkButton(master=root, text="Internet fix", command=guiinternet)
    internetbtn.pack(pady=10, padx=10)

    explorerbtn = customtkinter.CTkButton(master=root, text="Explorer fix", command=guiexplorer)
    explorerbtn.pack(pady=10, padx=10)

    termf = customtkinter.CTkTextbox(root, height=250, width=300)
    termf.bind("<Key>", lambda e: "break")
    termf.pack(pady=10, padx=10)

    root.mainloop()

try:
    if (sys.argv[1] == "list" or sys.argv[1] == "-l"):
        print(
            'List of available fixes:\n\n     + Internet fix ("Winfix.exe internet" or "Winfix.exe -i") - Use this for clear DNS Cache and renew IP, reset Winsock. [WARNING! YOU WILL SEE ALL COMMANDS OUTPUT, THERE CAN BE YOUR MAC ADDRESSES AND IP`s] \n\n     + Clipboard fix ("Winfix.exe clipboard" or "Winfix.exe -c") - Use this if you have broken clipboard.\n\n     + Explorer fix ("Winfix.exe explorer" or "Winfix.exe -e") - Use this if you have problems with desktop (restart explorer.exe).\n')
        exit()
    elif (sys.argv[1] == "internet" or sys.argv[1] == "-i"):
        print('Running internet fix...')
        internet()
        print("\nInternet fix was applied successfully! I recommend restarting PC.")
        exit()
    elif (sys.argv[1] == "clipboard" or sys.argv[1] == "-c"):
        print('Running clipboard fix...')
        clipboard()
        print("\nClipboard fix was applied successfully!")
        exit()
    elif (sys.argv[1] == "explorer" or sys.argv[1] == "-e"):
        print('Running explorer fix...')
        explorer()
        print("\nExplorer fix was applied successfully!")
        exit()
    else:
        print("Can't find arg. Running gui...")
        gui()
except:
    gui()

