import json
import os
import tkinter as tk
from tkinter import messagebox

from src.logica.Contraseñas import Contrasena
from src.logica.Contraseñas import GestorContraseñas

gestor = GestorContraseñas()

USERS_FILE = "usuarios.json"


def cargar_imagen(path, ventana):
    try:
        img = tk.PhotoImage(file=path)
        image_label = tk.Label(ventana, image=img)
        image_label.image = img  # Mantener la referencia a la imagen
        image_label.pack(pady=10)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return None


def cargar_usuarios():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as archivo:
            return json.load(archivo)
    return {}


def guardar_usuarios(usuarios):
    with open(USERS_FILE, "w") as archivo:
        json.dump(usuarios, archivo, indent=4)


def mostrar_login():
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("500x600")
    login_window.configure(bg="#3a3a3a")

    lbl_titulo = tk.Label(login_window, text="Acceso a PassKeeper", font=("Helvetica", 18, "bold"), bg="#3a3a3a",
                          fg="white")
    lbl_titulo.pack(pady=20)

    image_path = "src/vista/Candado.png"
    cargar_imagen(image_path, login_window)

    lbl_username = tk.Label(login_window, text="Nombre de Usuario:", font=("Arial", 12), bg="#3a3a3a", fg="White")
    lbl_username.pack(pady=5)
    entry_username = tk.Entry(login_window, font=("Arial", 12), bd=2, relief="solid", width=25)
    entry_username.pack(pady=5)

    lbl_password = tk.Label(login_window, text="Contraseña:", font=("Arial", 12), bg="#3a3a3a", fg="White")
    lbl_password.pack(pady=5)
    entry_password = tk.Entry(login_window, show="*", font=("Arial", 12), bd=2, relief="solid", width=25)
    entry_password.pack(pady=5)

    usuarios = cargar_usuarios()

    def login():
        username = entry_username.get()
        password = entry_password.get()

        if username in usuarios and usuarios[username] == password:
            messagebox.showinfo("Login Exitoso", "Acceso concedido.")
            login_window.destroy()
            abrir_ventana_principal()
        else:
            messagebox.showerror("Login Fallido", "Usuario o contraseña incorrectos.")

    def registrar():
        registro_window = tk.Toplevel(login_window)
        registro_window.title("Registrar Nuevo Usuario")
        registro_window.geometry("400x300")
        registro_window.configure(bg="#3a3a3a")

        lbl_new_username = tk.Label(registro_window, text="Nuevo Nombre de Usuario:", font=("Arial", 12),
                                    bg="#3a3a3a", fg="White")
        lbl_new_username.pack(pady=10)
        entry_new_username = tk.Entry(registro_window, font=("Arial", 12), bd=2, relief="solid", width=25)
        entry_new_username.pack(pady=5)

        lbl_new_password = tk.Label(registro_window, text="Nueva Contraseña:", font=("Arial", 12),
                                    bg="#3a3a3a", fg="White")
        lbl_new_password.pack(pady=10)
        entry_new_password = tk.Entry(registro_window, show="*", font=("Arial", 12), bd=2, relief="solid", width=25)
        entry_new_password.pack(pady=5)

        def guardar_usuario():
            new_username = entry_new_username.get()
            new_password = entry_new_password.get()

            if new_username == "" or new_password == "":
                messagebox.showwarning("Campos Vacíos", "Debe completar todos los campos.")
                return

            if new_username in usuarios:
                messagebox.showwarning("Usuario Existente", "Este nombre de usuario ya está registrado.")
            else:
                # Guardar el nuevo usuario
                usuarios[new_username] = new_password
                guardar_usuarios(usuarios)
                messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente.")
                registro_window.destroy()

        btn_guardar_usuario = tk.Button(registro_window, text="Registrar", command=guardar_usuario,
                                        font=("Arial", 12), bg="#241f7f", width=20, fg="white")
        btn_guardar_usuario.pack(pady=20)

        btn_cerrar = tk.Button(registro_window, text="Cerrar", command=registro_window.destroy,
                               font=("Arial", 12), bg="#b83810", width=20, fg="white")
        btn_cerrar.pack(pady=10)

    btn_login = tk.Button(login_window, text="Iniciar Sesión", command=login, font=("Arial", 12), bg="#241f7f",
                          width=20, fg="white")
    btn_login.pack(pady=15)

    btn_registrar = tk.Button(login_window, text="Registrar Nuevo Usuario", command=registrar,
                              font=("Arial", 12), bg="#241f7f", width=20, fg="white")
    btn_registrar.pack(pady=10)

    btn_cerrar = tk.Button(login_window, text="Cerrar", command=login_window.destroy, font=("Arial", 12),
                           bg="#b83810", width=20, fg="white")
    btn_cerrar.pack(pady=10)


def abrir_ventana_principal():
    fuente_boton = ("Times New Roman", 12)
    color_boton = "#241f7f"
    color_instrucciones = "#A9A9A9"

    ventana_Principal = tk.Tk()
    ventana_Principal.title("PassKeeper - Gestor de Contraseñas")
    ventana_Principal.geometry("600x600")
    ventana_Principal.configure(bg="#3a3a3a")

    lbl_titulo = tk.Label(ventana_Principal, text="PassKeeper - Gestor de Contraseñas", font=("Arial", 20, "bold"),
                          bg="#3a3a3a",
                          fg="white")
    lbl_titulo.pack(pady=20)

    image_path = r"src\vista\Candado.png"
    cargar_imagen(image_path, ventana_Principal)

    lbl_descripcion = tk.Label(ventana_Principal, text="Organiza y gestiona tus contraseñas de forma segura.",
                               font=("Arial", 14),
                               bg="#3a3a3a", fg=color_instrucciones)
    lbl_descripcion.pack(pady=10)

    btn_agregar = tk.Button(ventana_Principal, text="Agregar Contraseña", command=abrir_agregar_contrasena,
                            font=fuente_boton,
                            bg=color_boton, width=20, fg="white", relief="raised")
    btn_agregar.pack(pady=10)

    btn_editar = tk.Button(ventana_Principal, text="Editar Contraseña", command=abrir_editar_contrasena,
                           font=fuente_boton,
                           bg=color_boton, width=20, fg="white", relief="raised")
    btn_editar.pack(pady=10)

    btn_eliminar = tk.Button(ventana_Principal, text="Eliminar Contraseña", command=abrir_eliminar_contrasena,
                             font=fuente_boton,
                             bg=color_boton, width=20, fg="white", relief="raised")
    btn_eliminar.pack(pady=10)

    btn_ver_contrasenas = tk.Button(ventana_Principal, text="Ver Contraseñas", command=ver_contrasenas,
                                    font=fuente_boton,
                                    bg=color_boton, width=20, fg="white", relief="raised")
    btn_ver_contrasenas.pack(pady=10)

    btn_backup = tk.Button(ventana_Principal, text="Realizar Backup", command=backup_contrasenas, font=fuente_boton,
                           bg=color_boton, width=20, fg="white", relief="raised")
    btn_backup.pack(pady=10)

    btn_restaurar = tk.Button(ventana_Principal, text="Restaurar desde Backup", command=restaurar_contrasenas,
                              font=fuente_boton,
                              bg=color_boton, width=20, fg="white", relief="raised")
    btn_restaurar.pack(pady=10)

    def salir():
        ventana_Principal.quit()

    btn_salir = tk.Button(ventana_Principal, text="Salir", command=salir, font=("Arial", 12, "bold"), bg="#b83810",
                          width=20,
                          fg="white", relief="raised")
    btn_salir.pack(pady=20)

    ventana_Principal.mainloop()


def abrir_agregar_contrasena():
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Contraseña")
    ventana_agregar.geometry("400x500")
    ventana_agregar.configure(bg="#2f2f2f")

    lbl_username = tk.Label(ventana_agregar, text="Nombre de Usuario:", font=("Helvetica", 12), bg="#3a3a3a",
                            fg="white")
    lbl_username.pack(pady=8)
    entry_username = tk.Entry(ventana_agregar, font=("Helvetica", 12), bd=2)
    entry_username.pack(pady=8, padx=20, fill=tk.X)

    lbl_red = tk.Label(ventana_agregar, text="Red (Servicio/App):", font=("Helvetica", 12), bg="#3a3a3a", fg="white")
    lbl_red.pack(pady=8)
    entry_red = tk.Entry(ventana_agregar, font=("Helvetica", 12), bd=2)
    entry_red.pack(pady=8, padx=20, fill=tk.X)

    lbl_contrasena = tk.Label(ventana_agregar, text="Nueva Contraseña:", font=("Helvetica", 12), bg="#3a3a3a",
                              fg="white")
    lbl_contrasena.pack(pady=8)
    entry_contrasena = tk.Entry(ventana_agregar, font=("Helvetica", 12), bd=2, show="*")
    entry_contrasena.pack(pady=8, padx=20, fill=tk.X)

    lbl_confirmar = tk.Label(ventana_agregar, text="Confirmar Contraseña:", font=("Helvetica", 12), bg="#3a3a3a",
                             fg="white")
    lbl_confirmar.pack(pady=8)
    entry_confirmar = tk.Entry(ventana_agregar, font=("Helvetica", 12), bd=2, show="*")
    entry_confirmar.pack(pady=8, padx=20, fill=tk.X)

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

    btn_guardar = tk.Button(ventana_agregar, text="Guardar", command=guardar_contrasena, font=("Helvetica", 14),
                            bg="#241f7f", fg="white", width=20, relief="raised")
    btn_guardar.pack(pady=20)
    btn_cerrar = tk.Button(ventana_agregar, text="Cerrar", command=ventana_agregar.destroy, font=("Helvetica", 14),
                           bg="#b83810", fg="white", width=20, relief="raised")
    btn_cerrar.pack(pady=10)


def abrir_editar_contrasena():
    ventana_editar = tk.Toplevel(root)
    ventana_editar.title("Editar Contraseña")
    ventana_editar.geometry("400x500")
    ventana_editar.configure(bg="#2f2f2f")

    lbl_usuario = tk.Label(ventana_editar, text="Selecciona el Usuario:", font=("Helvetica", 12), bg="#3a3a3a",
                           fg="white")
    lbl_usuario.pack(pady=8)
    usuarios = [(usuario, red) for usuario, red in gestor.contrasenas.keys()]
    if not usuarios:
        messagebox.showwarning("Advertencia", "No hay usuarios registrados.")
        ventana_editar.destroy()
        return
    combo_usuarios = tk.StringVar(ventana_editar)
    combo_usuarios.set(f"{usuarios[0][0]} - {usuarios[0][1]}")
    menu_usuarios = tk.OptionMenu(ventana_editar, combo_usuarios, *[f"{u} - {r}" for u, r in usuarios])
    menu_usuarios.pack(pady=8)

    lbl_nueva_contrasena = tk.Label(ventana_editar, text="Nueva Contraseña:", font=("Helvetica", 12), bg="#3a3a3a",
                                    fg="white")
    lbl_nueva_contrasena.pack(pady=8)
    entry_nueva_contrasena = tk.Entry(ventana_editar, font=("Helvetica", 12), bd=2, show="*")
    entry_nueva_contrasena.pack(pady=8, padx=20, fill=tk.X)

    lbl_confirmar = tk.Label(ventana_editar, text="Confirmar Contraseña:", font=("Helvetica", 12), bg="#3a3a3a",
                             fg="white")
    lbl_confirmar.pack(pady=8)
    entry_confirmar = tk.Entry(ventana_editar, font=("Helvetica", 12), bd=2, show="*")
    entry_confirmar.pack(pady=8, padx=20, fill=tk.X)

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

    btn_guardar = tk.Button(ventana_editar, text="Guardar Cambios", command=guardar_cambios, font=("Helvetica", 14),
                            bg="#241f7f", fg="white", width=20, relief="raised")
    btn_guardar.pack(pady=20)
    btn_cerrar = tk.Button(ventana_editar, text="Cerrar", command=ventana_editar.destroy, font=("Helvetica", 14),
                           bg="#b83810", fg="white", width=20, relief="raised")
    btn_cerrar.pack(pady=10)


def abrir_eliminar_contrasena():
    ventana_eliminar = tk.Toplevel(root)
    ventana_eliminar.title("Eliminar Contraseña")
    ventana_eliminar.geometry("400x400")
    ventana_eliminar.configure(bg="#2f2f2f")

    lbl_usuario = tk.Label(ventana_eliminar, text="Selecciona el Usuario:", font=("Helvetica", 12), bg="#3a3a3a",
                           fg="white")
    lbl_usuario.pack(pady=8)
    usuarios = [(usuario, red) for usuario, red in gestor.contrasenas.keys()]
    if not usuarios:
        messagebox.showwarning("Advertencia", "No hay usuarios registrados.")
        ventana_eliminar.destroy()
        return
    combo_usuarios = tk.StringVar(ventana_eliminar)
    combo_usuarios.set(f"{usuarios[0][0]} - {usuarios[0][1]}")
    menu_usuarios = tk.OptionMenu(ventana_eliminar, combo_usuarios, *[f"{u} - {r}" for u, r in usuarios])
    menu_usuarios.pack(pady=8)

    def eliminar():
        seleccion = combo_usuarios.get()
        username, red = seleccion.split(" - ")
        resultado = gestor.eliminar_contrasena(username, red)
        messagebox.showinfo("Resultado", resultado)
        ventana_eliminar.destroy()

    btn_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar, font=("Helvetica", 14),
                             bg="#241f7f", fg="white", width=20, relief="raised")
    btn_eliminar.pack(pady=20)

    btn_cerrar = tk.Button(ventana_eliminar, text="Cerrar", command=ventana_eliminar.destroy, font=("Helvetica", 14),
                           bg="#b83810", fg="white", width=20, relief="raised")
    btn_cerrar.pack(pady=10)


def ver_contrasenas():
    ventana_ver = tk.Toplevel(root)
    ventana_ver.title("Ver Contraseñas")
    ventana_ver.geometry("400x500")
    ventana_ver.configure(bg="#2f2f2f")

    frame_scroll = tk.Frame(ventana_ver, bg="#2f2f2f")
    frame_scroll.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_scroll, bg="#2f2f2f")
    scrollbar = tk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#2f2f2f")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    for (usuario, red), contrasena in gestor.contrasenas.items():
        # Formato: Red, Usuario, Contraseña
        frame_contrasena = tk.Frame(scrollable_frame, relief=tk.GROOVE, bd=2, bg="#3a3a3a")
        frame_contrasena.pack(fill=tk.X, pady=8, padx=10)

        lbl_red = tk.Label(frame_contrasena, text=f"Red: {red}", font=("Helvetica", 12, "bold"), bg="#3a3a3a",
                           fg="white")
        lbl_red.pack(anchor="w", padx=10)

        lbl_usuario = tk.Label(frame_contrasena, text=f"Usuario: {usuario}", font=("Helvetica", 11), bg="#3a3a3a",
                               fg="white")
        lbl_usuario.pack(anchor="w", padx=10)

        lbl_contrasena = tk.Label(frame_contrasena, text=f"Contraseña: {'*' * len(contrasena.valor)}",
                                  font=("Helvetica", 11), bg="#3a3a3a", fg="white")
        lbl_contrasena.pack(anchor="w", padx=10)

        def mostrar_contrasena(lbl_contrasena=lbl_contrasena, contrasena=contrasena):
            if lbl_contrasena.cget("text").startswith("Contraseña: "):
                lbl_contrasena.config(text=f"Contraseña: {contrasena.valor}")
            else:
                lbl_contrasena.config(text=f"Contraseña: {'*' * len(contrasena.valor)}")

        btn_mostrar = tk.Button(frame_contrasena, text="VER 👁️", command=mostrar_contrasena, font=("Helvetica", 12),
                                bg="#241f7f", fg="white", relief="raised")
        btn_mostrar.pack(anchor="e", padx=10, pady=5)

    btn_cerrar = tk.Button(ventana_ver, text="Cerrar", command=ventana_ver.destroy, font=("Helvetica", 14),
                           bg="#b83810", fg="white", width=20, relief="raised")
    btn_cerrar.pack(pady=10)


def backup_contrasenas():
    try:
        contrasenas_data = {}
        for (usuario, red), contrasena in gestor.contrasenas.items():
            contrasenas_data[f"{usuario} - {red}"] = contrasena.valor

        with open("backup_contrasenas.json", "w") as archivo:
            json.dump(contrasenas_data, archivo, indent=4)

        messagebox.showinfo("Backup Exitoso", "El backup de contraseñas se ha realizado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo realizar el backup. Error: {str(e)}")


def restaurar_contrasenas():
    try:
        with open("backup_contrasenas.json", "r") as archivo:
            contrasenas_data = json.load(archivo)

        for usuario_red, contrasena in contrasenas_data.items():
            usuario, red = usuario_red.split(" - ")
            gestor.agregar_contrasena(usuario, red, Contrasena(contrasena))

        messagebox.showinfo("Restauración Exitosa", "Las contraseñas se han restaurado correctamente desde el backup.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo restaurar el backup. Error: {str(e)}")


root = tk.Tk()
root.withdraw()
mostrar_login()
root.mainloop()
