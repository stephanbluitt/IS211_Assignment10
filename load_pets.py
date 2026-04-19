import sqlite3

# Connect to database
conn = sqlite3.connect('pets.db')
cur = conn.cursor()

# Insert Persons
persons = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

cur.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", persons)

# Insert Pets
pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

cur.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pets)

# Insert Relationships
person_pets = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

cur.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pets)

# Save and close
conn.commit()
conn.close()

print("Data loaded successfully.")
