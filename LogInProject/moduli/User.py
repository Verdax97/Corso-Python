import simplejson as json
import bcrypt as bc
import os
import getpass


class User:
    def __init__(self):
        self.username = ''
        self.email = ''
        self.__logged = False
        # eventuali altre informazioni da legare all'utente

    def register(self, username,email, password):
        # controllo se il file eseste e se non è vuoto
        if os.path.isfile("users.json") and os.stat("users.json").st_size != 0:
            # apro il file e carico gli utenti in users
            fp = open("users.json", "r+")
            users = json.load(fp)
        else:
            # creo il file e inizializzo il vettore fegli utenti
            fp = open("users.json", "w+")
            users = []

        # controllo che non esista già un utente con lo stesso username (non prioritario)
        for u in users:
            if u["username"] == username:
                print("Spiacenti, username già esistente.")
                # devo ricordarmi di chiudere il file
                fp.close()
                return

        # faccio un hashing della password
        password = bc.hashpw(password.encode(), bc.gensalt())
        # creo il dizionario dell'utente che verrà tradotto in oggetto js dalla libreria json
        data = {"username": username, "email": email, "password": password}

        # print(data)
        users.append(data)
        # print(users)

        # sposto il puntatore all'inizio del file.
        # questo è necessario in quanto vogliamo riscrivere il file ogni volta
        fp.seek(0)
        # salvo i dati in json
        json.dump(users, fp)
        # chiudo il file
        fp.close()

    def login(self, username, password):
        # controllo che il file esista e che non sia vuoto
        if os.path.isfile("users.json") and os.stat("users.json").st_size != 0:
            # apro il file e carico gli utenti in users
            fp = open("users.json", "r+")
            users = json.load(fp)
            # posso chiudere subito il file in quanto ho caricato le informazioni in users e non devo scrivere
            fp.close()
        else:
            # non posso loggare se non esistono utenti salvati
            print("Devi registrare almeno un account prima di poter effettuare il Login.")
            return

        # inizializzo user a None (equivalente di null in python)
        user = None
        for u in users:
            # cerco l'utente con l'username inserito
            if u["username"] == username:
                # se lo trovo copio dizionario in user
                user = u
                break

        # se ho trovato l'utente (altrimenti è ancora a None e la condizione non è verificata
        if user:
            # controllo la password
            if bc.checkpw(password.encode(), user["password"].encode()):
                # se è corretta copio username e email nei campi dell'istanza corrente
                self.username = user["username"]
                self.email = user["email"]
                print("User logged in as: ", self.username)
                # associo altri eventuali informazioni dell'utente
                self.__logged = True
            else:
                # se è sbagliata stampo un errore
                print("Password errata")
        else:
            # se non ho trovato l'utente, stampo un errore
            print("Username non trovato")

    def logout(self):
        # setto logged a falso e elimino username e email vecchie
        self.__logged = False
        self.username = ''
        self.email = ''

    def is_logged(self):
        # __logged è un "private instance variable", per leggerla fuori da questo file ho bisogno di una funzione
        return self.__logged

    def print_profile(self):
        # Se sono loggato stampo le informazioni del profilo
        if self.__logged:
            print("Username:", self.username)
            print("Email:", self.email)
        else:
            print("You need to be logged in!")

    def change_password(self, old_password):
        if self.__logged:
            # apro il file di salvataggio e carico gli utenti
            if os.path.isfile("users.json") and os.stat("users.json").st_size != 0:
                fp = open("users.json", "r+")
                users = json.load(fp)
            else:
                # se sono arrivato a questa funzione il file di salvataggio deve esistere!
                print("Unexpected error.")
                return

            # cerco l'utente
            user = None
            for u in users:
                if u["username"] == self.username:
                    user = u
                    break
            # controllo la password vecchia
            if bc.checkpw(old_password.encode(), user["password"].encode()):
                # se la password vecchia è giusta chiedo nuova password e ne faccio un hashing
                password = bc.hashpw(getpass.getpass("Inserisci nuova password: ").encode(), bc.gensalt())
            else:
                print("Vecchia password errata!")
                # devo ricordarmi di chiudere il file
                fp.close()
                return

            # cerco l'utente per cambiare il suo campo password
            for u in users:
                if u["username"] == self.username:
                    u["password"] = password
                    break

            # salvo la lista degli utenti aggiornata e chiudo il file
            fp.seek(0)
            json.dump(users, fp)
            fp.close()

            print("Password cambiata con successo.")
        else:
            print("Devi essere loggato per cambiare password!")
