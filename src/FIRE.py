import pymem
import pymem.process
import customtkinter as ctk
from PIL import Image
import os
import sys

OFFSET_XRAY = 0xC060DC

# Use a consistent base path for resources both in development and when packaged by PyInstaller.
# When running as a PyInstaller onefile bundle, sys._MEIPASS points to the temporary unpack directory.
BASE_PATH = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

def resource_path(path: str) -> str:
    """Return an absolute path to a resource, working for both dev and PyInstaller builds."""
    return os.path.join(BASE_PATH, path)

caminhoIcone = resource_path(os.path.join("ICON", "fire.ico"))
caminhoWall = resource_path(os.path.join("ICON", "wall.png"))


def limpar_frame():
    for widget in frameConteudo.winfo_children():
        widget.destroy()

def acc():
    try:
        pm = pymem.Pymem("cs2.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        alvo = client + OFFSET_XRAY
        
        if box.get() == 1:
            pm.write_bytes(alvo, b'\x01', 1)
        else:
            pm.write_bytes(alvo, b'\x00', 1)
    except Exception as e:
        print(f"Erro: Abra o CS2 primeiro! ({e})")


def sair():
    return app.destroy()

def FuncaoMain():
    global box
    limpar_frame()
    main = ctk.CTkLabel(frameConteudo,text="MAIN",text_color="#6C048B",font=("Impact",24))
    main.pack(pady=10,anchor="c")


    box = ctk.CTkCheckBox(frameConteudo,text="ESP DE PLAYER",border_color="#8F108F",fg_color="purple",hover_color="#230045",command=acc)
    box.pack(padx=20, pady=10, anchor="w")

    box2 = ctk.CTkCheckBox(frameConteudo,text="Sair",border_color="#8F108F",fg_color="#230045",hover_color="#230045",command=sair)
    box2.pack(padx=20, pady=10, anchor="w")

    my_image = ctk.CTkImage(dark_image=Image.open(caminhoWall),size=(150,150))
    imagemlam = ctk.CTkLabel(frameConteudo,image=my_image,text="")
    imagemlam.place(x=250, y=40)
    
def infoMain():
    limpar_frame()

    inf = ctk.CTkLabel(frameConteudo,text="INFORMAÇÃO",text_color="#6C048B",font=("Impact",24))
    inf.pack(pady=10,anchor="c")

    infoBox = ctk.CTkLabel(frameConteudo,text="Criador: ZERO",font=("JetBrains Mono", 16))
    infoBox.pack(pady=5,anchor="c")

    infoBox2 = ctk.CTkLabel(frameConteudo,text="DISCORD: olho_zero",font=("JetBrains Mono", 16))
    infoBox2.pack(pady=5,anchor="c")

    inf = ctk.CTkLabel(frameConteudo,text="MODELO DO PAINEL (PREMIUM)",text_color="#6C048B",font=("Impact",24))
    inf.pack(pady=10,anchor="c")


app = ctk.CTk()
app.iconbitmap(caminhoIcone)
app.geometry("600x400")
app.title("FIRE CS")
app._apply_appearance_mode("dark")

frameinicil = ctk.CTkFrame(app,width=150,height=1000,fg_color="#1a1a1a",corner_radius=0)
frameinicil.propagate(False)
frameinicil.pack(side="left", fill="y")

frameConteudo = ctk.CTkFrame(app,fg_color="#252525",corner_radius=0)
frameConteudo.pack(side="left", expand=True,fill="both")

nome = ctk.CTkLabel(frameinicil,text="FIRE CS",text_color="#6A0E86",font=("Impact",24))
nome.pack(pady=10)

frameMain = ctk.CTkButton(frameinicil,text="MAIN",fg_color="#72076D",hover_color="#5C2C59",command=FuncaoMain)
frameMain.pack(pady=20,padx=10)

frameSobre = ctk.CTkButton(frameinicil,text="INFO",fg_color="#72076D",hover_color="#5C2C59",command=infoMain)
frameSobre.pack(pady=20,padx=10)

app.mainloop()