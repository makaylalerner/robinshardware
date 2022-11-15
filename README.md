# robinshardware
ROBIN'S HARDWARE STORE INVENTORY DATABASE 

Documentation Prepared by Makayla Lerner 

For INSC 484: Database Applications 

On October 14, 2022 

DESCRIPTION: 
The local hardware store, Robin’s Hardware, has brought in a consultant, Makayla Lerner, to build an inventory database system for the store. 

REQUIREMENTS: 

The database must store: 
-	Items sold in the hardware store, including item name, item category, and item cost
-	The number of each item in stock
-	The manufacturer of the items, including manufacturer addresses and delivery days
-	The name and phone number of the delivery person who last delivered a set of items for the manufacturer

The user must be able to: 
-	Insert new items
-	Remove items
-	Search for items by name or category of item and retrieve the current number in stock
-	If an item is sold out, the next delivery date must be also returned to the user
-	Update the number of items in stock
-	View all items that are sold out
-	View the last delivery person for an item
-	Update the last delivery person for an item 

ASSUMPTIONS: 

The following assumptions were considered in the design of the system: 
-	Each item is unique 
-	Each item has 1 manufacturer, but manufacturers can make many items. 
-	The categories for items are pre-defined with corresponding characters. The categories are tools (T), building materials (B), machinery (M), paints and stains (P), housewares (H), lawn and garden (L), and miscellaneous (M). 
-	The user has access to unique item_ids and manufacturer_ids when making changes to the system such as deleting items or updating the stock of an item. 
-	Manufacturers make weekly deliveries on the same day. 
-	User updates the item stock when deliveries and sales are made. 
-	User updates delivery person as needed.

DESIGN:

The database: 

The database was designed to have two tables: manufacturers and items. The manufacturers table has 6 columns: a primary key (manufacturer_id), manufacturer_name, manufacturer_address, delivery_day, delivery_person_name, and delivery_phone_num. The items table has 6 columns as well: a primary key (item_id), item_name, item_category, item_cost, item_quant_in_stock, and a foreign key of manufacturer_id so manufacturer and delivery information can be obtained by joining the tables on the manufacturer_id. 
Below is an entity relationship diagram of the system, where there is a one-to-many relationship between manufacturers and items. 

![image](https://user-images.githubusercontent.com/57692009/201999984-2cf0b012-e939-4fa1-8985-94230c8fca64.png)

The software: 

The system is broken up into four files: schema.sql, main.py, body.py, and database.py. 
The schema file holds the SQL queries to create the database tables. The consultant prefers to make a separate schema file for readability and modularity purposes. Separating the schema also reduces the number of strings in the database file. 
The main file was designed to be as simple as possible as it is to be read and run often. It uses functions from the body and database files. It has a simple welcome statement, then sets up the connection to sqlite3 to be used by nearly every function in the system. The main structure is a while loop that goes through the menu choices and calls respective prompt functions. 
The body file holds the item categories dictionary, prompt functions, and functions that call database functions. It creates the menu and all the strings used to prompt the user for inputs as well as directing the system to other functions based on a user’s choice. There are 14 functions defined in this file, broken down by actions that the system takes. 
The database file holds many SQL statements and 9 functions, including the function that sets up the database (setup_db) with an optional reset flag (force_reset) and sets up the connection too be used by every function. The functions each call the SQL statements defined in the file after they are called by their respective functions in the body. 

APPENDIX

The system was tested and created using data inspired by Stardew Valley, a video game by ConcernedApe. Data was loaded by pasting into DB Browser, as the assignment did not permit the use of other libraries. The csv files created from the wiki site are attached and the sites are referenced below. Other data including item quantities, addresses, and phone numbers were randomly generated. 

ConcernedApe. (2016). Stardew Valley. Retrieved October 14, 2022, from https://www.stardewvalley.net/ 

Stardew Valley Wiki. (2021, October 25). Marnie's ranch. Stardew Valley Wiki. Retrieved October 14, 2022, from https://stardewvalleywiki.com/Marnie%27s_Ranch 

Stardew Valley Wiki. (2022, August 13). Blacksmith. Stardew Valley Wiki. Retrieved October 14, 2022, from https://stardewvalleywiki.com/Blacksmith 

Stardew Valley Wiki. (2022, August 29). Carpenter's shop. Stardew Valley Wiki. Retrieved October 14, 2022, from https://stardewvalleywiki.com/Carpenter%27s_Shop 

Stardew Valley Wiki. (2022, August 7). Pierre's General Store. Stardew Valley Wiki. Retrieved October 14, 2022, from https://stardewvalleywiki.com/Pierre%27s_General_Store 

Stardew Valley Wiki. (2022, September 6). Fish shop. Stardew Valley Wiki. Retrieved October 14, 2022, from https://stardewvalleywiki.com/Fish_Shop 


