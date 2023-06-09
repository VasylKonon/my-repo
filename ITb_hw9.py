def compare(first_file, second_file):
    try:
        f1 = open(first_file, "r")
    except FileNotFoundError:
        return f"File '{first_file}' not found."

    try:
        f2 = open(second_file, "r")
    except FileNotFoundError:
        return f"File '{second_file}' not found.", f1.close()

    else:
        first_lines = f1.readlines()
        second_lines = f2.readlines()
        res = ""
        for i in first_lines:
            if i not in second_lines:
                res += i

    f1.close()
    f2.close()

    return res


print(compare("t1.txt", "t2.txt"))
