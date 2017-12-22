from lib.paste_bin import PasteBinApi
import argparse
import re
import requests
import time
import sqlite3
import os
from colorama import init, Fore, Style

api_dev_key = ""                # Pastebin api_dev_key


init()

__author__ = Fore.CYAN+"Author:"+Style.RESET_ALL+"LukeBob"
__version__ = Fore.YELLOW+"Version:"+Style.RESET_ALL+"1.0"

prog = os.path.basename(__file__)

g = Fore.GREEN+"#"+Style.RESET_ALL
b = Fore.RED+"#"+Style.RESET_ALL

sb = (Fore.GREEN+"""
███████╗██╗███╗   ██╗      ██████╗ ██╗███╗   ██╗
██╔════╝██║████╗  ██║      ██╔══██╗██║████╗  ██║
███████╗██║██╔██╗ ██║█████╗██████╔╝██║██╔██╗ ██║
╚════██║██║██║╚██╗██║╚════╝██╔══██╗██║██║╚██╗██║
███████║██║██║ ╚████║      ██████╔╝██║██║ ╚████║
╚══════╝╚═╝╚═╝  ╚═══╝      ╚═════╝ ╚═╝╚═╝  ╚═══╝
"""+Style.RESET_ALL)

banner = (r"""
                ┈╭━━━━━━━━━━━╮┈
                ┈┃╭━━━╮┊╭━━━╮┃┈
                ╭┫┃┈{3}┈┃┊┃┈{3}┈┃┣╮
                ┃┃╰━━━╯┊╰━━━╯┃┃
                ╰┫╭━╮╰━━━╯╭━╮┣╯
                ┈┃┃┣┳┳┳┳┳┳┳┫┃┃┈
                ┈┃┃╰┻┻┻┻┻┻┻╯┃┃┈
                ┈╰━━━━━━━━━━━╯┈
{2}
({1})
({0})
""".format(__author__, __version__, sb, Fore.RED+"▇"+Style.RESET_ALL))
print(banner)

__example__ = ('''{0} --query --all                       List all Email:Password entries in database.
usage: {0} --query --email my@email.com        Query database for single email.
usage: {0} --stream --time 0.2                 Stream latest trending pastes.
usage: {0} --dump                              Scrape for Email:Password combinations, add them to database.
usage: {0} --drop                              Drop all entries from database.
usage: {0} --purge                             Drop all duplicate entries from databse.
usage: {0} --count                             Count all entries in database.
usage: {0} --backup                            Make a backup of database.
'''.format(prog))


parser = argparse.ArgumentParser(description="Pastebin tool", usage=__example__, epilog=Fore.GREEN+"MOTTO: "+Style.RESET_ALL+"WYO OR GTFO!")
parser.add_argument("-d", "--dump", action="store_true", help="Scrape pastebin for Email:password dumps.")
parser.add_argument("-s", "--stream", action="store_true", help="Stream trending pastebin content.")
parser.add_argument("-t", "--time", help="intervals to print data in seconds default: 0.3")
parser.add_argument("-q", "--query", action="store_true", help="Query database.")
parser.add_argument("-e", "--email", help="Email to look for entries")
parser.add_argument("-a", "--all", action="store_true", help="Dump(List) all entries stored in database")
parser.add_argument("-x", "--drop", action="store_true", help="Drop(Delete) all Email:Password entries.")
parser.add_argument("-p", "--purge", action="store_true", help="Drop(Delete) duplicate entries in database")
parser.add_argument("-c", "--count", action="store_true", help="Count entries in database")
parser.add_argument("-b", "--backup", action="store_true", help="Make a backup of database.")

args = parser.parse_args()


email_list = []


def db_connect():
    try:
        db     = sqlite3.connect('data/pastebin')
        cursor = db.cursor()
        return(db, cursor)
    except:
        print("\n[{0}] Error no data directory found, creating one now...".format(b))
        try:
            os.system("mkdir data")
            print("\n[{0}] Created data directory with database pastebin.".format(g))
            db     = sqlite3.connect('data/pastebin')
            cursor = db.cursor()
            return(db, cursor)
        except:
            raise

def return_time():
    time_now = time.strftime("%Y-%m-%d--%H-%M-%S", time.gmtime())
    return(time_now)

def backup_database():
    time_now = return_time()
    try:
        print("\n[{0}] Creating directory backup/{1}".format(g, time_now))
        if os.name != "nt":
            os.system("mkdir backup/{0}".format(time_now))
            time.sleep(1)
        else:
            os.system("mkdir backup\{0}".format(time_now))
            time.sleep(1)

        print("\n[{0}] Saving backup to backup/{1}/pastebin".format(g, time_now))
        time.sleep(1)
        if os.name != "nt":
            os.system("cp data/pastebin backup/{0}/pastebin".format(time_now))
        else:
            os.system("copy data\pastebin backup\{0}\pastebin".format(time_now))

        print("\n[{0}] Backup Sucessfull!".format(g))
    except:
        raise
        print("\n[{0}] Backup Unsucessfull!".format(b))

def count_entries():
    (db, cursor) = db_connect()
    cursor.execute('''SELECT * FROM victims''')
    all_rows = cursor.fetchall()
    if all_rows:
        print("[{0}] Found [{1}] entries in database.".format(g, str(len(all_rows))))
    else:
        print("[{0}] No entries in database!".format(b))


def purge_data():
    (db, cursor) = db_connect()
    cursor.execute('''SELECT * FROM victims WHERE rowid NOT IN (SELECT min(rowid) FROM victims GROUP BY name, password)''')
    vic = cursor.fetchall()
    if vic:
        print("\n[{0}] Found [{1}] duplicate entries in databse.".format(g, str(len(vic))))
        cursor.execute('''DELETE FROM victims WHERE rowid NOT IN (SELECT min(rowid) FROM victims GROUP BY name, password)''')
        db.commit()
        print("\n[{0}] Removed [{1}] duplicate entries from database".format(g, str(len(vic))))


    else:
        print("\n[{0}] No duplicate entires found in database!".format(b))

def drop_all():
    (db, cursor) = db_connect()
    cursor.execute('''DELETE FROM victims''')
    db.commit()
    print("\n[{0}] Deleted all entry's from database.".format(g))


def query_sqlite3():
    (db, cursor) = db_connect()

    if args.email:
        cursor.execute('''SELECT DISTINCT password FROM victims WHERE name=?''', (args.email,))
        vic = cursor.fetchall()
        if vic:
            for row in vic:
                print("\n[{3}] Email   : {0}\n[*] Password: {1}\n".format(args.email, row[0], g))
        else:
            print("\n[{0}] No Entries found for ({1})\n".format(b ,args.email))

    elif args.all:
        cursor.execute('''SELECT * FROM victims''')
        all_rows = cursor.fetchall()
        for row in all_rows:
            print("{0}:{1}".format(row[0], row[1]))
        print("\n[{0}] Dumped {1} Email:Password Combinations.\n".format(g, str(len(all_rows))))

    else:
        parser.print_help()

def dump_email(paste_key):
    (db, cursor) = db_connect()
    print("\n[{0}] Scraping pastebin for email:password dumps...\n".format(g))
    for key in paste_key:
        r = requests.get("https://pastebin.com/raw/{0}".format(key))
        data = r.text

        for line in data.split('\n'):
            if re.match("[\w.]+@[\w.]+", line):
                email_list.append(line)
    print("[{0}] Inserting [{1}] Username:Password combinations into Database...".format(g, str(len(email_list))))


    for email in email_list:
        try:
            username, password = email.split(":")
            try:
               cursor.execute('''INSERT INTO victims(name, password) VALUES(?,?)''', (username, password))
            except sqlite3.OperationalError:
               cursor.execute('''
                   CREATE TABLE victims(name TEXT, password TEXT)
               ''')
            db.commit()

        except ValueError:
            try:
                username, password = email.split("|")
                try:
                   cursor.execute('''INSERT INTO victims(name, password) VALUES(?,?)''', (username, password))
                except sqlite3.OperationalError:
                   cursor.execute('''
                       CREATE TABLE victims(name TEXT, password TEXT)
                   ''')
            except:
                pass

    print("\n[{0}] Succesfully Inserted [{1}] Email:Password combinations into Database.".format(g, str(len(email_list))))


def stream(paste_key, tyme=0.3):
        print("\n[{0}] Scraping pastebin...\n".format(g))
        for key in paste_key:
            print(key)
            r = requests.get("https://pastebin.com/raw/{0}".format(key))
            data = r.text
            for line in data.split('\n'):
                time.sleep(tyme)
                print(line)

def main():
    api = PasteBinApi(api_dev_key)
    trends = api.trends()
    paste_key  = re.findall("\<paste\_key\>(.{1,50})\<", trends)
    try:

        if args.backup:
            backup_database()

        elif args.count:
            count_entries()

        elif args.purge:
            purge_data()

        elif args.query:
            query_sqlite3()

        elif args.drop:
            sure = input("Delete All Entry's from database? [y,n]: ")

            if sure == 'y' or sure == 'Y':
                drop_all()

            else:
                print("\nexiting...")
                exit(0)

        elif args.dump:
            dump_email(paste_key)

        elif args.stream and args.time:
            stream(paste_key, tyme=(float(args.time)))

        elif args.stream and not args.time:
            stream(paste_key)

        else:
            parser.print_help()

    except KeyboardInterrupt:
        print("KeyboardInterrupt!")
        exit(0)

if __name__ == '__main__':
    main()

