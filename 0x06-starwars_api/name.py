import os

fd = os.open('alx-interview', os.O_RDONLY)

def opener(path, flags):
    return os.opener(path. flags, fd = fd)
with open("names.txt", "w", opener= opener) as f:
    print("this will be written", file=f)
    os.close(fd)