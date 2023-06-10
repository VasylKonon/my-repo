def del_line(file):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        return f"File {file} not found"

    else:
        lines = f.readlines()
        f.close()

        try:
            n = int(input("Enter number of line you want to remove: "))
        except ValueError:
            return "You entered not a number"

        result_after_del = []
        for i in range(len(lines)):
            if i + 1 != n:
                result_after_del.append(lines[i])

        f = open(file, "w")
        f.writelines(result_after_del)
        f.close()


del_line("t1.txt")
