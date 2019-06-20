import sqlite3

def alchemy_add_name(name,db):
        db.session.add(name)
        db.session.commit()
    return f"{name} added"

def alchemy_get_names(User): 
    return User.query.all()


def initdb():
    with sqlite3.connect('name.db') as db:
        c =  db.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS names(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);')
    return 

def add_name(name):
    with sqlite3.connect('name.db') as db:
        c =  db.cursor()
        c.execute(f'INSERT INTO names(name) values("{name}");')
        db.commit()
    return "Database appended"

def get_names():
    with sqlite3.connect('name.db') as db:
        c =  db.cursor()
        c.execute(f'SELECT name FROM names;')
        names = list(c.fetchall())
        return names


if __name__ == "__main__":
    initdb()





