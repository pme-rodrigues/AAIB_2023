def run():
    try:
        message = input('Ok? (y/n):')
        if message == 'y':
            print('ok :)')
        else:
            raise ValueError(message)
    except ValueError as err:
        print(message)

if __name__ == '__main__':
    run()