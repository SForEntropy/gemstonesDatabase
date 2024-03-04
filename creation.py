import sqlite3


conn = sqlite3.connect('Gemstones.db')


cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS stonesTable (
        name TEXT,
        primaryColour TEXT,
        placeMined TEXT,
        mohs INTEGER
    )
''')


conn.commit()
conn.close()

print("Database 'Gemstones' and table 'stonesTable' created successfully.")