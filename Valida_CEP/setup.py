import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","clipboard","openpyxl","subprocess", "numpy","pandas","difflib", "requests","shutil","time", "datetime","json","connection","unidecode","unicodedata"]}

# build_exe_options = {}
# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

setup(  name = "Busca CEP",
        version = "1.0",
        description = "Script para consulta de cep na api VIACEP e validação de endereço.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("script.py")])