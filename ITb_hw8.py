def copy_of_txt(first_file, second_file):
    try:
        f1 = open(first_file, "r")
    except FileNotFoundError:
        return f"Non-existing file: {first_file}"

    try:
        f2 = open(second_file, "a")
    except FileNotFoundError:           #Якщо такого файлу не існує, створиться новий. Але на всяк випадок
        return f"Non-existing file: {second_file}", f1.close()

    else:
        try:
            for i in f1:
                f2.write(i)
        except Exception:
            return "Oops, something went wrong."
        else:
            return "Copy successful"
        finally:
            f1.close()
            f2.close()


print(copy_of_txt("test1.txt", "test2.txt"))
