nilai={}
while True :
    print('')
    c = input("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar: ")

    #Keluar
    if c.lower() =='k':
        break

    #Lihat (Tabel)
    elif c.lower() == 'l':
        print("Daftar NIlai")
        print("===========================================================")
        print("| NO |  NIM           |  NAMA     | TUGAS |  UTS  |  UAS  | AKHIR |")
        no = 1
        for tabel in nilai.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} | ".format
                  (no, tabel[1], tabel[0], tabel[2], tabel[3], tabel[4], tabel[5]))
            no += 1
        print("===========================================================")

    #Tambah
    elif c.lower() == 't':
        print("Tambah data mahasiswa")
        nama=(input("Nama   : "));
        nim=(input("NIM    : ")); 
        tugas=(input("Tugas  : "));
        uts=(input("UTS    : "));
        uas=(input("UAS    : "));
        akhir=(float(tugas) * 30 / 100) + (float(uts) * 35 / 100) + (float(uas) * 35 / 100)
        nilai[nama]=[nama, nim, tugas, uts, uas, akhir]

    #Ubah
    elif c.lower() == 'u':
        print("Ubah Data Mahasiswa")
        nama = input("Nama = ")
        if nama in nilai.keys():
            nilai[nama][1]=input("Nim = ")
            nilai[nama][2]=input("Tugas = ")
            nilai[nama][3]=input("UTS = ")
            nilai[nama][4]=input("UAS = ")
        else:
            print("Data {0} tidak ada ".format(nama))

    #Hapus
    elif c.lower() == 'h':
        print("Hapus Data")
        nama=input("Nama : ")
        if nama in nilai.keys():
            del nilai[nama]
            print("Data Berhasil dihapus")
        else:
            print("Data {0} tidak ada ".format(nama))

    #Cari
    elif c.lower() == 'c':
        print("Mencari Data Mahasiswa")
        nama=input("Nama : ")
        if nama in nilai.keys():
            print("=======================================================================")
            print("Nama : {0} |NIM: {1} |TUGAS: {2} |UTS: {3} |UAS: {4} |AKHIR: {5} ".format(nilai[nama][0], nilai[nama][1], nilai[nama][2],
                                                                                             nilai[nama][3], nilai[nama][4], nilai[nama][5]))
            print("=======================================================================")
        else:
            print("Data {0} tidak ditemukan".format(nama))
    else:
        print("Pilih menu yang tersedia dengan huruf kecil")
