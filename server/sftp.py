from paramiko import SSHClient, AutoAddPolicy
import pandas as pd
import os
from datetime import datetime

def sftp_ip(ip: str, dev_name: str) -> str:
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        ssh_client.connect(hostname=ip, username='ebianchi', password='Skiing#2')
        ftp_client = ssh_client.open_sftp()
        ftp_client.chdir(f'/home/ebianchi/tinyweb/tinyweather/data/')
        data_dir = ftp_client.listdir()
        for file in data_dir:
            if file == ".config":
                continue
            ftp_client.get(remotepath=f'/home/ebianchi/tinyweb/tinyweather/data/{file}', 
                        localpath=f'/Users/{os.getlogin()}/programs/tinyserver/data/{dev_name}/{file}'
                        )
        ftp_client.close()
        return f"data retrieval successful from {ip}"


if __name__ == "__main__":
    df = pd.read_csv('server/nodes.csv')
    for ip, dev_name in df.itertuples(index=False):
        with open(f"/Users/{os.getlogin()}/programs/tinyserver/server/logs/sftp_log.txt", 'a') as file:
            file.write(f"{sftp_ip(ip, dev_name)} at {datetime.now()}\n")

