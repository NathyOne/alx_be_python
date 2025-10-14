class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as file:
            return file.read()
    

    def instantiate_from_csv


# Usage
file_obj = FileHandler('oop.py')
print(file_obj.read_data())
