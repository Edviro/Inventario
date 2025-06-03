import os
import sys
import tkinter as tk
from tkinter import messagebox

# Asegurar que el directorio raíz esté en el path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importaciones de la aplicación
from database.connection import DatabaseConnection
from views.main_window import MainWindow

def main():
    # Inicializar la base de datos
    db = DatabaseConnection()
    try:
        db.create_tables()
    except Exception as e:
        messagebox.showerror("Error de Base de Datos", f"Error al inicializar la base de datos: {str(e)}")
        return
    
    # Inicializar la aplicación Tkinter
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()