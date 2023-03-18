import tkinter as tk
import functions
import pyscreenshot as ImageGrab
from time import sleep

def select_region(entry_widget):
    def on_mouse_down(event):
        nonlocal start_x, start_y
        start_x, start_y = event.x_root, event.y_root
        canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red", tag="selection")

    def on_mouse_move(event):
        nonlocal start_x, start_y
        canvas.coords("selection", start_x, start_y, event.x_root, event.y_root)

    def on_mouse_up(event):
        nonlocal start_x, start_y
        end_x, end_y = event.x_root, event.y_root
        region = (start_x, start_y, end_x, end_y)
        entry_widget.delete(0, "end")
        entry_widget.insert(0, str(region))
        selection_window.destroy()

    start_x, start_y = 0, 0
    selection_window = tk.Toplevel()
    selection_window.overrideredirect(1)
    selection_window.attributes("-topmost", True, "-alpha", 0.3)
    selection_window.geometry(f"{selection_window.winfo_screenwidth()}x{selection_window.winfo_screenheight()}")

    canvas = tk.Canvas(selection_window, bg="grey", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.bind("<Button-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_move)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)

    selection_window.mainloop()

window = tk.Tk()
window.title("Bot Monitoramento de Números")

label_region1 = tk.Label(window, text="Caminho da imagem 1:")
entry_region1 = tk.Entry(window)
button_select_region1 = tk.Button(window, text="Selecionar região", command=lambda: select_region(entry_region1))

label_target_number1 = tk.Label(window, text="Número alvo 1:")
entry_target_number1 = tk.Entry(window)

label_key1 = tk.Label(window, text="Tecla 1:")
entry_key1 = tk.Entry(window)

label_region2 = tk.Label(window, text="Caminho da imagem 2:")
entry_region2 = tk.Entry(window)
button_select_region2 = tk.Button(window, text="Selecionar região", command=lambda: select_region(entry_region2))

label_target_number2 = tk.Label(window, text="Número alvo 2:")
entry_target_number2 = tk.Entry(window)

label_key2 = tk.Label(window, text="Tecla 2:")
entry_key2 = tk.Entry(window)

button_start = tk.Button(window, text="Iniciar", command=lambda: functions.start_monitoring(
    entry_region1.get(),
    entry_target_number1.get(),
    entry_key1.get(),
    entry_region2.get(),
    entry_target_number2.get(),
    entry_key2.get()
))

button_stop = tk.Button(window, text="Parar", command=functions.stop_monitoring)

label_region1.grid(column=0, row=0)
entry_region1.grid(column=1, row=0)
button_select_region1.grid(column=2, row=0)

label_target_number1.grid(column=0, row=1)
entry_target_number1.grid(column=1, row=1)

label_key1.grid(column=0, row=2)
entry_key1.grid(column=1, row=2)

label_region2.grid(column=0, row=3)
entry_region2.grid(column=1, row=3)
button_select_region2.grid(column=2, row=3)

label_target_number2.grid(column=0, row=4)
entry_target_number2.grid(column=1, row=4)

label_key2.grid(column=0, row=5)
entry_key2.grid(column=1, row=5)


button_start.grid(column=0, row=6)
button_stop.grid(column=1, row=6)

window.mainloop()

