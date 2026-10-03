#sistem kasir kedai minuman

daftar_menu = [
    {'Kode' : 'A', 'Nama Minuman':  'Es Teh', 'Harga': 5000},
    {'Kode' : 'B', 'Nama Minuman':  'Es Jeruk', 'Harga': 7000},
    {'Kode' : 'C', 'Nama Minuman':  'Kopi Susu', 'Harga': 10000},
    {'Kode' : 'D', 'Nama Minuman':  'Cokelat', 'Harga': 12000},
    {'Kode' : 'E', 'Nama Minuman':  'Matcha Latte', 'Harga': 15000}
]
 
#menampilkan menu
print("===== DAFTAR MENU =====")
for menu in daftar_menu:
    print(f"{menu['Kode']}. {menu['Nama Minuman']} - Rp {menu['Harga']:,}")

#melakukan pemilihkan menu
total = 0
while True:
    pilih = input("Pilih Menu: ")
    jumlah = int(input("Jumlah: "))

    for menu in daftar_menu:
        if menu['Kode'] == pilih:

            harga = menu['Harga']
            nama = menu['Nama Minuman']

            subtotal = harga * jumlah
            print(f"Subtotal: Rp {subtotal:,}")

            total += subtotal

    pilihan = input("Pesan lagi? (y/n): ")
    if pilihan == "n":
        break

print("\n==== PEMBAYARAN ====")
pembayaran = int(input("Uang Pembayaran: "))
kembalian = pembayaran - total

print("\n===== TOTAL =====")
print(f"Total Belanja: Rp {total:,}")
print(f"Uang Pembayaran: Rp {pembayaran:,}")
print(f"Kembalian: Rp {kembalian:,}")
print("---------------------------------------")
print("===== TERIMAKASIH ======")





  