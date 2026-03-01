# ===============================
# Program MyParkir UMS
# ===============================

# ---------- LIST GLOBAL ----------
# Menyimpan semua data kendaraan
data_kendaraan = []

# ---------- FUNGSI LOGIN ----------
def login_sso():
    try:
        username = input("Masukkan username SSO: ")
        password = input("Masukkan password SSO: ")

        if username == "" or password == "":
            raise ValueError("Username dan password tidak boleh kosong")

        print("Login SSO berhasil\n")
        return True

    except ValueError as e:
        print("Error:", e)
        return False


# ---------- FUNGSI INPUT DATA STNK ----------
def input_stnk():
    try:
        nama = input("Masukkan nama pemilik kendaraan: ")
        nomor_kendaraan = input("Masukkan nomor kendaraan: ")

        if nama == "" or nomor_kendaraan == "":
            raise ValueError("Data STNK tidak lengkap")

        # Menggunakan tuple
        data = (nama, nomor_kendaraan)
        return data

    except ValueError as e:
        print("Error:", e)
        return None


# ---------- TAMBAH DATA KE LIST ----------
def tambah_ke_list(data):
    # Menyimpan tuple ke list
    data_kendaraan.append(data)
    print("Data berhasil ditambahkan ke list\n")


# ---------- FUNGSI SIMPAN KE FILE ----------
def simpan_data_file():
    try:
        with open("data_parkir.txt", "a") as file:
            for kendaraan in data_kendaraan:
                file.write(f"Nama: {kendaraan[0]}, Kendaraan: {kendaraan[1]}\n")

        print("Semua data berhasil disimpan ke file\n")

    except IOError:
        print("Gagal menyimpan data")


# ---------- FUNGSI TAMPILKAN BARCODE ----------
def tampilkan_barcode(nomor_kendaraan):
    print("\n=== BARCODE PARKIR UMS ===")
    print("|| ||| | || |||")
    print("Kode Kendaraan:", nomor_kendaraan)
    print("Gunakan barcode ini untuk masuk dan keluar kampus\n")


# ---------- PROGRAM UTAMA ----------
def main():
    print("=== SISTEM PARKIR UMS ===")

    # Perulangan login
    while True:
        if login_sso():
            break
        else:
            print("Silakan login ulang\n")

    # Perulangan input kendaraan
    while True:
        data = input_stnk()

        if data is not None:
            tambah_ke_list(data)
            tampilkan_barcode(data[1])
        else:
            print("Input gagal")

        ulang = input("Tambah kendaraan lagi? (y/t): ")
        if ulang.lower() != "y":
            break

    # Simpan semua data ke file
    simpan_data_file()


# ---------- PEMANGGILAN PROGRAM ----------
main()