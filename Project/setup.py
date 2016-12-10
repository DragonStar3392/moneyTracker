import cx_Freeze
import sys
import os
import tkinter

os.environ['TCL_LIBRARY'] = "C:\\Users\\My Document\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\My Document\\AppData\\Local\\Programs\\Python\\Python35\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Main.py", base=base, icon="coin2.ico")]
includefiles= ["displayPage.py","modifyPage.py","warningPage.py","Payment.txt","coin2.ico",
               "tcl86t.dll","tk86t.dll"]

cx_Freeze.setup(
    name = "MoneyTracker",
    options = {"build_exe":{"packages":["os"],
                            "includes":["tkinter"],
                            "include_files":includefiles}},
    version = "0.0.9",
    description = "Made by Shouh Yann Mo, ID: 59090029, KMITL",
    executables = executables
    )
'''
executables = [cx_Freeze.Executable("Main.py", base=base, icon="coin2.ico")]

cx_Freeze.setup(
    name = "MoneyTracker",
    options = {"build_exe":{"packages":["tkinter"],"include_files":["coin2.ico"]}},
    version = "0.0.8",
    description = "Made by Shouh Yann Mo, ID: 59090029, KMITL",
    executables = executables
    )
'''
