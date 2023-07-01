from paramiko import SSHClient, AutoAddPolicy
import pandas as pd
import os

def sftp_ip(ip: str) -> None:
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(hostname=ip, username='ebianchi', password='hahah')
        ftp_client = ssh_client.open_sftp()
        ftp_client.chdir(f'/Users/ebianchi/programs/tinyweb/tinyweather/data/')
        data_dir = ftp_client.listdir()
        for file in data_dir:
            if file == ".config":
                continue
            ftp_client.get(remotepath=f'/Users/ebianchi/programs/tinyweb/tinyweather/data/{file}', 
                        localpath=f'/Users/{os.getlogin()}/programs/tinyserver/data/{file}'
                        )
        ftp_client.close()
        return f"data retrieval successful from {ip}"


if __name__ == "__main__":
    df = pd.read_csv('server/nodes.csv')
    for ip in df['ip']:
        with open(f"/Users/{os.getlogin()}/programs/tinyserver/server/logs/sftp_log.txt", 'a') as file:
            file.write(f'{sftp_ip(ip)} \n')

