import sqlite3
import sys

def query_pets():
    # Connect to the database
    con = sqlite3.connect('pets.db')
    cur = con.cursor()

    while True:
        try:
            # Prompt the user for an ID
            person_id = int(input("\nEnter a person's ID number (-1 to exit): "))
        except ValueError:
            print("Please enter a valid integer ID.")
            continue

        if person_id == -1:
            print("Exiting program...")
            sys.exit()

        # Query the person table
        cur.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person = cur.fetchone()

        if person:
            first_name, last_name, age = person
            print(f"{first_name} {last_name}, {age} years old")

            # Query the person's pets using an INNER JOIN through the person_pet table
            cur.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead
                FROM pet
                JOIN person_pet ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = ?
            """, (person_id,))
            
            pets = cur.fetchall()
            
            # Iterate through the returned pets and format the output
            for pet in pets:
                name, breed, pet_age, dead = pet
                
                # Adjust grammar based on whether the pet is dead (1) or alive (0)
                owned_status = "owned" if dead == 1 else "owns"
                is_was = "was" if dead == 1 else "is"
                
                print(f"  {first_name} {last_name} {owned_status} {name}, a {breed}, that {is_was} {pet_age} years old.")
        else:
            print("Error: Person ID not found in the database.")

if __name__ == '__main__':
    query_pets()
