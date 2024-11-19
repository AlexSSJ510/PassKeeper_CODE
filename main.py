import json
import tkinter as tk
from tkinter import messagebox

from src.logica.Contraseñas import Contrasena
from src.logica.Contraseñas import GestorContraseñas

# Crear el gestor de contraseñas
gestor = GestorContraseñas()


# Funciones para las acciones
def abrir_agregar_contrasena():
    # Crear una nueva ventana para agregar una contraseña
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Contraseña")
    ventana_agregar.geometry("400x400")

    # Etiqueta y campo para el nombre de usuario
    lbl_username = tk.Label(ventana_agregar, text="Nombre de Usuario:")
    lbl_username.pack(pady=5)
    entry_username = tk.Entry(ventana_agregar)
    entry_username.pack(pady=5)

    # Etiqueta y campo para la red
    lbl_red = tk.Label(ventana_agregar, text="Red (Servicio/App):")
    lbl_red.pack(pady=5)
    entry_red = tk.Entry(ventana_agregar)
    entry_red.pack(pady=5)

    # Etiqueta y campo para la nueva contraseña
    lbl_contrasena = tk.Label(ventana_agregar, text="Nueva Contraseña:")
    lbl_contrasena.pack(pady=5)
    entry_contrasena = tk.Entry(ventana_agregar, show="*")
    entry_contrasena.pack(pady=5)

    # Etiqueta y campo para confirmar contraseña
    lbl_confirmar = tk.Label(ventana_agregar, text="Confirmar Contraseña:")
    lbl_confirmar.pack(pady=5)
    entry_confirmar = tk.Entry(ventana_agregar, show="*")
    entry_confirmar.pack(pady=5)

    # Función para guardar la contraseña
    def guardar_contrasena():
        username = entry_username.get()
        red = entry_red.get()
        nueva_contra = entry_contrasena.get()
        confirmar_contra = entry_confirmar.get()

        if not username or not red or not nueva_contra or not confirmar_contra:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")
            return
        if nueva_contra != confirmar_contra:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        contrasena = Contrasena(nueva_contra)
        resultado = gestor.agregar_contrasena(username, red, contrasena)
        messagebox.showinfo("Resultado", resultado)
        ventana_agregar.destroy()

    # Botón para guardar la contraseña
    btn_guardar = tk.Button(ventana_agregar, text="Guardar", command=guardar_contrasena)
    btn_guardar.pack(pady=20)

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_agregar, text="Cerrar", command=ventana_agregar.destroy)
    btn_cerrar.pack(pady=10)


def abrir_editar_contrasena():
    ventana_editar = tk.Toplevel(root)
    ventana_editar.title("Editar Contraseña")
    ventana_editar.geometry("400x400")

    # Seleccionar usuario y red
    lbl_usuario = tk.Label(ventana_editar, text="Selecciona el Usuario:")
    lbl_usuario.pack(pady=5)
    usuarios = [(usuario, red) for usuario, red in gestor.contrasenas.keys()]
    if not usuarios:
        messagebox.showwarning("Advertencia", "No hay usuarios registrados.")
        ventana_editar.destroy()
        return
    combo_usuarios = tk.StringVar(ventana_editar)
    combo_usuarios.set(f"{usuarios[0][0]} - {usuarios[0][1]}")  # Valor por defecto
    menu_usuarios = tk.OptionMenu(ventana_editar, combo_usuarios, *[f"{u} - {r}" for u, r in usuarios])
    menu_usuarios.pack(pady=5)

    # Entrada para la nueva contraseña y confirmación
    lbl_nueva_contrasena = tk.Label(ventana_editar, text="Nueva Contraseña:")
    lbl_nueva_contrasena.pack(pady=5)
    entry_nueva_contrasena = tk.Entry(ventana_editar, show="*")
    entry_nueva_contrasena.pack(pady=5)

    lbl_confirmar = tk.Label(ventana_editar, text="Confirmar Contraseña:")
    lbl_confirmar.pack(pady=5)
    entry_confirmar = tk.Entry(ventana_editar, show="*")
    entry_confirmar.pack(pady=5)

    def guardar_cambios():
        seleccion = combo_usuarios.get()
        username, red = seleccion.split(" - ")
        nueva_contrasena = entry_nueva_contrasena.get()
        confirmar_contrasena = entry_confirmar.get()

        if not nueva_contrasena or not confirmar_contrasena:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")
            return
        if nueva_contrasena != confirmar_contrasena:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        resultado = gestor.editar_contrasena(username, red, nueva_contrasena)
        messagebox.showinfo("Resultado", resultado)
        ventana_editar.destroy()

    btn_guardar = tk.Button(ventana_editar, text="Guardar Cambios", command=guardar_cambios)
    btn_guardar.pack(pady=20)
    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_editar, text="Cerrar", command=ventana_editar.destroy)
    btn_cerrar.pack(pady=10)


def abrir_eliminar_contrasena():
    ventana_eliminar = tk.Toplevel(root)
    ventana_eliminar.title("Eliminar Contraseña")
    ventana_eliminar.geometry("400x300")

    # Seleccionar usuario y red
    lbl_usuario = tk.Label(ventana_eliminar, text="Selecciona el Usuario:")
    lbl_usuario.pack(pady=5)
    usuarios = [(usuario, red) for usuario, red in gestor.contrasenas.keys()]
    if not usuarios:
        messagebox.showwarning("Advertencia", "No hay usuarios registrados.")
        ventana_eliminar.destroy()
        return
    combo_usuarios = tk.StringVar(ventana_eliminar)
    combo_usuarios.set(f"{usuarios[0][0]} - {usuarios[0][1]}")
    menu_usuarios = tk.OptionMenu(ventana_eliminar, combo_usuarios, *[f"{u} - {r}" for u, r in usuarios])
    menu_usuarios.pack(pady=5)

    def eliminar():
        seleccion = combo_usuarios.get()
        username, red = seleccion.split(" - ")
        resultado = gestor.eliminar_contrasena(username, red)
        messagebox.showinfo("Resultado", resultado)
        ventana_eliminar.destroy()

    btn_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar)
    btn_eliminar.pack(pady=20)
    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_eliminar, text="Cerrar", command=ventana_eliminar.destroy)
    btn_cerrar.pack(pady=10)


def ver_contrasenas():
    # Crear una nueva ventana para ver las contraseñas
    ventana_ver = tk.Toplevel(root)
    ventana_ver.title("Ver Contraseñas")
    ventana_ver.geometry("400x400")

    # Scrollbar para manejar múltiples contraseñas
    frame_scroll = tk.Frame(ventana_ver)
    frame_scroll.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_scroll)
    scrollbar = tk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Mostrar cada contraseña registrada
    for (usuario, red), contrasena in gestor.contrasenas.items():
        # Formato: Red, Usuario, Contraseña
        frame_contrasena = tk.Frame(scrollable_frame, relief=tk.GROOVE, bd=2)
        frame_contrasena.pack(fill=tk.X, pady=5, padx=5)

        lbl_red = tk.Label(frame_contrasena, text=f"Red: {red}", font=("Arial", 12, "bold"))
        lbl_red.pack(anchor="w", padx=5)

        lbl_usuario = tk.Label(frame_contrasena, text=f"Usuario: {usuario}", font=("Arial", 10))
        lbl_usuario.pack(anchor="w", padx=5)

        lbl_contrasena = tk.Label(frame_contrasena, text=f"Contraseña: {'*' * len(contrasena.valor)}",
                                  font=("Arial", 10))
        lbl_contrasena.pack(anchor="w", padx=5)

        # Botón para mostrar la contraseña
        def mostrar_contrasena(lbl_contrasena=lbl_contrasena, contrasena=contrasena):
            if lbl_contrasena.cget("text").startswith("Contraseña: "):
                lbl_contrasena.config(text=f"Contraseña: {contrasena.valor}")
            else:
                lbl_contrasena.config(text=f"Contraseña: {'*' * len(contrasena.valor)}")

        btn_mostrar = tk.Button(frame_contrasena, text="VER 👁️", command=mostrar_contrasena)
        btn_mostrar.pack(anchor="e", padx=5, pady=2)
    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_ver, text="Cerrar", command=ventana_ver.destroy)
    btn_cerrar.pack(pady=10)


def backup_contrasenas():
    try:
        # Convertir las contraseñas a un formato adecuado para guardar en JSON
        contrasenas_data = {}
        for (usuario, red), contrasena in gestor.contrasenas.items():
            contrasenas_data[f"{usuario} - {red}"] = contrasena.valor

        # Guardar en un archivo JSON
        with open("backup_contrasenas.json", "w") as archivo:
            json.dump(contrasenas_data, archivo, indent=4)

        messagebox.showinfo("Backup Exitoso", "El backup de contraseñas se ha realizado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo realizar el backup. Error: {str(e)}")


def restaurar_contrasenas():
    try:
        # Leer el archivo JSON
        with open("backup_contrasenas.json", "r") as archivo:
            contrasenas_data = json.load(archivo)

        # Restaurar las contraseñas
        for usuario_red, contrasena in contrasenas_data.items():
            usuario, red = usuario_red.split(" - ")
            # Aquí se debe usar el método adecuado del gestor para agregar contraseñas
            gestor.agregar_contrasena(usuario, red, Contrasena(contrasena))

        messagebox.showinfo("Restauración Exitosa", "Las contraseñas se han restaurado correctamente desde el backup.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo restaurar el backup. Error: {str(e)}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("PassKeeper - Gestor de Contraseñas")
root.geometry("500x600")

# Etiquetas y campos de entrada
lbl_instrucciones = tk.Label(root, text="PassKeeper - Gestor de Contraseñas", font=("Arial", 16))
lbl_instrucciones.pack(pady=10)

image_path = "src/vista/Candado.png"
img = tk.PhotoImage(file=image_path)  # Cargar la imagen
image_label = tk.Label(root, image=img)  # Crear el label con la imagen
image_label.pack(pady=10)  # Empaquetar la imagen debajo del título

# Modificar el botón en la ventana principal
btn_agregar = tk.Button(root, text="Agregar Contraseña", command=abrir_agregar_contrasena)
btn_agregar.pack(pady=10)

btn_editar = tk.Button(root, text="Editar Contraseña", command=abrir_editar_contrasena)
btn_editar.pack(pady=10)

btn_eliminar = tk.Button(root, text="Eliminar Contraseña", command=abrir_eliminar_contrasena)
btn_eliminar.pack(pady=10)

# Añadir un botón en la ventana principal
btn_ver_contrasenas = tk.Button(root, text="Ver Contraseñas", command=ver_contrasenas)
btn_ver_contrasenas.pack(pady=10)

# Botón para Backup
btn_backup = tk.Button(root, text="Realizar Backup", command=backup_contrasenas)
btn_backup.pack(pady=10)

# Botón para Restaurar
btn_restaurar = tk.Button(root, text="Restaurar desde Backup", command=restaurar_contrasenas)
btn_restaurar.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
