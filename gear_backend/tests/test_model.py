import pytest
import sqlite3
import os
import json
from app.model import Gear, initialize_database, import_from_file, export_to_file, insert_gear


@pytest.fixture()
def db_file(tmp_path):
    # create your file manually here using the tmp_path fixture
    # or just import a static pre-built mock file
    # something like :
    database_file = os.path.join(tmp_path, 'gear.db')
    if os.path.exists(database_file):
        os.remove(database_file)
    with open(database_file, "w+") as f:
        pass
    yield database_file
    if os.path.exists(database_file):
        os.remove(database_file)

def test_initialize_database(db_file):

    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # Drop the gear table if it exists
    cursor.execute('DROP TABLE IF EXISTS gear')
    conn.commit()

    # Initialize the database
    initialize_database(db_file)

    # Check if the gear table was created
    cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="gear"')
    result = cursor.fetchone()
    assert result is not None


def test_import_from_file(db_file):
    initialize_database(db_file)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # Create a sample JSON file
    sample_data = [
        {
            "id": 1,
            "name": "Backpack",
            "producer": "North Face",
            "model": "Terra 55",
            "weight": 2.0,
            "isPacked": True,
            "category": "Backpack"
        },
        {
            "id": 2,
            "name": "Sleeping Bag",
            "producer": "Marmot",
            "model": "Spruce",
            "weight": 3.0,
            "isPacked": False,
            "category": "Sleeping Bag"
        }
    ]
    with open('sample_data.json', 'w') as f:
        json.dump(sample_data, f)

    # Import data from the sample JSON file
    import_from_file('sample_data.json', db_file)

    # Check if the data was imported correctly
    cursor.execute('SELECT * FROM gear')
    result = cursor.fetchall()
    assert len(result) == 2
    os.remove('sample_data.json')


def test_export_to_file(db_file):
    initialize_database(db_file)
    sample_data = [
        {
            "id": 1,
            "name": "Backpack",
            "producer": "North Face",
            "model": "Terra 55",
            "weight": 2.0,
            "isPacked": True,
            "category": "Backpack"
        },
        {
            "id": 2,
            "name": "Sleeping Bag",
            "producer": "Marmot",
            "model": "Spruce",
            "weight": 3.0,
            "isPacked": False,
            "category": "Sleeping Bag"
        }
    ]
    with open('sample_data.json', 'w') as f:
        json.dump(sample_data, f)

    # Import data from the sample JSON file
    import_from_file('sample_data.json', db_file)

    # Export the gear data to a JSON file
    export_to_file('gear_data.json', db_file)

    # Load the data from the exported file
    with open('gear_data.json') as f:
        exported_data = json.load(f)

    # Check if the data was exported correctly
    assert len(exported_data) == 2
    os.remove('gear_data.json')
    os.remove('sample_data.json')


def test_insert_gear(db_file):
    initialize_database(db_file)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # Insert a new gear item
    gear = Gear(id=3, name="Tent", producer="Big Agnes", 
                model="Copper Spur", weight=4.0, is_packed=True, category="Tent")
    insert_gear(gear, db_file)

    # Check if the gear item was inserted correctly
    cursor.execute('SELECT * FROM gear WHERE id=3')
    result = cursor.fetchone()
    assert result is not None

