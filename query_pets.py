import sqlite3

conn = sqlite3.connect('pets.db')
cur = conn.cursor()

while True:
    person_id = input("Enter a person ID (-1 to exit): ")

    if person_id == '-1':
        break

    # Get person
    cur.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cur.fetchone()

    if person:
        first, last, age = person
        print(f"{first} {last}, {age} years old")

        # Get pets
        cur.execute("""
            SELECT pet.name, pet.breed, pet.age
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        """, (person_id,))

        pets = cur.fetchall()

        for pet in pets:
            name, breed, age = pet
            print(f"  Owns {name}, a {breed}, that is {age} years old")

    else:
        print("Person not found.")

conn.close()
