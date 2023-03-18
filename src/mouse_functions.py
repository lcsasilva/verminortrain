import tkinter as tk

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
