def run():
    try:
        message = input('Ok? (y/n):')
        if message == 'y':
            print('ok :)')
        else:
            raise ValueError()
    except ValueError():
        print(':(')

if __name__ == '__main__':
    run()