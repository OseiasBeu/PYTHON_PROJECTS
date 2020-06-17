import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os","clipboard","openpyxl","subprocess"]}
build_exe_options = {}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(  name = "upload drive",
        version = "1.0",
        description = "upload api drive",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Main.py")])

        # python3 setup.py build