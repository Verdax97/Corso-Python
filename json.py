import simplejson as json
user1 = {
    "username": "Luca",
    "email": "luca.collini@mail.polimi.it",
    "password": "password"
}

user2 = {
    "username": "Carlo",
    "email": "luca.collini@mail.polimi.it",
    "password": "password"
}

user3 = {
    "username": "Mario",
    "email": "luca.collini@mail.polimi.it",
    "password": "password"
}

# users = [user1, user2]

fp = open("utenti.json", "r+")

users = json.load(fp)

users.append(user3)
fp.seek(0)
json.dump(users, fp)
