import socket
import json

host = socket.gethostname()
port = 5000
sock = socket.socket()
sock.connect((host, port))

def sort():
    sock.send(json.dumps({'opt': 'list'}).encode())
    response = json.loads(json.loads(sock.recv(1024).decode()))
    if response['status'] == 'ok':
        for name, number in response['contacts'].items():
            print(f'Name: {name}')
            print(f'Number: {number}\n')
    else:
        print(response['message'])

def add():
    name = input('Enter name: ')
    number = input('Enter number: ')
    sock.send(json.dumps({
        'opt': 'add',
        'name': name,
        'number': number
    }).encode())
    response = json.loads(json.loads(sock.recv(1024).decode()))
    print(response['message'])

def delete():
    name = input('Enter name to delete: ')
    sock.send(json.dumps({
        'opt': 'delete',
        'name': name
    }).encode())
    response = json.loads(json.loads(sock.recv(1024).decode()))
    print(response['message'])

def searchNo():
    n = input('Enter number to search: ')
    sock.send(json.dumps({
        'opt': 'searchNum',
        'number': n
    }).encode())
    response = json.loads(json.loads(sock.recv(1024).decode()))
    if response['status'] == 'ok':
        name = response['contact']['name']
        number = response['contact']['number']
        print(f'Name: {name}')
        print(f'Number: {number}\n')
    else:
        print(response['message'])

def searchName():
    n = input('Enter name to search: ')
    sock.send(json.dumps({
        'opt': 'searchName',
        'name': n
    }).encode())
    response = json.loads(json.loads(sock.recv(1024).decode()))
    if response['status'] == 'ok':
        name = response['contact']['name']
        number = response['contact']['number']
        print(f'Name: {name}')
        print(f'Number: {number}\n')
    else:
        print(response['message'])
    

while(True):
    print('''
    1. List all contacts
    2. Add new contact
    3. Delete a contact
    4. Search by name
    5. Search by number
    6. Exit
    ''')
    opt = int(input('> '))
    match opt:
        case 1: sort()
        case 2: add()
        case 3: delete()
        case 4: searchName()
        case 5: searchNo()
        case 6: break
        case _: print('Invalid input')


sock.close()