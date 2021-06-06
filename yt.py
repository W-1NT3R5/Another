try:
    import colorama
    colorama.init()
    import time
    import ctypes
    import os
        
    '''
 _____
(___  )                    _               
    | |   __    ___   ___ (_)   ___    _ _ 
 _  | | /'__`\/',__)/',__)| | /'___) /'_` )
( )_| |(  ___/\__, \\__, \| |( (___ ( (_| |
`\___/'`\____)(____/(____/(_)`\____)`\__,_)                                       
    '''

    from pytube import *
    from colorama import Fore,Back,Style
    from ctypes import windll, byref
    from ctypes.wintypes import SMALL_RECT
except Exception as e:
    print(f"Error: {e}(missing modules)")
try:
    os.system('cls')
except:
    print("Windows only!!")
try:
    LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 12
    font.dwFontSize.X = 12
    font.dwFontSize.Y = 19
    font.FontFamily = 54
    font.FontWeight = 400
    font.FaceName = "Lucida Console"
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font))
except:
    print("Failed!,loading default configuration........")
def ui():
    print(Fore.RED+'''
                              YT VIDEO DOWNLOADER
                                  
                                  author: H2O
    ''')
    Fore.RESET

def vid_dwn():
    try:
        yt_link = input(Fore.GREEN+"Enter the link to the yt video: ")
        start = time.time()
        yt = YouTube(yt_link).streams.first()
        print(Fore.GREEN+"[+][+]Downloading starting[+][+]")
        yt.download()
        end = time.time()
        print(Fore.GREEN+"[+][+]Downloading finished[+][+]")
        print(Fore.GREEN+f"Finished in {end-start}")
    except Exception as e:
        print(Fore.RED+f"Error:{e}")
ui()
vid_dwn()
Fore.RESET