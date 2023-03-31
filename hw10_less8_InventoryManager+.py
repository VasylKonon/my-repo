print('*' * 200)
print('Welcome to your inventory!')
print('*' * 200)
inventory = {}


def search_inv():
    try:
        search_item = input('Enter item or description: ')
        result = []
        for i, d in inventory.items():
            if search_item.lower() in i.lower() or search_item.lower() in d['description'].lower():
                result.append(i)
        if result:
            for j in result:
                print('*' * 200)
                print(f"{j}({inventory[j]['description']}). Quantity: {inventory[j]['quantity']}")
                print('*' * 200)
        else:
            print('*' * 200)
            print('Item or description not found.')
            print('*' * 200)
    except Exception as e:
        print('*' * 200)
        print(f"Error occurred while searching inventory: {e}")
        print('*' * 200)


def updt_quantity():
    try:
        name_item = input('Enter the item: ')
        if name_item in inventory:
            updt_q = int(input('Enter new quantity of item: '))
            inventory[name_item]['quantity'] = updt_q
            print('*' * 200)
            print(f'Successfully updated quantity')
            print('*' * 200)
        else:
            print('*' * 200)
            print('Item not found')
            print('*' * 200)
    except Exception as e:
        print('*' * 200)
        print(f"Error occurred while updating quantity: {e}")
        print('*' * 200)


def remove_inv():
    try:
        remove = input('Enter item you want to remove from inventory: ')
        if remove in inventory:
            del inventory[remove]
            print('*' * 200)
            print(f'Successfully deleted {remove}')
            print('*' * 200)
        else:
            print('*' * 200)
            print('Item not found.')
            print('*' * 200)
    except Exception as e:
        print('*' * 200)
        print(f"Error occurred while removing item: {e}")
        print('*' * 200)


def add_inv():
    try:
        item = input('Enter item: ')
        description = input('Enter a description of the item: ')
        quantity = int(input('Enter quantity of items: '))
        inventory[item] = {'description': description, 'quantity': quantity}
        print('*' * 200)
        print('Successfully added.')
        print('*' * 200)
    except Exception as e:
        print('*' * 200)
        print(f"Error occurred while adding item: {e}")
        print('*' * 200)


def view_inv():
    try:
        if inventory == {}:
            print('*' * 200)
            print('Empty inventory. Press "a" to add item to your inventory.')
            print('*' * 200)
        else:
            print('*' * 200)
            for item, details in inventory.items():
                print(f"{item}({details['description']}). Quantity: {details['quantity']}")
            print('*' * 200)
    except Exception as e:
        print('*' * 200)
        print(f"Error occurred while viewing inventory: {str(e)}")
        print('*' * 200)


while True:
    print('Here is your following options: ')
    print('To view inventory - press "v"', 'To add item - press "a"', 'To remove item - press "r"',
          'To update quantity - press "u"', 'To search inventory - press "s"', 'To quit - press "q"', sep='\n')
    answer = input('Select an action: ')
    if answer == 'v':
        view_inv()
    elif answer == 'a':
        add_inv()
    elif answer == 'r':
        remove_inv()
    elif answer == 'u':
        updt_quantity()
    elif answer == 's':
        search_inv()
    elif answer == 'q':
        print('*' * 200)
        print('See you in your inventory!')
        print('*' * 200)
        break
    else:
        print('*' * 200)
        print('Unknown operation.')
        print('*' * 200)