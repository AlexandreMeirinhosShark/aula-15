import tkinter as tk
root = tk.Tk()
root.title("Color Changer")
root.geometry("500x400+400+100")
root.wm_resizable(width=False, height=False)

azul = "#0000ff"
vermelho = "#ff0000"
amarelo = "#ffff00"
verde = "#00ff00"


def bg_blue():
    root.config(background=azul)


def bg_red():
    root.config(background=vermelho)


def bg_yellow():
    root.config(background=amarelo)


def bg_green():
    root.config(background=verde)


btn1 = tk.Button(root, text="Azul", font="Fixedsys 18 underline", command=bg_blue)
btn1.place(width=200, height=160, x=40, y=20)

btn2 = tk.Button(root, text="Vermelho", font="Fixedsys 18 underline", command=bg_red)
btn2.place(width=200, height=160, x=260, y=20)

btn3 = tk.Button(root, text="Verde", font="Fixedsys 18 underline", command=bg_green)
btn3.place(width=200, height=160, x=40, y=200)

btn4 = tk.Button(root, text="Amarelo", font="Fixedsys 18 underline", command=bg_yellow)
btn4.place(width=200, height=160, x=260, y=200)
root.mainloop()
