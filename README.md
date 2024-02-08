# PyMonitor
This is an **utterly** simple Python implementation which fetches real-time CPU & memory information directly from a Windows host.
# Download
The source code has been compiled in a way so that the program can run without the existence of Python (alongside the source code's required libraries). It can be found [here](https://github.com/GabrielRogd/PyMonitor/releases).
# Build
The program can be compiled using the **pyinstaller** library.

 - ``pip install -r requirements.txt`` (make sure the required library is installed - it's just psutil lol)
 - ``pip install pyinstaller`` (install the library through pip)
 - ``pyinstaller --onefile --noconsole PyMonitor.py`` (compile the code into an executable - wait until finished)

 The executable will be found in the **dist** folder (inside the repo folder).