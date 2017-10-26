import argparse
import os.path
import csv, sqlite3

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--file', dest='filename',
                    help='Please provide a csv')
parser.add_argument('-c', '--command', dest='command',
                    help='Command.')

args = parser.parse_args()


# DB Setup
LOCAL = 'my_db.sqlite'
MEMORY = ":memory:"

# DB Commands
CREATE = "CREATE TABLE {table} ({columns});"
INSERT = "INSERT INTO {table} ({columns}) VALUES (?, ?);"
DROP = "DROP TABLE IF EXISTS {table};"


def create(filename):
    table = os.path.splitext(filename)[0]
    csvfile = open(filename, 'rb')
    dict_reader = csv.DictReader(csvfile)
    columns = dict_reader.fieldnames

    con = sqlite3.connect(LOCAL)
    cur = con.cursor()

    # Drop
    command = DROP.format(table=table)
    cur.execute(command)

    # Create
    command = CREATE.format(table=table, columns=", ".join(columns))
    cur.execute(command)

    # Insert
    to_db = [row.values() for row in dict_reader]
    command = INSERT.format(table=table, columns=", ".join(columns))
    cur.executemany(command, to_db)
    con.commit()
    con.close()
    csvfile.close()


if __name__ == "__main__":
    filename = args.filename
    if args.command.lower() == "create":
        create(filename)
