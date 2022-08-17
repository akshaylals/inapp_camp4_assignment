import json

import socket

contacts = dict()

def searchNo(request):
    for name, number in contacts.items():
        if number == request['number']:
            return json.dumps({
                'status': 'ok',
                'message': '',
                'contact': {
                    'name': name,
                    'number': number
                }
            })
    return json.dumps({
        'status': 'error',
        'message': f'{request["number"]} does not exist',
        'contact': {}
    })


def searchName(request):
    for name, number in contacts.items():
        if name.lower() == request['name']:
            return json.dumps({
                'status': 'ok',
                'message': '',
                'contact': {
                    'name': name,
                    'number': number
                }
            })
    return json.dumps({
        'status': 'error',
        'message': f'{request["name"]} does not exist',
        'contact': {}
    })
            
    

def add(request):
    contacts[request['name']] = request['number']
    return json.dumps({
        'status': 'ok',
        'message': 'Contact added'
    })

def delete(request):
    if contacts.get(request['name']):
        del contacts[request['name']]
        return json.dumps({
            'status': 'ok',
            'message': 'Deleted',
        })
    else:
        return json.dumps({
            'status': 'error',
            'message': f'{request["name"]} does not exist',
        })

def sort():
    if len(contacts) > 0:
        return json.dumps({
            'status': 'ok',
            'message': '',
            'contacts': contacts
        })
    else:
        return json.dumps({
            'status': 'error',
            'message': 'No Contacts',
            'contacts': ''
        })


def phone_server():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    
    c, address = server_socket.accept()
    
    print('Connection from:', str(address))
    
    while True:
        data = c.recv(1024).decode()
        if not data:
            break

        d = json.loads(str(data))
        match d['opt']:
            case 'add': response = json.dumps(add(d))
            case 'delete': response = json.dumps(delete(d))
            case 'searchName': response = json.dumps(searchName(d))
            case 'searchNum': response = json.dumps(searchNo(d))
            case 'list': response = json.dumps(sort())
            case _: response = json.dumps({
                'status': 'error',
                'message': 'Invalid option'
            })
        c.send(response.encode())
    c.close()

if __name__ == '__main__':
    while True:
        phone_server()
    


# tests
# print(sort())

# print(add({
#     'name': 'abc',
#     'number': '12345'
# }))


# print(add({
#     'name': 'def',
#     'number': '687678'
# }))

# print(sort())
# print(searchName({'name': 'abc'}))
# print(searchNo({'number': '12345'}))

# print(delete({'name': 'abc'}))

# print(sort())