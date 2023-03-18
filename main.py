import tkinter as tk
from src.gui import create_gui
from src.functions import start_monitoring, stop_monitoring
from src.mouse_functions import select_region

def main():
    window = tk.Tk()
    window.title("Train bot")

    create_gui(window, select_region, start_monitoring, stop_monitoring)

    window.mainloop()

if __name__ == "__main__":
    main()
