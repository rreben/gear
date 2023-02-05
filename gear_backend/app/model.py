# model.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license

'''Model module for the gear backend.
This program implements a simple database for storing gear information, using the SQLite database engine and the Python sqlite3 module. The database has a single table, "gear", which has the following columns:

id: an integer identifier for the gear item
name: a string representing the name of the gear item
producer: a string representing the producer of the gear item
model: a string representing the model of the gear item
weight: a float representing the weight of the gear item
isPacked: an integer representing whether the gear item is packed or not
category: a string representing the category of the gear item
The program consists of three functions:

initialize_database creates the "gear" table in the SQLite database if it doesn't already exist.
import_from_file imports gear data from a JSON file into the "gear" table in the SQLite database.
export_to_file exports the gear data from the "gear" table in the SQLite database to a JSON file.
You can call this function and pass in an instance of the Gear data class to insert a new gear item into the database.
'''
import sqlite3
import json
from dataclasses import dataclass

@dataclass
class Gear:
    id: int
    name: str
    producer: str
    model: str
    weight: float
    is_packed: bool
    category: str

def initialize_database(database_name='gear.db'):
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Create the gear table
    table_create_query = f'''
    CREATE TABLE IF NOT EXISTS gear (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        producer TEXT NOT NULL,
        model TEXT NOT NULL,
        weight REAL NOT NULL,
        is_packed INTEGER NOT NULL,
        category TEXT NOT NULL
    );
    '''
    cursor.execute(table_create_query)

    # Commit changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()

def import_from_file(filename, database_name='gear.db'):
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Load the data from the JSON file
    with open(filename) as f:
        gear_data = json.load(f)

    # Insert the data into the gear table
    for gear in gear_data:
        gear_insert_query = f'''
        INSERT INTO gear (id, name, producer, model, weight, is_packed, category)
        VALUES ({gear['id']}, '{gear['name']}', '{gear['producer']}', '{gear['model']}', {gear['weight']}, {1 if gear['isPacked'] else 0}, '{gear['category']}');
        '''
        cursor.execute(gear_insert_query)

    # Commit changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()

def export_to_file(filename, database_name='gear.db'):
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Retrieve all gear from the database
    gear_select_query = 'SELECT * FROM gear;'
    cursor.execute(gear_select_query)
    raw_gear = cursor.fetchall()

    # Write the gear data to the file
    gear = [Gear(*row).__dict__ for row in raw_gear]
    with open(filename, 'w') as f:
        json.dump(gear, f, indent=4)

    # Close the connection to the database
    conn.close()

from dataclasses import asdict

def insert_gear(gear, database_name='gear.db'):
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Convert the gear data class to a dictionary
    gear_data = asdict(gear)

    # Insert the gear data into the gear table
    gear_insert_query = f'''
    INSERT INTO gear (id, name, producer, model, weight, is_packed, category)
    VALUES ({gear_data['id']}, '{gear_data['name']}', '{gear_data['producer']}', '{gear_data['model']}', {gear_data['weight']}, {gear_data['is_packed']}, '{gear_data['category']}');
    '''
    cursor.execute(gear_insert_query)

    # Commit changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()

def update_item(item: Gear, database_name='gear.db'):
    '''Update an item in the database.
    Note that this implementation is using the asdict function from the dataclasses module to convert the Gear object to a dictionary, which makes it easier to access its attributes in the SQL query.'''
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Create the update query using the data from the Gear object
    gear_update_query = f'''
    UPDATE gear
    SET name='{item.name}', producer='{item.producer}', model='{item.model}', weight={item.weight}, isPacked={item.is_packed}, category='{item.category}'
    WHERE id={item.id};
    '''
    cursor.execute(gear_update_query)

    # Commit changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()


def delete_gear(id: int, database_name='gear.db'):
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Delete the gear item with the specified id
    delete_query = f"DELETE FROM gear WHERE id = {id};"
    cursor.execute(delete_query)

    # Commit changes to the database
    conn.commit()

    # Close the connection to the database
    conn.close()