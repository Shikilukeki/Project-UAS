class View:
    def get_input(self):
        name = input("Masukkan Nama: ")
        age = input("Masukan umur: ")
        return name, age

    def display_result(self, data):
        print(f"Name: {data.name}")
        print(f"Age: {data.age}")
