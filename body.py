import database

#predefined categories for simplicity's sake
item_categories = {"T" : "Tools", "B" : "Building Materials", "M" : "Machinery",
                   "P" : "Paints and Stains", "H" : "Housewares",
                   "L" : "Lawn and Garden", "X" : "Misc"}

def prompt_menu():
    #main user interface, only accepts numbers
    menu = '''\nPlease select one of the following options:
    1. Add new item
    2. Remove an item
    3. Search 
    4. Update stock of an item.
    5. View sold out items.
    6. View last delivery person for an item.
    7. Update last delivery person.
    8. Exit

    Your selection: '''
    print(menu)
    action = input()
    return action

def print_categories():
    # setting up the categories output format
    return ''' 
            Type T for Tools \n
            Type B for Building Materials \n
            Type M for Machinery \n
            Type P for Paints and Stains \n
            Type H for Housewares \n
            Type L for Lawn and Garden \n
            Type X for Misc. \n
        '''

def prompt_add_item(conn):
    #add a new item to database
    item_name = input("Enter item name: ").lower() #normalized
    item_category = input(f"Choice a category: \n {print_categories()}").upper() #normalized
    item_cost = input("Enter retail price: \n")
    quant = input("Enter current quantity in stock: \n")
    man_id = input("Enter manufacturer_id: \n")
    database.add_item(conn, item_name, item_category, item_cost, quant, man_id)
    return "Item Added"

def prompt_remove_item(conn):
    # remove an item from the database
    item_id = int(input("Enter the item_id for removal: \n"))
    database.remove_item(conn, item_id)
    return "Item Removed"

def prompt_search(conn):
    # take user input of category or item name to find items
    choice = input("Type C to search by category or I to search by item: ")
    choice = choice.lower() #normalizes input
    if choice == 'c':
        search_by_cat_prompt(conn)
    elif choice == 'i':
        search_by_item_prompt(conn)

def search_by_cat_prompt(conn):
    # user chooses a category from the list to search by
    cat_choice = input(f"Choose a category: \n {print_categories()}").upper() #normalized
    search_by_cat(conn, cat_choice)

def search_by_cat(conn, cat_choice):
    # checks whether the category entered exists by checking the category dictionary keys
    # if not it calls the prompt again
    if cat_choice in item_categories.keys():
        print(database.items_by_cat(conn, cat_choice))
    else:
        search_by_cat_prompt(conn)

def search_by_item_prompt(conn):
    # user can search by item name
    item_choice = input("Enter item name: \n").lower()
    search_by_item(conn, item_choice)

def search_by_item(conn, item_choice):
    # calls database function that queries using the like function in sql so user
    # doesn't have to have the exact name (i.e. you can search "hammer" and find all kinds of hammers)
    print(database.items_by_name(conn, item_choice))

def prompt_stock_update(conn):
    # user can change the number of items in stock
    item = input("Enter the item id to change its stock: \n")
    q = input("Enter the new quantity in stock: \n")
    stock_update(conn, q, item)

def stock_update(conn, q, item):
    database.update_stock_quant(conn, q, item)

def print_sold_outs(conn):
    # returns a list of all sold out items, or where item_quant_in_stock = 0
    print(database.get_sold_outs(conn))

def last_delivery(conn):
    # returns the last delivery person for an item by item_id
    item = input("Enter the item id: \n")
    # takes item_id and finds the corresponding manufacturer_id
    man_id = database.get_man_id_from_item(conn, item)
    print(database.get_last_delivery_person(conn, man_id))

def prompt_update_last_delivery(conn):
    # updates delivery_person_name and delivery_phone_number in deliveries table
    man_id = int(input("Enter the manufacturer_id: \n"))
    name = input("Enter new delivery person's name: \n")
    num = input("Enter the new delivery phone number: \n")
    database.update_delivery_info(conn, man_id, name, num)
    return "Delivery Info Updated"