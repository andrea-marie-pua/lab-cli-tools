from zipfile import ZipFile, BadZipFile
import zlib

with open("Ashley-Madison.txt", "r", encoding="utf-8") as file:
    passwords = [line.strip() for line in file]

for i, password in enumerate(passwords):
    if i % 10000 == 0: 
        print(i, password)
        
    try:
        with ZipFile("whitehouse_secrets.zip") as zf:
            zf.extractall(pwd=password.encode())

        print("Password found:", password)
        break

    except (RuntimeError, BadZipFile, zlib.error):
        pass