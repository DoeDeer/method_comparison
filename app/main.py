import core

if __name__ == '__main__':
    print('-' * 80 + '\nMethod comparison v.0.1.\n' + '-' * 80,
          '\nHello! Please, select command:\n'
          '\t1) Exit;')
    while True:
        cmd = input('Type command here:\n')
        if cmd.lower() == 'exit':
            break
        else:
            print("Command wasn't found")
