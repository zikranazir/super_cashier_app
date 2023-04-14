from main import Transaction
import sys

trnsct_123 = Transaction() # Instance Class
path = '/SUPER_CASHIER_PROJECT/drive.py' #driver path

print("*"*60)
print("Selamat Datang di Aplikasi Super Cashier")


while True:
    print("*"*60)
    print("Menu Transaksi")
    print("*"*60, "\n")
    print("1. Tambah Item")
    print("2. Update Item")
    print("3. Hapus Item")
    print("4. Hapus Transaksi")
    print("5. Lihat Keranjang")
    print("6. Check Out")
    print("7. Keluar")

    choice = input("Masukkan Pilihan Anda: ")

    if choice == '1':
        nama_item = input("Masukkan Nama Item: ")
        jumlah_item = int(input("Masukkan Jumlah Item: "))
        harga_item = int(input("Masukkan Harga per Item: "))
        trnsct_123.add_item([nama_item, jumlah_item, harga_item])
        print(f"{nama_item} berhasil ditambahkan.")

    elif choice == '2':
        while True:
            print("1. Update Item")
            print("2. Update Jumlah Item")
            print("3. Update Harga Item")
            choice = input("Masukkan Pilihan Anda: ")

            if choice == '1':
                old_item = input("Masukkan Nama Item Lama: ")
                if trnsct_123.check_item(old_item) is True:
                    new_item = input("Masukkan Nama Item baru: ")
                    qty = int(input("Masukkan Jumlah Item: "))
                    price = int(input("Masukkan Harga per Item: "))
                    trnsct_123.delete_item
                    trnsct_123.update_item(new_item, qty, price)
                    print("Item berhasil di update")
                    break

            elif choice == '2':
                nama_item = input("Masukkan Nama Item: ")
                if trnsct_123.check_item(nama_item) is True:
                    jumlah_baru = int(input("Masukkan Jumlah Item Baru: "))
                    trnsct_123.update_item_qty(nama_item, jumlah_baru)
                    print("Jumlah item berhasil diubah.")
                    break

            elif choice == '3':
                nama_item = input("Masukkan Nama Item: ")
                if trnsct_123.check_item(nama_item) is True:
                    harga_baru = int(input("Masukkan Harga Baru: "))
                    trnsct_123.update_item_price(nama_item, harga_baru)
                    print("Harga item berhasil diubah.")
                    break

    elif choice == "3":
        nama_item = input("Masukan Item Yang Akan Dihapus: ")
        if trnsct_123.check_item(nama_item.lower()) is True:
            trnsct_123.delete_item(nama_item)
            print("Berhasil Menghapus {}".format(nama_item))

    elif choice == "4":
        choice = input("Apakah Anda Akan Menghapus Semua Transaksi? (Y/n)")
        if choice.lower() == "y":
            trnsct_123.remove_transaction()
        elif choice.lower() == "n":
            continue
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

    elif choice == '5':
        print("Detail Transaksi:")
        table, item_data, formated_total_harga = trnsct_123.check_order()
        print(table)
        print(formated_total_harga)
        print("1. Lanjutkan Belanja")
        print("2. Checkout")

        while True:
            choice = input("Masukkan Pilihan Anda: ")
            if choice == "1":
                break
            elif choice == "2":
                trnsct_123.check_out()
                while True:
                    choice = input("Apakah Anda Ingin Berbelanja Kembali? {Y/n}:")
                    if choice.lower() == "y":
                        # Exit From Application
                        sys.argv = ['drive.py']
                        exec(open('drive.py').read())
                    elif choice.lower() == "n":
                        # Re-running Application
                        print("Terimakasih telah menggunakan aplikasi Super Cashier")
                        sys.exit()
                    else:
                        # Exception
                        print("Pilihan tidak valid. Silahkan coba lagi.")
                        continue
            else: 
                print("Pilihan tidak valid. Silahkan coba lagi.")
                continue


    elif choice == '6':
        trnsct_123.check_out()
        while True:
            choice = input("Apakah Anda Ingin Berbelanja Kembali? {Y/n}:")
            if choice.lower() == "y":
                # Exit From Application
                sys.argv = ['drive.py']
                exec(open('drive.py').read())
            elif choice.lower() == "n":
                # Re-running Application
                print("Terimakasih telah menggunakan aplikasi Super Cashier")
                sys.exit()
            else:
                # Exception
                print("Pilihan tidak valid. Silahkan coba lagi.")
                continue


    elif choice == '7':
        print("*"*60)
        print("Terimakasih telah menggunakan aplikasi Super Cashier")
        print("*"*60)
        sys.exit()

    else:
        print("Pilihan tidak valid. Silahkan coba lagi.")
