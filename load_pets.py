import sqlite3

def load_data():
    # Connects to pets.db (creates it if it doesn't exist)
    con = sqlite3.connect('pets.db')
    cur = con.cursor()

    # Create the tables based on the assignment schema
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        );
        CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT,
            age INTEGER,
            dead INTEGER
        );
        CREATE TABLE IF NOT EXISTS person_pet (
            person_id INTEGER,
            pet_id INTEGER
        );
    """)

    # Clear existing data to prevent duplicate rows if run multiple times
    cur.execute("DELETE FROM person")
    cur.execute("DELETE FROM pet")
    cur.execute("DELETE FROM person_pet")

    # Define the data tuples
    persons = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]

    pets = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]

    person_pets = [
        (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)
    ]

    # Insert data into the tables using executemany for efficiency
    cur.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", persons)
    cur.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pets)
    cur.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pets)

    # Commit changes and close connection
    con.commit()
    con.close()
    print("Database populated successfully.")

if __name__ == '__main__':
    load_data()
