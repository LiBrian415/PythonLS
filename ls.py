import os
from pathlib import Path

def main():
    path_list = []
    while True:
        n = input("Input next subdirectory or n to stop: (Note: starts at home"
                " directory) ")
        if n == 'n':
            break
        else:
            path_list.append(n)
    if len(path_list) == 0:
        print(os.listdir(Path()))
    else:
        path = Path.home()
        for s in path_list:
            path = path / s
        print(os.listdir(Path(path)))

if __name__ == "__main__": 
    main()
