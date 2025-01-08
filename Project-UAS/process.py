from data import Data

class Process:
    def validate_input(self, name, age):
        if not name.isalpha():
            raise ValueError("Nama hanya bisa alphabet")
        if not age.isdigit() or int(age) <= 0:
            raise ValueError("Umur hanya bisa  menggunakan angka positif")

    def create_data(self, name, age):
        return Data(name, age)
