member_name = input('Enter your name(example "Name Surname"): ')
list_members = {}

while member_name != 'q':
    list_members[member_name] = 0
    member_name = input('Enter your name(example "Name Surname"): ')
    if member_name in list_members:
        print('name already in list')
        other_name = input('Enter a unique name. You can use numbers at the end of the name: ')
        list_members[other_name] = 0

print('-' * 100)

for i in list_members:
    selected_name = input(f'{i}, choose who you want to vote for(example "Name Surname") {list_members}: ')
    if selected_name not in list_members:
        selected_name = input(f'Choose correct who you want to vote for(example "Name Surname") {list_members}: ')
    list_members[selected_name] += 1

max_val = max(list_members.values())

for k, v in list_members.items():
    if v == max_val:
        print(f'The winner is {k, v}')
