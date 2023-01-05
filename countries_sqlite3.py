import sqlite3, json

def create_table(c):
    c.execute("CREATE TABLE countries( id INTEGER NOT NULL, name VARCHAR UNIQUE, timezones VARCHAR, topLevelDomain VARCHAR, alpha2Code VARCHAR, alpha3Code VARCHAR, callingCodes VARCHAR, flag VARCHAR, population INTEGER, capital VARCHAR, nativeName VARCHAR, numericCode INTEGER, region VARCHAR, subregion VARCHAR, currencies VARCHAR, borders VARCHAR, gini INTEGER, user_id INTEGER, PRIMARY KEY (id), FOREIGN KEY (user_id) REFERENCES users (id))")
    c.execute("CREATE TABLE addresses( id INTEGER, street VARCHAR, number VARCHAR, zipcode VARCHAR, city VARCHAR, state VARCHAR, description VARCHAR, country_id INTEGER, PRIMARY KEY (id), FOREIGN KEY (country_id) REFERENCES countries (id))")
    c.execute("CREATE TABLE users( id INTEGER NOT NULL, email VARCHAR, username VARCHAR UNIQUE, firstname VARCHAR, middlename VARCHAR, lastname VARCHAR, picture VARCHAR, hashed_password VARCHAR, address_id INTEGER, country_id INTEGER, PRIMARY KEY (id), FOREIGN KEY (country_id) REFERENCES countries (id), FOREIGN KEY (address_id) REFERENCES addresses (id))")
    c.execute("CREATE UNIQUE INDEX ix_countries_name ON countries (name)")
    c.execute("CREATE UNIQUE INDEX ix_users_email ON users (email)")
    c.execute("CREATE UNIQUE INDEX ix_users_username ON users (username)")

conn=sqlite3.connect('countries.db')
c=conn.cursor()
create_table(c)
f = open('countries.json','r')
f = f.readlines()
countries = json.loads(f[0])
o = ""
keys = list(countries[0].keys())
k = f'({keys[0]},{keys[2]},{keys[3]},{keys[5]},{keys[7]})'
k = k.replace("'","")
for cou in countries:
    val=''
    values = list(cou.values())
    val = f'("{values[0]}","{values[2]}","{values[3]}","{values[5]}","{values[7]}")'
    sql_statement=f'INSERT INTO countries {k} VALUES {val};'
    c.execute(sql_statement)
c.execute('commit')
conn.close()
