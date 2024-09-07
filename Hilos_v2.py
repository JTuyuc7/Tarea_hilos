import threading
import time
import tkinter as tk
from tkinter import scrolledtext

# Variable global para controlar la finalización de los hilos
stop_threads = False

# Función para actualizar el reloj en el lado derecho
def update_clock(label):
    global stop_threads
    while not stop_threads:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        # Usamos 'after' para actualizar el label en el hilo principal
        label.after(0, label.config, {'text': f"Hora actual:\n{current_time}"})
        time.sleep(1)

# Función para manejar la entrada de texto
def handle_text_input(event, display_area, entry_field):
    input_text = entry_field.get()
    if input_text.strip():  # Evitar entradas vacías
        display_area.configure(state='normal')
        display_area.insert(tk.END, input_text + '\n')
        display_area.configure(state='disabled')
        entry_field.delete(0, tk.END)

# Función para detener la aplicación
def stop_app(root):
    global stop_threads
    stop_threads = True
    root.destroy()  # Cierra la ventana principal

# Función principal
def main():
    global stop_threads
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Aplicación con Hilos en Python")
    root.geometry("600x400")

    # Crear un frame para organizar los widgets
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Dividir la ventana en dos partes (izquierda y derecha)
    left_frame = tk.Frame(main_frame)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    right_frame = tk.Frame(main_frame)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # ---- Lado Izquierdo ----
    # Etiqueta de instrucción
    instruction_label = tk.Label(left_frame, text="Escribe tu texto aquí:")
    instruction_label.pack(pady=10)

    # Campo de entrada de texto
    text_entry = tk.Entry(left_frame, width=40)
    text_entry.pack(pady=5)

    # Área de texto para mostrar lo escrito
    display_area = scrolledtext.ScrolledText(left_frame, width=40, height=15, state='disabled')
    display_area.pack(pady=10)

    # Evento al presionar Enter en el campo de texto
    text_entry.bind('<Return>', lambda event: handle_text_input(event, display_area, text_entry))

    # ---- Lado Derecho ----
    # Etiqueta para mostrar el reloj
    clock_label = tk.Label(right_frame, text="Hora actual:\n--:--:--", font=("Helvetica", 16))
    clock_label.pack(pady=50)

    # Botón para detener la aplicación
    stop_button = tk.Button(right_frame, text="Detener Aplicación", command=lambda: stop_app(root))
    stop_button.pack(pady=20)

    # ---- Hilos ----
    # Hilo para actualizar el reloj
    clock_thread = threading.Thread(target=update_clock, args=(clock_label,))
    clock_thread.start()

    # Ejecutar la aplicación
    root.mainloop()

    # Esperar a que el hilo termine
    clock_thread.join()
    print("La aplicación ha finalizado.")

if __name__ == "__main__":
    main()
