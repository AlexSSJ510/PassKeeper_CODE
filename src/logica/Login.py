import json
import tkinter as tk
from tkinter import messagebox

from src.logica.Contraseñas import Contrasena
from src.logica.Contraseñas import GestorContraseñas

gestor = GestorContraseñas()
class Contrasena:
    def __init__(self, contrasena):
        self.valor = contrasena


class GestorContraseñas:
    def __init__(self):
        self.contrasenas = {}  # Diccionario que almacenará contraseñas, clave: (usuario, red)

    def agregar_contrasena(self, usuario, red, contrasena):
        self.contrasenas[(usuario, red)] = contrasena
        return "Contraseña agregada correctamente."

    def editar_contrasena(self, usuario, red, nueva_contrasena):
        if (usuario, red) in self.contrasenas:
            self.contrasenas[(usuario, red)] = Contrasena(nueva_contrasena)
            return "Contraseña editada correctamente."
        return "Usuario no encontrado."

    def eliminar_contrasena(self, usuario, red):
        if (usuario, red) in self.contrasenas:
            del self.contrasenas[(usuario, red)]
            return "Contraseña eliminada correctamente."
        return "Usuario no encontrado."


# Función de Login
def login():
    def verificar_login():
        username = entry_username.get()
        password = entry_password.get()

        # Aquí podrías realizar una verificación más real, como comparar con una base de datos.
        if username == "admin" and password == "admin":
            ventana_login.destroy()  # Cierra la ventana de login
            mostrar_ventana_principal()  # Muestra la ventana principal después del login
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos.")

    ventana_login = tk.Toplevel()
    ventana_login.title("Login")
    ventana_login.geometry("300x200")

    # Campos de entrada de usuario y contraseña
    lbl_username = tk.Label(ventana_login, text="Usuario:")
    lbl_username.pack(pady=10)
    entry_username = tk.Entry(ventana_login)
    entry_username.pack(pady=5)

    lbl_password = tk.Label(ventana_login, text="Contraseña:")
    lbl_password.pack(pady=10)
    entry_password = tk.Entry(ventana_login, show="*")
    entry_password.pack(pady=5)

    btn_login = tk.Button(ventana_login, text="Login", command=verificar_login)
    btn_login.pack(pady=20)


# Función que muestra la ventana principal después del login
def mostrar_ventana_principal():
    global root
    root = tk.Tk()
    root.title("PassKeeper - Gestor de Contraseñas")
    root.geometry("500x600")
    root.configure(bg="#5b5962")

    fuente_boton = ("Times New Roman", 12)
    color_boton = "#262335"

    # Etiquetas y campos de entrada
    lbl_instrucciones = tk.Label(root, text="PassKeeper - Gestor de Contraseñas", font=("Times New Roman", 20),
                                 bg="#5b5962", fg="#96a5b1")
    lbl_instrucciones.pack(pady=10)

    image_path = "src/vista/Candado.png"  # Asegúrate de que esta ruta sea correcta
    img = tk.PhotoImage(file=image_path)
    image_label = tk.Label(root, image=img)
    image_label.pack(pady=10)

    # Modificar los botones en la ventana principal
    btn_agregar = tk.Button(root, text="Agregar Contraseña", command=abrir_agregar_contrasena, font=fuente_boton,
                            bg=color_boton, width=20, fg="white")
    btn_agregar.pack(pady=10)

    btn_editar = tk.Button(root, text="Editar Contraseña", command=abrir_editar_contrasena, font=fuente_boton,
                           bg=color_boton, width=20, fg="white")
    btn_editar.pack(pady=10)

    btn_eliminar = tk.Button(root, text="Eliminar Contraseña", command=abrir_eliminar_contrasena, font=fuente_boton,
                             bg=color_boton, width=20, fg="white")
    btn_eliminar.pack(pady=10)

    btn_ver_contrasenas = tk.Button(root, text="Ver Contraseñas", command=mostrar_contrasenas(), font=fuente_boton,
                                    bg=color_boton, width=20, fg="white")
    btn_ver_contrasenas.pack(pady=10)

    btn_backup = tk.Button(root, text="Realizar Backup", command=backup_contrasenas, font=fuente_boton, bg=color_boton,
                           width=20, fg="white")
    btn_backup.pack(pady=10)

    btn_restaurar = tk.Button(root, text="Restaurar desde Backup", command=restaurar_contrasenas, font=fuente_boton,
                              bg=color_boton, width=20, fg="white")
    btn_restaurar.pack(pady=10)

    root.mainloop()


# Funciones de las opciones (agregar, editar, eliminar, etc.)
def abrir_agregar_contrasena():
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Contraseña")
    ventana_agregar.geometry("400x400")
    ventana_agregar.configure(bg="#5b5962")

    lbl_username = tk.Label(ventana_agregar, text="Nombre de Usuario:", font=("Times New Roman", 13), bg="#1e1644", fg="White")
    lbl_username.pack(pady=5)
    entry_username = tk.Entry(ventana_agregar)
    entry_username.pack(pady=5)

    lbl_red = tk.Label(ventana_agregar, text="Red (Servicio/App):", font=("Times New Roman", 13), bg="#1e1644", fg="White")
    lbl_red.pack(pady=5)
    entry_red = tk.Entry(ventana_agregar)
    entry_red.pack(pady=5)

    lbl_contrasena = tk.Label(ventana_agregar, text="Nueva Contraseña:", font=("Times New Roman", 13), bg="#1e1644", fg="White")
    lbl_contrasena.pack(pady=5)
    entry_contrasena = tk.Entry(ventana_agregar, show="*")
    entry_contrasena.pack(pady=5)

    lbl_confirmar = tk.Label(ventana_agregar, text="Confirmar Contraseña:", font=("Times New Roman", 13), bg="#1e1644", fg="White")
    lbl_confirmar.pack(pady=5)
    entry_confirmar = tk.Entry(ventana_agregar, show="*")
    entry_confirmar.pack(pady=5)

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
    btn_guardar = tk.Button(ventana_agregar, text="Guardar", command=guardar_contrasena, font=("Times New Roman", 12), bg="#262335", width=20, fg="white")
    btn_guardar.pack(pady=20)

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_agregar, text="Cerrar", command=ventana_agregar.destroy, font=("Times New Roman", 12), bg="#262335", width=20, fg="white")
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
    combo_usuarios.set(f"{usuarios[0][0]} - {usuarios[0][1]}")  # Valor por defecto
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


def mostrar_contrasenas():
    ventana_mostrar = tk.Toplevel(root)
    ventana_mostrar.title("Contraseñas Registradas")
    ventana_mostrar.geometry("500x400")

    lista_contrasenas = tk.Listbox(ventana_mostrar, width=60, height=15)
    lista_contrasenas.pack(pady=10)

    for (usuario, red), contrasena in gestor.contrasenas.items():
        lista_contrasenas.insert(tk.END, f"{usuario} - {red}: {contrasena.valor}")

    # Botón para cerrar
    btn_cerrar = tk.Button(ventana_mostrar, text="Cerrar", command=ventana_mostrar.destroy)
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
        # Abrir el archivo de backup
        with open("backup_contrasenas.json", "r") as archivo:
            contrasenas_data = json.load(archivo)  # Cargar los datos del archivo JSON

        # Verificar si el archivo contiene datos
        if not contrasenas_data:
            messagebox.showwarning("Advertencia", "El archivo de backup está vacío.")
            return

        # Restaurar las contraseñas
        for usuario_red, contrasena in contrasenas_data.items():
            # Separar usuario y red
            usuario, red = usuario_red.split(" - ")

            # Agregar la contraseña al gestor de contraseñas
            resultado = gestor.agregar_contrasena(usuario, red, Contrasena(contrasena))

        messagebox.showinfo("Restauración Exitosa", "Las contraseñas se han restaurado correctamente desde el backup.")

    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo de backup.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "El archivo de backup no es válido o está corrupto.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo restaurar el backup. Error: {str(e)}")

# Inicia la aplicación mostrando la ventana de login
login()
