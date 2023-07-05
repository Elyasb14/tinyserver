import os

dirs = [dir for dir in os.listdir('data')]
for dir in dirs:
    print(sorted(os.listdir(f'data/{dir}')))