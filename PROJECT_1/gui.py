import tkinter as tk
import pygame
pygame.mixer.init()
from logic import tekan_logic, hitung_logic, clear_logic


BG_COLOR = "#1b1b1b"
BTN_NUM = "#C49A6C"       
BTN_OP = "#61C13A"      
BTN_FUNC = "#8A8A8A"      
BTN_EQUAL = "#E0C14A"     

def play_click():
    pygame.mixer.Sound("click.mp3").play()
def main():
    root = tk.Tk()
    root.title("Minecraft iOS Calculator - Dea")
    root.geometry("330x480")
    root.config(bg=BG_COLOR)


    display = tk.Entry(
        root,
        font=("Courier New", 26, "bold"),
        bg="#2b2b2b",
        fg="white",
        justify="right",
        bd=5,
        relief="ridge"
    )
    display.pack(fill="x", padx=15, pady=15, ipady=12)


    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(expand=True, fill="both")

    tombol = [
        ("C", BTN_FUNC), ("+/-", BTN_FUNC), ("%", BTN_FUNC), ("/", BTN_OP),
        ("7", BTN_NUM), ("8", BTN_NUM), ("9", BTN_NUM), ("*", BTN_OP),
        ("4", BTN_NUM), ("5", BTN_NUM), ("6", BTN_NUM), ("-", BTN_OP),
        ("1", BTN_NUM), ("2", BTN_NUM), ("3", BTN_NUM), ("+", BTN_OP),
        ("0", BTN_NUM), (".", BTN_NUM), ("=", BTN_EQUAL)
    ]

    row = 0
    col = 0

    for text, color in tombol:
        
        def buat_cmd(t=text):
            if t == "C":
                return lambda: display_replace(display, clear_logic())

            elif t == "=":
                return lambda: action(
    play_click,
    lambda: display_replace(display, hitung_logic(display.get()))
)

            elif t == "+/-":
                return lambda: toggle_minus(display)

            else: 
                return lambda: (play_click(), display_replace(display, tekan_logic(display.get(), t)))

        btn = tk.Button(
            frame,
            text=text,
            font=("Courier New", 16, "bold"),
            bg=color,
            fg="white",
            bd=3,
            relief="ridge",
            command=buat_cmd()
        )

        if text == "0":
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
            col += 2
        else:
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            col += 1

        if col > 3:
            col = 0
            row += 1

    for i in range(6):
        frame.rowconfigure(i, weight=1)
    for i in range(4):
        frame.columnconfigure(i, weight=1)

    root.mainloop()

def action(*funcs):
    for f in funcs:
        f()
def display_replace(display, value):
    display.delete(0, tk.END)
    display.insert(0, value)

def toggle_minus(display):
    text = display.get()
    if text.startswith("-"):
        display_replace(display, text[1:])
    else:
        display_replace(display, "-" + text)


if __name__ == "__main__":
    main()

