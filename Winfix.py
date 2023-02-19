from logging import exception
import os
import signal
import sys
from ctypes import windll
from time import sleep
import psutil
import readchar

windll.kernel32.SetConsoleTitleW("Winfix")


print('WinFix is a small script for fixing annoying Windows 10 bugs and errors. © John Strider 2022\nCurrent version: 1.0\n')


def internet():
    os.system("ipconfig /flushdns")
    os.system("ipconfig /release")
    os.system("ipconfig /renew")
    os.system("netsh winsock reset")


def clipboard():
    os.system("dir | clip")
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()


def explorer():
    for proc in psutil.process_iter():
        if proc.name() == "explorer.exe":
            proc.kill()


try:
    if (sys.argv[1] == "list" or sys.argv[1] == "-l"):
        print(
            'List of available fixes:\n\n     + Internet fix ("Winfix.exe internet" or "Winfix.exe -i") - Use this for clear DNS Cache and renew IP, reset Winsock. [WARNING! YOU WILL SEE ALL COMMANDS OUTPUT, THERE CAN BE YOUR MAC ADDRESSES AND IP`s] \n\n     + Clipboard fix ("Winfix.exe clipboard" or "Winfix.exe -c") - Use this if you have broken clipboard.\n\n     + Explorer fix ("Winfix.exe explorer" or "Winfix.exe -e") - Use this if you have problems with desktop (restart explorer.exe).\n')
    elif (sys.argv[1] == "internet" or sys.argv[1] == "-i"):
        print('Running internet fix...')
        internet()
        print("\nInternet fix was applied successfully! I recommend restarting PC.")
    elif (sys.argv[1] == "clipboard" or sys.argv[1] == "-c"):
        print('Running clipboard fix...')
        clipboard()
        print("\nClipboard fix was applied successfully!")
    elif (sys.argv[1] == "explorer" or sys.argv[1] == "-e"):
        print('Running explorer fix...')
        explorer()
        print("\nExplorer fix was applied successfully!")
    else:
        print('OH, looks like there is some problem with input or error :<\n\nPlease, write "winfix.exe list" or "winfix.exe -l" to print available fixes. :3 \n')
except:
    print('OH, looks like there is some problem with input or error :<\n\nPlease, write "winfix.exe list" or "winfix.exe -l" to print available fixes. :3 \n')

print("\nPress any key to exit...")
k = readchar.readchar()
