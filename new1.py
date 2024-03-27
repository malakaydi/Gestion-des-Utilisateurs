import tkinter as tk
from tkinter import messagebox
import subprocess

def verifier_utilisateur_existant(username):
    try:
        subprocess.check_output(["id", username])
        return True
    except subprocess.CalledProcessError:
        return False
        
        
def creer_utilisateur():
    def creer():
        username = username_entry.get()

        if username == "":
            messagebox.showerror("Erreur", "Le nom d'utilisateur ne peut pas être vide.")
            return

        if verifier_utilisateur_existant(username):
            messagebox.showerror("Erreur", f"L'utilisateur '{username}' existe déjà.")
            return

        fullname = fullname_entry.get()
        if fullname == "":
            messagebox.showerror("Erreur", "Le nom complet ne peut pas être vide.")
            return

        password = password_entry.get()
        password_confirm = password_confirm_entry.get()

        if password != password_confirm:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas. Veuillez réessayer.")
            return

        if len(password) < 8:
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins 8 caractères.")
            return

        phone_number = phone_entry.get()
        if not phone_number.isdigit() or len(phone_number) != 8:
            messagebox.showerror("Erreur", "Le numéro de téléphone doit contenir exactement 8 chiffres.")
            return

        address = address_entry.get()
        if not address.isalpha():
            messagebox.showerror("Erreur", "L'adresse doit contenir uniquement des lettres.")
            return

        try:
            subprocess.check_output(["sudo", "useradd", "-m", "-c", f"{fullname}, {phone_number}, {address}", username, "-f", "0"])
            subprocess.check_output(["sudo", "chpasswd"], input=f"{username}:{password}", universal_newlines=True)
            messagebox.showinfo("Succès", f"L'utilisateur '{username}' a été créé avec succès.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Erreur", f"Impossible de créer l'utilisateur '{username}'.")

    create_window = tk.Toplevel()
    create_window.title("Création d'utilisateur")

    username_label = tk.Label(create_window, text="Nom d'utilisateur :")
    username_label.pack()
    username_entry = tk.Entry(create_window)
    username_entry.pack()

    fullname_label = tk.Label(create_window, text="Nom complet :")
    fullname_label.pack()
    fullname_entry = tk.Entry(create_window)
    fullname_entry.pack()
    
    phone_label = tk.Label(create_window, text="Numéro de téléphone (8 chiffres) :")
    phone_label.pack()
    phone_entry = tk.Entry(create_window)
    phone_entry.pack()

    address_label = tk.Label(create_window, text="Adresse :")
    address_label.pack()
    address_entry = tk.Entry(create_window)
    address_entry.pack()

    password_label = tk.Label(create_window, text="Mot de passe (8 caractères minimum) :")
    password_label.pack()
    password_entry = tk.Entry(create_window, show="*")
    password_entry.pack()

    password_confirm_label = tk.Label(create_window, text="Confirmez le mot de passe :")
    password_confirm_label.pack()
    password_confirm_entry = tk.Entry(create_window, show="*")
    password_confirm_entry.pack()

    

    create_button = tk.Button(create_window, text="Créer utilisateur", command=creer)
    create_button.pack()


def modifier_nom_dutilisateur():
    def modifier_info():
        username = username_modify_entry.get()

        if username == "":
            messagebox.showerror("Erreur", "Le nom d'utilisateur à modifier ne peut pas être vide.")
            return

        if not verifier_utilisateur_existant(username):
            messagebox.showerror("Erreur", f"L'utilisateur '{username}' n'existe pas.")
            return

        new_username = new_username_entry.get()

        if new_username == "":
            messagebox.showerror("Erreur", "Le nouveau nom d'utilisateur ne peut pas être vide.")
            return

        try:
            subprocess.check_output(["sudo", "usermod", "-l", new_username, username])
            messagebox.showinfo("Succès", f"L'utilisateur '{username}' a été renommé en '{new_username}' avec succès.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Erreur", f"Impossible de renommer l'utilisateur '{username}' en '{new_username}'.")

    modify_window = tk.Toplevel()
    modify_window.title("Modification d'utilisateur")

    username_modify_label = tk.Label(modify_window, text="Nom d'utilisateur à modifier :")
    username_modify_label.pack()
    username_modify_entry = tk.Entry(modify_window)
    username_modify_entry.pack()

    new_username_label = tk.Label(modify_window, text="Nouveau nom d'utilisateur :")
    new_username_label.pack()
    new_username_entry = tk.Entry(modify_window)
    new_username_entry.pack()

    modify_button = tk.Button(modify_window, text="Modifier utilisateur", command=modifier_info)
    modify_button.pack()

def modifier_info_dutilisateur():
    def modifier_nom():
        username = username_modify_entry.get()

        if username == "":
            messagebox.showerror("Erreur", "Le nom d'utilisateur à modifier ne peut pas être vide.")
            return

        if not verifier_utilisateur_existant(username):
            messagebox.showerror("Erreur", f"L'utilisateur '{username}' n'existe pas.")
            return

        new_phone_number = phone_entry.get()
        new_address = address_entry.get()

        if new_phone_number == "" and new_address == "":
            messagebox.showerror("Erreur", "Vous devez entrer au moins une nouvelle information (numéro de téléphone ou adresse).")
            return

        try:
            if new_phone_number:
                subprocess.check_output(["sudo", "usermod", "-c", f"{new_phone_number}", username])
            if new_address:
                subprocess.check_output(["sudo", "usermod", "-c", f"{new_address}", username])
            messagebox.showinfo("Succès", f"Les informations de l'utilisateur '{username}' ont été modifiées avec succès.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Erreur", f"Impossible de modifier les informations de l'utilisateur '{username}'.")

    modify_window = tk.Toplevel()
    modify_window.title("Modification d'informations d'utilisateur")

    username_modify_label = tk.Label(modify_window, text="Nom d'utilisateur à modifier :")
    username_modify_label.pack()
    username_modify_entry = tk.Entry(modify_window)
    username_modify_entry.pack()

    phone_label = tk.Label(modify_window, text="Nouveau numéro de téléphone (8 chiffres) :")
    phone_label.pack()
    phone_entry = tk.Entry(modify_window)
    phone_entry.pack()

    address_label = tk.Label(modify_window, text="Nouvelle adresse :")
    address_label.pack()
    address_entry = tk.Entry(modify_window)
    address_entry.pack()

    modify_button = tk.Button(modify_window, text="Modifier informations", command=modifier_nom)
    modify_button.pack()



def supprimer_utilisateur():
    def supprimer():
        username = username_delete_entry.get()

        if username == "":
            messagebox.showerror("Erreur", "Le nom d'utilisateur ne peut pas être vide.")
            return

        if not verifier_utilisateur_existant(username):
            messagebox.showerror("Erreur", f"L'utilisateur '{username}' n'existe pas.")
            return

        try:
            subprocess.check_output(["sudo", "userdel", "-r", username])
            messagebox.showinfo("Succès", f"L'utilisateur '{username}' a été supprimé avec succès.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Erreur", f"Impossible de supprimer l'utilisateur '{username}'.")

    delete_window = tk.Toplevel()
    delete_window.title("Suppression d'utilisateur")

    username_delete_label = tk.Label(delete_window, text="Nom d'utilisateur :")
    username_delete_label.pack()
    username_delete_entry = tk.Entry(delete_window)
    username_delete_entry.pack()

    delete_button = tk.Button(delete_window, text="Supprimer utilisateur", command=supprimer)
    delete_button.pack()

def afficher_liste_utilisateurs():
    users_window = tk.Toplevel()
    users_window.title("Liste des utilisateurs")

    users_label = tk.Label(users_window, text="Liste des utilisateurs :")
    users_label.pack()

    users_text = tk.Text(users_window)
    users_text.pack()

    try:
        output = subprocess.check_output(["awk", "-F:", "{print $1}", "/etc/passwd"], universal_newlines=True)
        users_text.insert(tk.END, output)
    except subprocess.CalledProcessError:
        users_text.insert(tk.END, "Erreur lors de la récupération de la liste des utilisateurs.")

    users_text.configure(state="disabled")
    

def surveillance_utilisation_serveur():
    def surveiller():
        date_debut = date_debut_entry.get()
        date_fin = date_fin_entry.get()

        try:
            subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'find / -type f -newermt "{date_debut}" ! -newermt "{date_fin}" -exec stat -c "%U" {{}} + 2>/dev/null; read -p "Appuyez sur Entrée pour continuer..."'])

        except subprocess.CalledProcessError:
            messagebox.showerror("Erreur", "Erreur lors de la surveillance de l'utilisation du serveur.")

    # Fenêtre et widgets pour la surveillance de l'utilisation du serveur
    surveillance_window = tk.Toplevel()
    surveillance_window.title("Surveillance utilisation serveur")

    date_debut_label = tk.Label(surveillance_window, text="Date de début (format : AAAA-MM-JJ HH:MM:SS) :")
    date_debut_label.pack()
    date_debut_entry = tk.Entry(surveillance_window)
    date_debut_entry.pack()

    date_fin_label = tk.Label(surveillance_window, text="Date de fin (format : AAAA-MM-JJ HH:MM:SS) :")
    date_fin_label.pack()
    date_fin_entry = tk.Entry(surveillance_window)
    date_fin_entry.pack()

    surveiller_button = tk.Button(surveillance_window, text="Surveiller", command=surveiller)
    surveiller_button.pack()
    
    
def reinitialiser_mot_de_passe():
    def reset_password():
        username = username_entry.get()

        if username == "":
            messagebox.showerror("Erreur", "Le nom d'utilisateur ne peut pas être vide.")
            return

        if not verifier_utilisateur_existant(username):
            messagebox.showerror("Erreur", f"L'utilisateur '{username}' n'existe pas.")
            return

        new_password = password_entry.get()
        password_confirm = password_confirm_entry.get()

        if new_password != password_confirm:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas. Veuillez réessayer.")
            return

        if len(new_password) < 8:
            messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins 8 caractères.")
            return

        try:
            subprocess.check_output(["sudo", "chpasswd"], input=f"{username}:{new_password}", universal_newlines=True)
            messagebox.showinfo("Succès", f"Le mot de passe de l'utilisateur '{username}' a été réinitialisé avec succès.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Erreur", f"Impossible de réinitialiser le mot de passe de l'utilisateur '{username}'.")

    reset_window = tk.Toplevel()
    reset_window.title("Réinitialisation du mot de passe")

    username_label = tk.Label(reset_window, text="Nom d'utilisateur :")
    username_label.pack()
    username_entry = tk.Entry(reset_window)
    username_entry.pack()

    password_label = tk.Label(reset_window, text="Nouveau mot de passe (8 caractères minimum) :")
    password_label.pack()
    password_entry = tk.Entry(reset_window, show="*")
    password_entry.pack()

    password_confirm_label = tk.Label(reset_window, text="Confirmez le nouveau mot de passe :")
    password_confirm_label.pack()
    password_confirm_entry = tk.Entry(reset_window, show="*")
    password_confirm_entry.pack()

    reset_button = tk.Button(reset_window, text="Réinitialiser le mot de passe", command=reset_password)
    reset_button.pack()
    

def afficher_informations_utilisateur():
    def show_user_info():
        username = username_entry.get()

        if username == "":
            messagebox.showerror("Erreur", "Le nom d'utilisateur ne peut pas être vide.")
            return

        if not verifier_utilisateur_existant(username):
            messagebox.showerror("Erreur", f"L'utilisateur '{username}' n'existe pas.")
            return

        try:
            user_info = subprocess.check_output(["getent", "passwd", username]).decode("utf-8")
            info_text.delete( tk.END)
            info_text.insert(tk.END, user_info)
        except subprocess.CalledProcessError:
            messagebox.showerror("Erreur", "Impossible de récupérer les informations de l'utilisateur.")

    info_window = tk.Toplevel()
    info_window.title("Informations Utilisateur")

    username_label = tk.Label(info_window, text="Nom d'utilisateur :")
    username_label.pack()
    username_entry = tk.Entry(info_window)
    username_entry.pack()


    show_button = tk.Button(info_window, text="Afficher informations", command=show_user_info)
    show_button.pack()

    info_text = tk.Text(info_window)
    info_text.pack()




def afficher_menu_principal():
    main_window = tk.Tk()
    main_window.title("Menu principal")
    
    title_label = tk.Label(main_window, text="============================== Bienvenue au systeme de gestion d'utilisateur ============================")
    title_label.pack()

    menu_button = tk.Button(main_window, text="Menu principal", command=afficher_menu_contextuel)
    menu_button.pack()
    
    quit_button = tk.Button(main_window, text="Quitter", command=lambda: quitter_programme(main_window))
    quit_button.pack()

    main_window.mainloop()


def afficher_menu_contextuel():
    context_window = tk.Toplevel()
    context_window.title("Menu des fonctionnalités :)")
    
    title_label = tk.Label(context_window, text="==================== Gestion des utilisateurs ============================")
    title_label.pack()

    create_button = tk.Button(context_window, text="Créer utilisateur", command=creer_utilisateur)
    create_button.pack()

    modify_button = tk.Button(context_window, text="Modifier le nom d'utilisateur", command=modifier_nom_dutilisateur)
    modify_button.pack()
    
    
    modify_button = tk.Button(context_window, text="Modifier les infos d'utilisateur", command=modifier_info_dutilisateur)
    modify_button.pack()
    
    reset_button = tk.Button(context_window, text="Réinitialiser le mot de passe", command=reinitialiser_mot_de_passe)
    reset_button.pack()
    
    info_button = tk.Button(context_window, text="Afficher informations utilisateur", command=afficher_informations_utilisateur)
    info_button.pack()
    
    list_button = tk.Button(context_window, text="Liste des utilisateurs", command=afficher_liste_utilisateurs)
    list_button.pack()
    
    delete_button = tk.Button(context_window, text="Supprimer utilisateur", command=supprimer_utilisateur)
    delete_button.pack()
    
    surveillance_button = tk.Button(context_window, text="Surveillance utilisation serveur", command=surveillance_utilisation_serveur)
    surveillance_button.pack()


    quit_button = tk.Button(context_window, text="Quitter", command=context_window.destroy)
    quit_button.pack()    
    

def quitter_programme(window):
    messagebox.showinfo("Information", "Programme terminé. A trés bientôt!")
    window.after(10, window.destroy) 


afficher_menu_principal()
