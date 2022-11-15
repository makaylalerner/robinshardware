
import body
import database


print("Welcome to Robin's Hardware Store Inventory Database! \n")

#set up the database and connection
conn = database.setup_db()

#intialize for while loop
action = 0

while action != 8:
    action = int(body.prompt_menu())

    # add item
    if action == 1:
        body.prompt_add_item(conn)

    # remove item
    elif action == 2:
        body.prompt_remove_item(conn)

    # search
    elif action == 3:
        body.prompt_search(conn)

    # update stock of an item
    elif action == 4:
        body.prompt_stock_update(conn)

    # view sold out items
    elif action == 5:
        body.print_sold_outs(conn)

    # view last delivery person
    elif action == 6:
        body.last_delivery(conn)

    # update last delivery person
    elif action == 7:
        body.prompt_update_last_delivery(conn)

    else:
        action = int(body.prompt_menu(conn))



