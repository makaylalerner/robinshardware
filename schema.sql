CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_name TEXT,
    manufacturer_address TEXT,
    delivery_day TEXT,
    delivery_person_name TEXT,
    delivery_phone_num TEXT
);

CREATE TABLE IF NOT EXISTS items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    item_category TEXT,
    item_cost FLOAT,
    item_quant_in_stock INTEGER,
    manufacturer_id INTEGER,
    FOREIGN KEY(manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);




