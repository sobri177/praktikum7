
# Penjelasan Program Manajemen Nilai Mahasiswa dengan Class
# 1. Konsep Dasar Class
Class adalah blueprint atau template untuk membuat objek. Dalam program ini, kita membuat class NilaiMahasiswa yang mewakili sistem pengelolaan nilai.

```python
class NilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}
```

# 2. Constructor (__init__)
Method khusus yang dipanggil saat objek dibuat. Menginisialisasi data_mahasiswa sebagai dictionary kosong.

```python
def __init__(self):
    self.data_mahasiswa = {}  # Dictionary untuk menyimpan data
```

# 3. Struktur Data
Menggunakan dictionary bersarang:

Key: Nama mahasiswa (string)

Value: Dictionary lain yang berisi nama dan nilai

Contoh struktur:

``` python
{
    'Sobri': {'nama': 'Sobri', 'nilai': 85.5},
    'EKi': {'nama': 'Eki', 'nilai': 90.0}
}
```

# 4. Method tambah()
```python
def tambah(self):
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai: "))
    self.data_mahasiswa[nama] = {'nama': nama, 'nilai': nilai}
```
Alur kerja:

Input nama dan nilai

Cek apakah nama sudah ada

Validasi input nilai (0-100)

Simpan ke dictionary

# 5. Method tampilkan()
```python
def tampilkan(self):
    for i, (nama, data) in enumerate(self.data_mahasiswa.items(), 1):
        print(f"{i}. {nama} - Nilai: {data['nilai']}")
```
Fitur:

Menampilkan data dalam format tabel

Mengurutkan berdasarkan nama

Menampilkan statistik (rata-rata, nilai tertinggi/terendah)

# 6. Method hapus(nama)
```python
def hapus(self, nama):
    if nama in self.data_mahasiswa:
        del self.data_mahasiswa[nama]
```
Prinsip kerja:

Cek apakah nama ada di dictionary

Jika ada, hapus dengan keyword del

Jika tidak, tampilkan pesan error

7. Method ubah(nama)
```python
def ubah(self, nama):
    if nama in self.data_mahasiswa:
        # Tampilkan data lama
        # Input data baru
        # Update dictionary
        self.data_mahasiswa[nama]['nilai'] = nilai_baru
```
Fitur khusus:

Bisa mengubah nama (membuat entry baru dan hapus yang lama)

Bisa hanya mengubah nilai

Input bisa dikosongkan untuk mempertahankan nilai lama

8. Method menu()
Method untuk membuat interface interaktif dengan pengguna. Menggunakan loop while untuk menampilkan menu berulang.

```python
def menu(self):
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        
        pilihan = input("Pilih: ")
        
        if pilihan == '1':
            self.tambah()
        # ... dan seterusnya
```
9. Method Private _tampilkan_statistik()
Method dengan underscore _ di awal adalah method private (konvensi Python). Hanya digunakan internal class.

```python
def _tampilkan_statistik(self):
    # Hanya dipanggil oleh method tampilkan()
```
10. Kelebihan Menggunakan Class
a. Encapsulation (Enkapsulasi)
```python
# Semua data dan method terkait nilai mahasiswa
# dibungkus dalam satu class
class NilaiMahasiswa:
    data_mahasiswa  # Data terenkapsulasi
    tambah()        # Method terenkapsulasi
    tampilkan()     # Method terenkapsulasi
```
b. Reusability (Dapat Digunakan Ulang)
```python
# Bisa membuat banyak objek dari class yang sama
sistem_kelasA = NilaiMahasiswa()
sistem_kelasB = NilaiMahasiswa()
sistem_kelasC = NilaiMahasiswa()
```
c. Maintainability (Mudah Dikelola)
Semua kode terkumpul dalam satu class

Mudah diubah dan dikembangkan

Tidak mengotori namespace global

11. Alur Program Utama
```python
# 1. Buat objek
sistem_nilai = NilaiMahasiswa()

# 2. Jalankan menu
sistem_nilai.menu()

# Alur dalam menu():
# 1 → tambah() → input data → simpan ke dictionary
# 2 → tampilkan() → baca dictionary → tampilkan tabel
# 3 → hapus(nama) → cari di dictionary → hapus
# 4 → ubah(nama) → cari di dictionary → update
```
12. Contoh Eksekusi Program
```text
========================================
SISTEM MANAJEMEN NILAI MAHASISWA
========================================
1. Tambah Data Mahasiswa
2. Tampilkan Data Mahasiswa
3. Hapus Data Mahasiswa
4. Ubah Data Mahasiswa
5. Keluar
========================================

Pilih menu (1-5): 1
Masukkan nama: Sobri
Masukkan nilai: 85.5
✅ Data berhasil ditambahkan!

Pilih menu (1-5): 2
============================================================
DAFTAR NILAI MAHASISWA
============================================================
No.  Nama                 Nilai      Keterangan    
------------------------------------------------------------
1    Sobri                 85.5       Lulus
```
13. Best Practices yang Diterapkan
Validasi Input: Memastikan input nilai antara 0-100

Error Handling: Menangani input yang tidak valid

User-Friendly: Pesan yang jelas dan format yang rapi

Modular: Setiap method melakukan satu tugas spesifik

Dokumentasi: Komentar yang menjelaskan fungsi method
