accounts = []


def signin():
    name = input('Enter name: ')
    balance = int(input('Enter balance: '))
    num = len(accounts) + 1
    account = {
        'name': name,
        'balance': balance,
        'account_number': num,
        'transactions': []
    }
    accounts.append(account)
    print(f'Your account number: {num}')


def get_account_by_num(account_num):
    result = list(filter(lambda x: x['account_number'] == account_num, accounts))
    if not result:
        print('You enter invalid account number, please try again')
        return
    return result[0]


def deposit(acc, dep):
    acc['balance'] += dep
    acc['transactions'].append({'type': 'deposit', 'amount': dep})


def withdraw(acc, wth):
    if wth > acc['balance']:
        print('You dont have enough money')
        return
    acc['balance'] -= wth
    acc['transactions'].append({'type': 'withdraw', 'amount': wth})


def transactions(acc):
    for trans in acc['transactions']:
        print(f'Operation type: {trans["type"]} with amount: {trans["amount"]}')


def show_balance():
    print(account['balance'])


def operations():
    print('Enter 0 if you want to see balance')
    print('Enter 1 if you want to withdraw')
    print('Enter 2 if you want to deposit')
    print('Enter 3 if you want to see the list of transactions')
    print('Enter q if you want to logout')

    option = input('Enter your choice: ')

    return option


def menu():
    print('Enter your type of operation')
    print('Enter 1 if you want to sign in')
    print('Enter 2 if you want to log in')
    print('Enter q if you want to quit')

    option = input('Enter your choice ')

    return option


if __name__ == '__main__':
    while True:
        choose_1 = menu()
        if choose_1 == '1':
            signin()
        elif choose_1 == '2':
            while True:
                account_num = int(input('Enter account number: '))
                account = get_account_by_num(account_num)
                if account:
                    break
            while True:
                choose_2 = operations()
                if choose_2 == '0':
                    show_balance()
                elif choose_2 == '1':
                    wth = int(input('How much you want to withdraw: '))
                    withdraw(account, wth)
                elif choose_2 == '2':
                    dep = int(input('How much you want to deposit: '))
                    deposit(account, dep)
                elif choose_2 == '3':
                    transactions(account)
                elif choose_2 == 'q':
                    break
        elif choose_1 == 'q':
            break
