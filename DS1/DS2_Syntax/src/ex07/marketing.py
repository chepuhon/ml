import sys


def get_clients_set() -> set:
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    return set(clients)


def get_participants_set() -> set:
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return set(participants)


def get_recipients_set() -> set:
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return set(recipients)


def get_call_center_list() -> list:
    clients = get_clients_set()
    recipients = get_recipients_set()
    result = clients - recipients
    return sorted(list(result))


def get_potential_clients_list() -> list:
    participants = get_participants_set()
    clients = get_clients_set()
    result = participants - clients
    return sorted(list(result))


def get_loyalty_program_list() -> list:
    clients = get_clients_set()
    participants = get_participants_set()
    result = clients - participants
    return sorted(list(result))


def main() -> None:
    if len(sys.argv) != 2:
        raise Exception("Invalid number of arguments")
    
    task = sys.argv[1]
    
    if task == 'call_center':
        result = get_call_center_list()
    elif task == 'potential_clients':
        result = get_potential_clients_list()
    elif task == 'loyalty_program':
        result = get_loyalty_program_list()
    else:
        raise Exception("Unknown task name")
    
    for email in result:
        print(email)


if __name__ == '__main__':
    main()
