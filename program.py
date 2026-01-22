print("\n----- SISTEM ATM -----")
print("Pilih Menu:")
print("1. Cek saldo")
print("2. Setor saldo")
print("3. Tarik saldo")
print("4. Keluar")

saldo=1000000

while True:
    pilih=input("\nPilih Menu (1-4): ")

    if pilih=="1":
        print(f"Saldo: Rp{saldo:,}")

    elif pilih=="2":
        setor=int(input("Masukan Nominal: "))

        saldo+=setor
        print(f"Setor berhasil.")
        print(f"Saldo kamu: Rp {saldo:,}")

    elif pilih=="3":
        tarik=int(input("masukan nominal yang ingin ditarik: "))

        if tarik > saldo:
            print("saldo tidak mencukupi.")
        else:
            saldo-=tarik
            print(f"Penarikan berhasil. Sisa saldo: Rp {saldo:,}")

    elif pilih=="4":
        print("Program selesai!")
        break

    else:
        print("pilihan tidak valid!")
