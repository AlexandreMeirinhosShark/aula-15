import tkinter as tk
root = tk.Tk()
root.title("Clicker")


clicks = 0


def add():
    global clicks
    clicks = clicks + 1


def update_click():
    add()
    labl.configure(text=f"Clicks: {clicks}")


root.geometry('500x300+200+200')
root.wm_resizable(width=True, height=True)

clickbtn = tk.Button(root, text="Click here!", command=update_click, font="Arial 20 italic")
clickbtn.pack(pady=80)

labl = tk.Label(root, text=f"Clicks: {clicks}", font="Time 18 bold")
labl.pack(pady=100)

root.mainloop()
