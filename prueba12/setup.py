import sys
from cx_Freeze import setup, Executable

setup(
    name="Ejecutable",
    version="1.0",
    description="Descripción de tu aplicación",
    executables=[Executable("prueba12_Ejecutable.py", base=None)]
)
