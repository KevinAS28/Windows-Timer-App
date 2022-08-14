import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": ["tkinter", 'PIL', 'psutil', 'ctypes'], 'include_files': ('images', 'quotas.json', 'config.json'), 'include_msvcr': True}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# setup(
#     name = "simple_Tkinter",
#     version = "0.1",
#     description = "Sample cx_Freeze Tkinter script",
#     options = {"build_exe": build_exe_options},
#     executables = [Executable("the timer.py", base = base)])

setup(  name = "lapas",
        version = "0.1",
        description = "lapas",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)],

        )