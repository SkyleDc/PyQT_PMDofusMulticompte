# PMMultiCompteDofus - This tool is in Work In Progress.

This tool is intended to simplify Multi-Account gameplay on Dofus by allowing the player to switch between Dofus windows only.

# What language is this tool using ?

This tool has been developped by SkyleDc under Python 3.9.6 with PyCharm.
It uses the PyQt5 library as well as pywin32 (win32gui) and pynput (May get removed later).

# How does it work ?

This tool checks every running Dofus.exe windows and embed them in a QTabWidget.
If it doesn't find any Dofus.exe, it creates an empty tab in the QTabWidget.

It also detects keyboard events (keypresses) but this may get removed later as I need to figure out how to make it work with QT.

# What does this tool allows me to do ?

This tool allows you to embed all running Dofus.exe in a single Qt app.
This allows you to switch between tabs faster with a single keypress (not yet implemented).

# What is missing atm ? Are there bugs ?

- Tab switch shortcut/hotkey is missing
- Refresh shortcut/hotkey to embed newly launched Dofus windows is missing
- There's a bug where embeded Dofus windows loses their Window_Name
  (You can see this in your Task Manager : Non embeded Dofus name is "Dofus <version>" or "<Your character name>" but embeded dofus will just display "Dofus.exe")
- There's a bug where embeded Dofus.exe won't accept text selection, copy, cut and paste after clicking on the QT app itself (Eveything not being Dofus)

If you know how to fix bugs/improve this app, feel free to contact me either on discord (Skyle#3260), either in the issues category of this repository.