data_list = []

def oi_final_grade(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

def lihat_data():
    if not data_list:
        print("\nTidak ada data!")
    else:
        print("\nDaftar Nilai Mahasiswa")
        print("-" * 70)
        print(f"| {'NO':<2} | {'NIM':<8} | {'NAMA':<10} | {'TUGAS':<8} | {'UTS':<8} | {'UAS':<8} | {'AKHIR':<8} |")
        print("-" * 70)
        for idx, student in enumerate(data_list, start=1):
            print(f"| {idx:<2} | {student['NIM']:<8} | {student['Nama']:<10} | "
                  f"{student['Tugas']:<8.2f} | {student['UTS']:<8.2f} | {student['UAS']:<8.2f} | {student['Nilai Akhir']:<8.2f} |")
        print("-" * 70)

def tambah_data():
    Nama = input("Nama: ")
    NIM = input("NIM: ")
    Tugas = float(input("Nilai Tugas: "))
    UTS = float(input("Nilai UTS: "))
    UAS = float(input("Nilai UAS: "))
    final_grade = oi_final_grade(Tugas, UTS, UAS)
    mahasiswa_data = {
        'Nama': Nama,
        'NIM': NIM,
        'Tugas': Tugas,
        'UTS': UTS,
        'UAS': UAS,
        'Nilai Akhir': final_grade
    }
    data_list.append(mahasiswa_data)
    print("\nData berhasil ditambahkan!")

def ubah_data():
    lihat_data()
    index = int(input("\nPilih nomor data yang ingin diubah: ")) - 1
    if 0 <= index < len(data_list):
        print("\nMasukkan data baru:")
        data_list[index]['NIM'] = input("NIM: ")
        data_list[index]['Nama'] = input("Nama: ")
        data_list[index]['Tugas'] = float(input("Nilai Tugas: "))
        data_list[index]['UTS'] = float(input("Nilai UTS: "))
        data_list[index]['UAS'] = float(input("Nilai UAS: "))
        data_list[index]['Nilai Akhir'] = oi_final_grade(
            data_list[index]['Tugas'], 
            data_list[index]['UTS'], 
            data_list[index]['UAS']
        )
        print("\nData berhasil diubah!")
    else:
        print("\nNomor data tidak ditemukan!")

def hapus_data():
    lihat_data()
    index = int(input("\nPilih nomor data yang ingin dihapus: ")) - 1
    if 0 <= index < len(data_list):
        data_list.pop(index)
        print("\nData berhasil dihapus!")
    else:
        print("\nNomor data tidak ditemukan!")

def cari_data():
    keyword = input("Masukkan NIM atau Nama yang ingin dicari: ").lower()
    found = [data for data in data_list if keyword in data['NIM'].lower() or keyword in data['Nama'].lower()]
    if found:
        print("\nHasil Pencarian:")
        print("-" * 70)
        print(f"| {'NO':<2} | {'NIM':<8} | {'NAMA':<10} | {'TUGAS':<8} | {'UTS':<8} | {'UAS':<8} | {'AKHIR':<8} |")
        print("-" * 70)
        for idx, student in enumerate(found, start=1):
            print(f"| {idx:<2} | {student['NIM']:<8} | {student['Nama']:<10} | "
                  f"{student['Tugas']:<8.2f} | {student['UTS']:<8.2f} | {student['UAS']:<8.2f} | {student['Nilai Akhir']:<8.2f} |")
        print("-" * 70)
    else:
        print("\nData tidak ditemukan!")

while True:
    print("\n[L]ihat, [T]ambah, [U]bah, [H]apus, [C]ari, [K]eluar")
    pilihan = input("Pilih menu: ").lower()
    if pilihan == 'l':
        lihat_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'c':
        cari_data()
    elif pilihan == 'k':
        print("\nProgram selesai. Sampai jumpa!")
        break
    else:
        print("\nPilihan tidak valid!")
