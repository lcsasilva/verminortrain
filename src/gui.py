import tkinter as tk

def create_gui(window, select_region, start_monitoring, stop_monitoring):
    # Labels, Entries e Botões para a imagem 1
    label_region1 = tk.Label(window, text="Caminho da imagem 1:")
    entry_region1 = tk.Entry(window)
    button_select_region1 = tk.Button(window, text="Selecionar região", command=lambda: select_region(entry_region1))

    label_target_number1 = tk.Label(window, text="Número alvo 1:")
    entry_target_number1 = tk.Entry(window)

    label_key1 = tk.Label(window, text="Tecla 1:")
    entry_key1 = tk.Entry(window)

    # Labels, Entries e Botões para a imagem 2
    label_region2 = tk.Label(window, text="Caminho da imagem 2:")
    entry_region2 = tk.Entry(window)
    button_select_region2 = tk.Button(window, text="Selecionar região", command=lambda: select_region(entry_region2))

    label_target_number2 = tk.Label(window, text="Número alvo 2:")
    entry_target_number2 = tk.Entry(window)

    label_key2 = tk.Label(window, text="Tecla 2:")
    entry_key2 = tk.Entry(window)

    # Botões Iniciar e Parar
    button_start = tk.Button(window, text="Iniciar", command=lambda: start_monitoring(
        entry_region1.get(),
        entry_target_number1.get(),
        entry_key1.get(),
        entry_region2.get(),
        entry_target_number2.get(),
        entry_key2.get()
    ))

    button_stop = tk.Button(window, text="Parar", command=stop_monitoring)

    # Organizando os elementos na janela usando grid
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
