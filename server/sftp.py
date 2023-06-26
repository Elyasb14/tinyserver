import pysftp

with pysftp.Connection(host='192.168.86.91', username="ebianchi", password="Galoisgroup#2") as connection:
    with connection.cd('/Users/ebianchi/programs/tinyweb/tinyweather/data'):
        data_dir = connection.listdir()
        for file in data_dir:
            connection.get(f'{file}', localpath=f'data/{file}')