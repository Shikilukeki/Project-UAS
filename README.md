# Project-UAS

Nama : Rifqi Maulana

NIM : 312410529

Kelas : TI.24.A5

Mata Kuliah : Bahasa Pemograman

Dosen Pengampu : Agung Nugroho, S.Kom., M.Kom.

# Penjelasan Program

## ```Class Mahasiswa (mahasiswa.py)```

```python
class Mahasiswa:
    def __init__(self, nama, nim, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nim = nim
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
        self.nilai_akhir = self.hitung_nilai_akhir()

    def hitung_nilai_akhir(self):
        return (0.3 * self.nilai_tugas) + (0.35 * self.nilai_uts) + (0.35 * self.nilai_uas)

```
Kelas Mahasiswa bertanggung jawab untuk mengelola data mahasiswa. Ini termasuk nama, NIM, nilai tugas, nilai UTS, nilai UAS, dan menghitung nilai akhir. Metode hitung_nilai_akhir menghitung nilai akhir berdasarkan bobot nilai tugas, UTS, dan UAS.

## ```Class View (view.py)```

```python
class View:
    def input_data(self):
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        nilai_tugas = float(input("Masukkan nilai tugas: "))
        nilai_uts = float(input("Masukkan nilai UTS: "))
        nilai_uas = float(input("Masukkan nilai UAS: "))
        return nama, nim, nilai_tugas, nilai_uts, nilai_uas

    def tampilkan_data(self, data_mahasiswa):
        print("\nDaftar Data Mahasiswa:")
        print("==========================================================================================")
        print("| No | Nama                      | NIM       | Tugas | UTS   | UAS   | Akhir             |")
        print("==========================================================================================")

        for i, mahasiswa in enumerate(data_mahasiswa, start=1):
            print(f"| {i:>2} | {mahasiswa.nama:<25} | {mahasiswa.nim:<9} | {mahasiswa.nilai_tugas:<5} | {mahasiswa.nilai_uts:<5} | {mahasiswa.nilai_uas:<5} | {mahasiswa.nilai_akhir:<17.2f} |")
            print("==========================================================================================")

```
Kelas View bertanggung jawab untuk interaksi dengan pengguna. Ini termasuk metode input_data untuk mendapatkan input dari pengguna dan metode tampilkan_data untuk menampilkan data mahasiswa dalam bentuk tabel.

## ```Class Controller (controller.py)```

```python
from mahasiswa import Mahasiswa
from view import View

class Controller:
    def __init__(self):
        self.data_mahasiswa = []
        self.view = View()

    def tambah_data(self):
        nama, nim, nilai_tugas, nilai_uts, nilai_uas = self.view.input_data()
        mahasiswa = Mahasiswa(nama, nim, nilai_tugas, nilai_uts, nilai_uas)
        self.data_mahasiswa.append(mahasiswa)

    def tampilkan_data(self):
        self.view.tampilkan_data(self.data_mahasiswa)

    def jalankan(self):
        while True:
            self.tambah_data()
            tambah_data = input("Tambah data lagi? (y/t): ")
            if tambah_data.lower() == 't':
                break
        self.tampilkan_data()

```
Kelas Controller bertanggung jawab untuk mengelola alur logika program. Ini termasuk menambah data mahasiswa (tambah_data), menampilkan data mahasiswa (tampilkan_data), dan menjalankan keseluruhan program (jalankan).

## ```main.py```

```python
from controller import Controller

if __name__ == "__main__":
    controller = Controller()
    controller.jalankan()

```
File main.py adalah titik masuk program. Ini membuat instance Controller dan menjalankan metode jalankan untuk memulai program.

# Hasil eksekusi program

![image](https://github.com/Shikilukeki/Foto/blob/main/Project%20UAS%20semester%201.png?raw=true)
