import pysftp

with pysftp.Connection(host='10.1.1.4', username="ebianchi", password="hahah") as sftp:
    with sftp.cd('/home/ebianchi/tinyweb/tinyweather/data'):
        sftp.get('04-29-2023-bme680.csv')