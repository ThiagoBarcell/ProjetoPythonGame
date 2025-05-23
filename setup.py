from cx_Freeze import setup, Executable
import os

path = "./asset/Tema_Corrida"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path,asset).replace("\\", "/") for asset in asset_list]
print(asset_list_completa)

executables =[Executable("main.py")]
files = { "include_files": asset_list_completa,"packages":["pygame"] }

setup(
    name="Car_Scape",
    version="1.0",
    description="Car Scape app",
    options={"build_exe": files},
    executables=executables
)