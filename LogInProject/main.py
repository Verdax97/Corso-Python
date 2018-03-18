from moduli import User
import getpass

user = User.User()

run = True
while run:

    if user.is_logged():
        # Azioni che posso fare se sono loggato
        prompt = input("Scegli un azione: \n1) Logout\n2) Profilo\n3) Cambia Password\n4) Esci\n[1, 2, 3, 4]: ")
        if prompt == '1':
            user.logout()
        elif prompt == '2':
            user.print_profile()
        elif prompt == "3":
            user.change_password(getpass.getpass("Inserisci vecchia password: "))
        elif prompt == "4":
            exit()
        else:
            print("Input non valido")
    else:
        # Azioni che posso fare se non sono loggato
        prompt = input("Scegli un azione: \n1) Registrati\n2) Login\n3) Esci\n[1, 2, 3]: ")
        if prompt == "1":
            user.register(input("Scegli un username: "), input("Email: "), getpass.getpass("Digita Password: "))
        elif prompt == "2":
            user.login(input("Username: "), getpass.getpass("Password: "))
        elif prompt == "4":
            exit()
        else:
            print("Input non valido")
