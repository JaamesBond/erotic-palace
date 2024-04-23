import sqlite3
import os


def create_database():
    # Connect to or create the database
    conn = sqlite3.connect('girls.db')
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS girls (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 hair_colour TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 boobs TEXT,
                 ass TEXT,
                 race TEXT,
                 bmi REAL,
                 personality TEXT,
                 services TEXT
                 )''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS photos (
    id INTEGER PRIMARY KEY,
    girl_id INTEGER,
    photo_url TEXT,
    FOREIGN KEY (girl_id) REFERENCES girls(id)
);
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


def insert_data(name, age, hair_colour, phone, boobs=None, ass=None, race=None, bmi=None, personality=None, services=None):
    conn = sqlite3.connect('girls.db')
    c = conn.cursor()

    # Insert a new row into the table
    c.execute('''INSERT INTO girls (name, age, hair_colour, phone, boobs, ass, race, bmi, personality, services)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (name, age, hair_colour, phone, boobs, ass, race, bmi, personality, services))

    # Commit changes and close connection
    conn.commit()
    conn.close()


def clear_database():
    conn = sqlite3.connect('girls.db')
    c = conn.cursor()

    # Delete all rows from the table
    c.execute('''DELETE FROM girls''')

    # Commit changes and close connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # Create the database and table
    create_database()
    print("Database 'girls' and table 'girls' created successfully.")

    clear_database()
    print("Database cleared successfully.")

    # Example data with mandatory fields only
    mandatory_data = {
        "name": "Alice_Idk",
        "age": 25,
        "hair_colour": "Blonde",
        "phone": "+31696969690",
        "boobs": "medium",
        "ass": "big"
    }

    # Insert data into the database
    insert_data(**mandatory_data)
    print("Data inserted successfully.")
