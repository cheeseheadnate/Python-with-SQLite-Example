import sqlite3

connection = sqlite3.connect("gta.db")

cursor = connection.cursor()

cursor.execute("create table gta (rel_year integer, rel_name text, city text)")

release_list = [
    (1997, "Grand Theft Auto", "Liberty City, San Andreas, Vice City"),
    (1999, "Grand Theft Auto 2", "Anywhere City"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos"),
    (2025, "Grand Theft Auto VI", "Leonida (based on Florida)")
]

cursor.executemany("insert into gta values (?, ?, ?)", release_list)

connection.commit()

for game in release_list:
    print(f"{game[0]}: {game[1]} - Location: {game[2]}")


connection.close()
