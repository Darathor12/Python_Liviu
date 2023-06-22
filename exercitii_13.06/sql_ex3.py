"""
Write a SQL statement to create a table called countries, with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_id – foreign key
population – number

"""

import sqlite3


connection = sqlite3.connect('countries.db')
cursor = connection.cursor()
cursor.execute("""
DROP TABLE IF EXISTS countries; 
""")
cursor.execute("""
CREATE TABLE countries(
continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
country_code CHAR(2),
country_name VARCHAR(255),
population_milions FLOAT
);
""")

countries = [("Romania", "EU", 19), ("USA", "NA", 330), ("France", "EU", 70), ("Hungary", "EU",  9), ("Canada", "NA", 40), ("China", "AS", 1450), ("Belgium", "EU", 12), ("Egypt", "AF", 110), ("Australia", "OC", 25)]
sql_query = 'INSERT INTO countries(country_name, country_code, population_milions) VALUES(?,?,?)'
cursor.executemany(sql_query, countries)
connection.commit()