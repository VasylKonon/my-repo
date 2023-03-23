def read_todo_list(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        todo_list = {}
        for line in lines:
            key, val = line.strip().split(': ')
            todo_list[int(key)] = val
        f.close()
        return todo_list
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty todo list.")
        return {}


def write_todo_list(todo_list, filename):
    f = open(filename, 'w')
    for key, val in todo_list.items():
        f.write(f"{key}: {val}\n")
    f.close()
    print(f"Todo list saved to {filename}.")


filename = 'hw9.txt'
todo_list = read_todo_list(filename)

answer = input('Select the action(add, edit, del, get). For quit press "q": ')

while answer != 'q':
    if answer == 'add':
        a = len(todo_list) + 1
        task = input('Enter what you want to add: ')
        todo_list[a] = task
        print(f'Successfully added "{task}"')
    elif answer == 'edit':
        y = int(input('Enter the number of task you want to change: '))
        del_val_list = todo_list[y]
        new_val_list = input('Enter new task: ')
        todo_list[y] = new_val_list
        print(f'You changed "{del_val_list}" for "{new_val_list}"')
    elif answer == 'del':
        z = int(input('Enter the number of task you want to delete: '))
        del_key_list = todo_list.pop(z)
        print(f'You delete "{del_key_list}"')
        todo_list[z] = 'Empty task'
    elif answer == 'get':
        print('Your list of tasks:', todo_list)
    else:
        print('Unknown action. Please, try again.')

    answer = input('Select the action(add, edit, del, get). For quit press "q": ')

write_todo_list(todo_list, filename)

print('Program completed')
