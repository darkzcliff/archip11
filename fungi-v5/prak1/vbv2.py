default_books = [
    {"judul": "A Tale of Two Cities", "pengarang": "Charles Dickens", "kode": "0001", "status": True},
    {"judul": "Harry Potter and the Sorcerer's Stone", "pengarang": "J.K. Rowling", "kode": "0002", "status": True},
    {"judul": "The Lion, the Witch and the Wardrobe", "pengarang": "C.S. Lewis", "kode": "0003", "status": True},
]

def write_to_file(data):
    with open("temp.txt", "w") as file:
        for item in data:
            file.write(f"{item['judul']}<>{item['pengarang']}<>{item['kode']}<>{item.get('status', True)}\n")

def read_temp():
    data = []
    try:
        with open("temp.txt", "r") as file:
            for line in file:
                info = line.split("<>")
                buku_info = {
                    "judul": info[0],
                    "pengarang": info[1],
                    "kode": info[2],
                    "status": info[3].strip()
                }
                data.append(buku_info)
    except FileNotFoundError:
        with open("temp.txt", "w") as file:
            for item in default_books:
                file.write(f"{item['judul']}<>{item['pengarang']}<>{item['kode']}<>{item['status']}\n")
        return default_books
    return data

def list_of_books():
    with open("temp.txt", 'r') as read_db:
        for i, info in enumerate(read_db, start=1):
            splt = info.split('<>')
            stat = "Tersedia" if splt[3].strip() == "True" else "Dipinjam"
            print(f"{i}. {splt[0]} oleh {splt[1]} - {splt[2]} {stat}")

def borrow_a_book():
    data = read_temp()
    list_of_books()
    try:
        nomor_buku = int(input("\nMasukkan nomor buku yang ingin dipinjam: ")) - 1
        if 0 <= nomor_buku < len(data) and data[nomor_buku]["status"] == "True":
            data[nomor_buku]["status"] = "False"
            print(f"Anda telah meminjam buku {data[nomor_buku]['judul']}")
            write_to_file(data)
        else:
            print("Try again.")
    except ValueError:
        print("Nomor tidak valid.")

def return_a_book():
    data = read_temp()
    kode_buku = input("Masukkan kode buku yang ingin dikembalikan: ")

    found = False
    for info in data:
        print(info['kode'], info['judul'], info['status'])
        if info['kode'] == kode_buku and info['status'] == "False":
            info['status'] = "True"
            found = True
            print(f"Anda telah mengembalikan buku {info['judul']}")
            write_to_file(data)
            break

    if not found:
        print("Buku dengan kode tersebut tidak dapat ditemukan atau belum dipinjam.")


def add_to_db():
    data = read_temp()
    print("\n[ List of Books ]")
    list_of_books()
    judul = input("\nMasukkan judul buku\t\t: ")
    pengarang = input("Masukkan nama pengarang\t\t: ")
    kode = input("Masukkan kode buku\t\t: ")

    if check_duplicate(data, judul, kode):
        print("Judul buku atau kode buku sudah ada dalam database.")
    else:
        buku_baru = {
            "judul": judul,
            "pengarang": pengarang,
            "kode": kode
        }
        data.append(buku_baru)
        write_to_file(data)
        print(f"Buku {judul} telah ditambahkan ke dalam database.")

def check_duplicate(data, judul, kode):
    for check in data:
        if check["judul"] == judul or check["kode"] == kode:
            return True
    return False

def as_user():
    while True:
        print("\n1. Pinjam Buku\n2. Kembalikan buku\n3. List buku\n0. Logout")
        choose = input('>> ')

        if choose == '1':
            borrow_a_book()
        elif choose == '2':
            return_a_book()
        elif choose == '3':
            list_of_books()
        elif choose == '0':
            break

def as_admin():
    while True:
        print("\n1. Tambah buku\n0. Logout")
        choose = input('>> ')

        if choose == '1':
            add_to_db()
        elif choose == '0':
            break

def main():
    while True:
        print("\nWelcome to the Library!")
        print("1. Login as Admin\n2. Login as Guest\n0. exit")
        choose = input('>> ')

        if choose == '1':
            as_admin()
        elif choose == '2':
            as_user()
        elif choose == '0':
            exit(0)

if __name__ == "__main__":
    main()
