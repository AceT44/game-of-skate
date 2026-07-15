import PyInstaller.__main__

PyInstaller.__main__.run([
    'tkinter_skate.py',
    '--windowed',
    '--icon=assets/skate_icon.icns'
])
