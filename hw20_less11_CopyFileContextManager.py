class ContextManager:
    def __init__(self, main_file, copy_file):
        self.main_file = main_file
        self.copy_file = copy_file

    def __enter__(self):
        with open("main_file.txt", "r") as main_file:
            self.file = main_file.read()
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("copy_file.txt", "w") as copy_file:
            copy_file.write(self.file)


with ContextManager("main_file.txt", "copy_file.txt") as manager:
    print("Successfully copied")
