import os 

files = os.listdir('data')

for file in files:
    print(os.path.getmtime(f"data/{file}"))