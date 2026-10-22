#!/usr/bin/env python3
"""Minimal Hello window using stdlib tkinter."""

import tkinter as tk


def main() -> None:
    root = tk.Tk()
    root.title("Hello")
    label = tk.Label(root, text="Hello", padx=40, pady=30)
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
