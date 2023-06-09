def work_with_txt():
    f = open("some_file.txt", "a")
    f.write(input("Enter your text: "))
    f.write("\n")
    f.close()


work_with_txt()
