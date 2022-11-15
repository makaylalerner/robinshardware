from pathlib import Path
import sqlite3
import datetime


INSERT_ITEM = "INSERT INTO items(item_name, item_category, item_cost, item_quant_in_stock, manufacturer_id) VALUES (?,?,?,?,?);"
INSERT_MANU = "INSERT INTO manufacturers(manufacturer_name, manufacturer_address, delivery_day, delivery_person_name, delivery_phone_num) VALUES(?, ?, ?, ?, ?);"
SEARCH_BY_CAT = "SELECT * FROM items where item_category = ? ;"
SEARCH_BY_ITEM = "SELECT * FROM items where item_name LIKE ?;" #I'm not sure how to make wildcard chars work here??
REMOVE_ITEM = "DELETE FROM items WHERE item_id = ?;"
UPDATE_DELIVERY_PERSON = "UPDATE manufacturers SET delivery_person_name = ?, delivery_phone_num = ? WHERE manufacturer_id = ?;"
UPDATE_STOCK = "UPDATE items SET item_quant_in_stock = ? WHERE item_id = ?;"
SELECT_LAST_DELIVERY_PERSON = "SELECT delivery_person_name FROM manufacturers WHERE manufacturer_id = ?;"
SELECT_MAN_ID_FROM_ITEM = "SELECT manufacturer_id FROM items WHERE item_id = ?;"

# join the tables here and use aliases (because typing is taxing) to get delivery day
SELECT_SOLD_OUT = ''' SELECT i.item_name, i.item_quant_in_stock, i.manufacturer_id, 
                      m.delivery_day FROM items i LEFT JOIN manufacturers m ON
                      i.manufacturer_id = m.manufacturer_id WHERE i.item_quant_in_stock = 0;'''

#setup the database and return the connection
def setup_db(force_reset=False):
    # you can change force_rest to true if you need to wipe your data for reasons that are definitely legal
    # also because I put a bunch of junk in here and broke it
    dbpath = Path("hardware_store.db")
    if dbpath.exists() and force_reset:
        dbpath.unlink()
    conn = sqlite3.connect(dbpath)
    # open and read the fancy schema file
    with open("schema.sql") as schemaf:
        conn.executescript(schemaf.read())
        conn.commit()
    return conn

def add_item(conn, item_name, item_category, item_cost, quant_in_stock, man_id):
    with conn:
        conn.execute(INSERT_ITEM, [item_name, item_category,item_cost, quant_in_stock, man_id ])

def remove_item(conn, item_id):
    with conn:
        return conn.execute(REMOVE_ITEM, [item_id])

def items_by_cat(conn, cat):
    cursor = conn.cursor()
    cursor.execute(SEARCH_BY_CAT, [cat])
    return list(cursor.fetchall())

def items_by_name(conn, name):
    cursor = conn.cursor()
    name_wc = '%' + name + '%'
    cursor.execute(SEARCH_BY_ITEM, [name_wc])
    return list(cursor.fetchall())

def update_stock_quant(conn, item_quant_in_stock, item_id):
    with conn:
        return conn.execute(UPDATE_STOCK, [item_quant_in_stock, item_id])

def update_delivery_info(conn, manufacturer_id, delivery_person_name, delivery_phone_num):
    with conn:
        return conn.execute(UPDATE_DELIVERY_PERSON, [manufacturer_id, delivery_person_name, delivery_phone_num])

def get_man_id_from_item(conn, item_id):
    cursor = conn.cursor()
    cursor.execute(SELECT_MAN_ID_FROM_ITEM, [item_id])
    return cursor.fetchone()[0]

def get_sold_outs(conn):
    cursor = conn.cursor()
    cursor.execute(SELECT_SOLD_OUT)
    return list(cursor.fetchall())

def get_last_delivery_person(conn, man_id):
    cursor = conn.cursor()
    cursor.execute(SELECT_LAST_DELIVERY_PERSON, [man_id])
    return cursor.fetchone()[0]