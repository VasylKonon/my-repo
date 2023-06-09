some_list = ["blue", "yellow", "green", "white"]
select_element = input("Enter number of element: ")
try:
    selected = some_list[int(select_element)]
except IndexError:
    print(f"Entered wrong value")
else:
    print(selected)
