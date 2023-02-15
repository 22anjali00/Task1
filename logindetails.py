def register():
    db = open("database.txt","r")
    username = input("create username:")
    password = input("create password:")
    password1 = input("confirm password:")

    if password != password1:
        print("password don't match, restart")
        register()
    else:
        if len(password) <= 6:
            print("password too short restart:")
            register()
        elif username in db:
            print("username exists")
            register()
        else:
            db = open("database.txt","a")
            db.write(username+", "+password+"\n")
            print("success!")

register()

def access():
    pass