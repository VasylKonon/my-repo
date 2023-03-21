todo_list = {}
answer = input('Select the action(add, edit, del, get). For quit press "q": ')


def add_list(x):
    a = len(todo_list) + 1
    todo_list[a] = x
    print(f'Successfully added "{x}"')


def edit_list(y):
    del_val_list = todo_list[y]
    new_val_list = input('Enter new task: ')
    todo_list[y] = new_val_list
    print(f'You change "{del_val_list}" for "{new_val_list}"')


def del_list(z):
    del_key_list = todo_list.pop(z)
    print(f'You delete "{del_key_list}"')
    todo_list[z] = 'Empty task'


while answer != 'q':
    if answer == 'add':
        add_list(input('Enter what you want to add: '))
    elif answer == 'edit':
        edit_list(int(input('Enter the number of task you want to change: ')))
    elif answer == 'del':
        del_list(int(input('Enter the number of task you want to delete: ')))
    elif answer == 'get':
        print('Your list of tasks:', todo_list)
    else:
        print('Unknown action. Please, try again.')
    answer = input('Select the action(add, edit, del, get). For quit press "q": ')
else:
    print('Program completed')
