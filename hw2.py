member_name = ''
list_members = {}

while member_name != 'q':
    member_name = input('Enter your name(example "Name Surname"): ')
    if member_name == 'q':
        break
    elif member_name in list_members:
        print('The name already in list, enter new name.')
        continue
    list_members[member_name] = 0
    print('For quit enter "q".')

print('-' * 100)

counter = 0
while counter != len(list_members):
    selected_name = input(f'{list(list_members.keys())[counter]} '
                          f'choose who you want to vote for(example "Name Surname") {list_members}: ')
    if selected_name not in list_members:
        print(f'{selected_name} not in list. Choose correct name {list_members}: ')
        continue
    list_members[selected_name] += 1
    counter += 1

max_val = max(list_members.values())

for k, v in list_members.items():
    if v == max_val:
        print(f'The winner is {k, v}')
