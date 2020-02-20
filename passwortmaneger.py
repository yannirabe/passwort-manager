import psycopg2
import datetime

connect = psycopg2.connect(
    user='postgres',
    password='Yannikrabe1',
    host='192.168.178.28',
    database='passwd')
c = connect.cursor()

secret = psycopg2.connect(
    user='postgres',
    password='Yannikrabe1',
    host='192.168.178.28',
    database='secret')
cs = secret.cursor()


def loggin():
    passwd = input('Passwort>>> ')
    cs.execute(f"SELECT passwort FROM secret WHERE passwort='{passwd}'")
    pwd_l = cs.fetchall()
    passwd_check = ''.join(c for c in str(pwd_l) if c not in "'[(,)]'")
    if not passwd == passwd_check:
        print('Passwort ist falsch')
        loggin()
    else:
        pass


def create():
    url = input('URL>>> ')
    user_name = input('User_Name>>> ')
    email = input('E-Mail>>> ')
    passwd = input('Passwort>>> ')
    kategorie = input('Kategorie>>> ')

    c.execute('INSERT INTO passwd(url, user_name, email, passwd, kategorie, datum) VALUES (%s, %s, %s, %s, %s, %s);',
              (url, user_name, email, passwd, kategorie, datetime.datetime.now().strftime('%d.%m.%y')))
    connect.commit()


def deleat():
    user_name = input('User_Name>>> ')
    passwd = input('Passwort>>> ')
    kategorie = input('Kategorie>>> ')

    c.execute(f"DELETE FROM passwd WHERE user_name='{user_name}' AND passwd='{passwd}' AND kategorie='{kategorie}'")
    connect.commit()


def edit():
    user_name = input('User_Name>>> ')
    passwd = input('Passwort>>> ')
    kategorie = input('Kategorie>>> ')

    new_url = input('URL>>> ')
    new_user_name = input('User_Name>>> ')
    new_email = input('E-Mail>>> ')
    new_passwd = input('Passwort>>> ')
    new_kategorie = input('Kategorie>>> ')

    c.execute(f"UPDATE passwd SET"
              f" url='{new_url}', user_name='{new_user_name}', email='{new_email}', passwd='{new_passwd}', kategorie='{new_kategorie}'"
              f"WHERE user_name='{user_name}' AND passwd='{passwd}' AND kategorie='{kategorie}'")
    connect.commit()


def show_all():
    c.execute('SELECT * FROM passwd')
    all = c.fetchall()
    for show in all:
        print(f"{show[0]} | {show[1]} | {show[2]} | {show[3]} | {show[4]} | {show[5]}")


def search():
    kategorie = input('Kategorie>>> ')
    print('Alle Einträge aus einer Kategorie:\n')
    c.execute(f"SELECT * FROM passwd WHERE kategorie='{kategorie}'")
    all = c.fetchall()
    for show in all:
        print(f"{show[0]} | {show[1]} | {show[2]} | {show[3]} | {show[4]} | {show[5]}")


def masterpasswd():
    now = input('Aktuelles Passwort>>> ')
    cs.execute(f"SELECT passwort FROM secret WHERE passwort='{now}'")
    pwd_l = cs.fetchall()
    passwd_check = ''.join(c for c in str(pwd_l) if c not in "'[(,)]'")
    if not now == passwd_check:
        print('Passwort ist falsch')
        masterpasswd()
    else:
        after = input('Neues Passwort>>> ')
        repeat = input('Passwort wiederholen>>> ')
        if after == repeat:
            cs.execute(f"UPDATE secret SET passwort='{after}'")
            secret.commit()
        else:
            print('Passwörter sind nicht gleich')


def help():
    print('\ncreate: Erstellt einen Eintrag.\n\n'
          'deleat: löscht einen Eintrag.\n\n'
          'edit: Bearbeitet einen Eintag\n\n'
          'show_all: Zeigt alle Einträge.\n\n'
          'search: Zeigt alle Einträge in einer Kategorie.\n\n'
          'passwd: Ändert das Masterpasswort.\n\n'
          'help: Zeigt dieses Menü\n')


loggin()

while True:
    mg = input('Command>>> ')
    if mg == 'create':
        create()
        print('Eintrag wurde erstellt')
    elif mg == 'deleat':
        deleat()
        print('Eintrag würde gelöscht')
    elif mg == 'edit':
        edit()
        print('\nEintrag wurde upgedated')
    elif mg == 'show_all':
        print('Alle Einträge:')
        show_all()
    elif mg == 'search':
        search()
    elif mg == 'passwd':
        masterpasswd()
    elif mg == 'help':
        help()
    elif mg == 'exit':
        break
    else:
        print('Commend not found')
