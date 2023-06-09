try:
    f = open("some_file.txt", "r")
except FileNotFoundError:
    print("Wrong file")
else:
    print(f.read())
    f.close()
