class NilaiMahasiswa:
    def __init__(self):
        # Dictionary untuk menyimpan data mahasiswa
        # Format: {'nama': {'nama': '...', 'nilai': ...}}
        self.data_mahasiswa = {}
    
    def tambah(self):
        """Method untuk menambah data mahasiswa"""
        print("\n" + "="*40)
        print("TAMBAH DATA MAHASISWA")
        print("="*40)
        
        nama = input("Masukkan nama mahasiswa: ").strip()
        
        # Cek apakah nama sudah ada
        if nama in self.data_mahasiswa:
            print(f"⚠️  Mahasiswa dengan nama '{nama}' sudah ada!")
            return
        
        # Input nilai dengan validasi
        while True:
            try:
                nilai = float(input("Masukkan nilai (0-100): "))
                if 0 <= nilai <= 100:
                    break
                else:
                    print("⚠️  Nilai harus antara 0-100!")
            except ValueError:
                print("⚠️  Input harus berupa angka!")
        
        # Simpan data
        self.data_mahasiswa[nama] = {
            'nama': nama,
            'nilai': nilai
        }
        print(f"✅ Data mahasiswa '{nama}' berhasil ditambahkan!")
    
    def tampilkan(self):
        """Method untuk menampilkan semua data mahasiswa"""
        print("\n" + "="*60)
        print("DAFTAR NILAI MAHASISWA")
        print("="*60)
        
        if not self.data_mahasiswa:
            print("📭 Tidak ada data mahasiswa!")
            return
        
        print(f"{'No.':<5} {'Nama':<20} {'Nilai':<10} {'Keterangan':<15}")
        print("-"*60)
        
        # Urutkan data berdasarkan nama
        sorted_data = sorted(self.data_mahasiswa.items())
        
        for i, (nama, data) in enumerate(sorted_data, 1):
            nilai = data['nilai']
            keterangan = "Lulus" if nilai >= 60 else "Tidak Lulus"
            print(f"{i:<5} {nama:<20} {nilai:<10} {keterangan:<15}")
        
        # Tampilkan statistik
        self._tampilkan_statistik()
    
    def _tampilkan_statistik(self):
        """Method private untuk menampilkan statistik"""
        if self.data_mahasiswa:
            nilai_list = [data['nilai'] for data in self.data_mahasiswa.values()]
            rata_rata = sum(nilai_list) / len(nilai_list)
            nilai_tertinggi = max(nilai_list)
            nilai_terendah = min(nilai_list)
            
            print("-"*60)
            print(f"📊 Statistik:")
            print(f"   Jumlah Mahasiswa : {len(self.data_mahasiswa)}")
            print(f"   Nilai Tertinggi  : {nilai_tertinggi}")
            print(f"   Nilai Terendah   : {nilai_terendah}")
            print(f"   Rata-rata Nilai  : {rata_rata:.2f}")
    
    def hapus(self, nama):
        """Method untuk menghapus data berdasarkan nama"""
        print("\n" + "="*40)
        print("HAPUS DATA MAHASISWA")
        print("="*40)
        
        if nama in self.data_mahasiswa:
            del self.data_mahasiswa[nama]
            print(f"✅ Data mahasiswa '{nama}' berhasil dihapus!")
        else:
            print(f"⚠️  Mahasiswa dengan nama '{nama}' tidak ditemukan!")
    
    def ubah(self, nama):
        """Method untuk mengubah data berdasarkan nama"""
        print("\n" + "="*40)
        print("UBAH DATA MAHASISWA")
        print("="*40)
        
        if nama not in self.data_mahasiswa:
            print(f"⚠️  Mahasiswa dengan nama '{nama}' tidak ditemukan!")
            return
        
        print(f"Data saat ini: {self.data_mahasiswa[nama]}")
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
        
        # Input nama baru
        nama_baru = input(f"Nama baru [{nama}]: ").strip()
        if not nama_baru:
            nama_baru = nama
        
        # Input nilai baru
        while True:
            nilai_input = input(f"Nilai baru [{self.data_mahasiswa[nama]['nilai']}]: ").strip()
            
            if not nilai_input:  # Jika dikosongkan, gunakan nilai lama
                nilai_baru = self.data_mahasiswa[nama]['nilai']
                break
            
            try:
                nilai_baru = float(nilai_input)
                if 0 <= nilai_baru <= 100:
                    break
                else:
                    print("⚠️  Nilai harus antara 0-100!")
            except ValueError:
                print("⚠️  Input harus berupa angka!")
        
        # Jika nama berubah, hapus entry lama dan buat baru
        if nama_baru != nama:
            # Simpan data ke nama baru
            self.data_mahasiswa[nama_baru] = {
                'nama': nama_baru,
                'nilai': nilai_baru
            }
            # Hapus data lama
            del self.data_mahasiswa[nama]
            print(f"✅ Data berhasil diubah dari '{nama}' menjadi '{nama_baru}'!")
        else:
            # Update data yang ada
            self.data_mahasiswa[nama]['nilai'] = nilai_baru
            print(f"✅ Data mahasiswa '{nama}' berhasil diubah!")
    
    def menu(self):
        """Method untuk menampilkan menu utama"""
        while True:
            print("\n" + "="*40)
            print("SISTEM MANAJEMEN NILAI MAHASISWA")
            print("="*40)
            print("1. Tambah Data Mahasiswa")
            print("2. Tampilkan Data Mahasiswa")
            print("3. Hapus Data Mahasiswa")
            print("4. Ubah Data Mahasiswa")
            print("5. Keluar")
            print("="*40)
            
            pilihan = input("Pilih menu (1-5): ").strip()
            
            if pilihan == '1':
                self.tambah()
            elif pilihan == '2':
                self.tampilkan()
            elif pilihan == '3':
                nama = input("Masukkan nama mahasiswa yang akan dihapus: ").strip()
                if nama:  # Pastikan input tidak kosong
                    self.hapus(nama)
                else:
                    print("⚠️  Nama tidak boleh kosong!")
            elif pilihan == '4':
                nama = input("Masukkan nama mahasiswa yang akan diubah: ").strip()
                if nama:  # Pastikan input tidak kosong
                    self.ubah(nama)
                else:
                    print("⚠️  Nama tidak boleh kosong!")
            elif pilihan == '5':
                print("\n👋 Terima kasih telah menggunakan program!")
                break
            else:
                print("⚠️  Pilihan tidak valid! Silakan pilih 1-5.")
            
            input("\nTekan Enter untuk melanjutkan...")


# Program utama
if __name__ == "__main__":
    # Membuat objek dari class NilaiMahasiswa
    sistem_nilai = NilaiMahasiswa()
    
    # Menjalankan menu utama
    sistem_nilai.menu()