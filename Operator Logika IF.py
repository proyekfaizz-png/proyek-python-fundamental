print("-"*30)
print("  TUGAS LOGIKA OPERATOR IF")
print("-"*30)

#golongan gaji karyawan
golongan_karyawan=input("Masukan golongan (A/B/C): ")

if golongan_karyawan =="A":
  gaji_pokok = 5000000
elif golongan_karyawan =="B":
   gaji_pokok = 6500000
elif golongan_karyawan =="C":
   gaji_pokok = 9500000
else:
  print("golongan tidak ditemukan")
  gaji_pokok = 0

#lembur karyawan
jam_lembur=int(input("Masukan jam lembur: "))

if jam_lembur == 1 :
  upah_lembur = 0.30*gaji_pokok
elif jam_lembur == 2 :
  upah_lembur = 0.32*gaji_pokok
elif jam_lembur == 3 :
  upah_lembur = 0.34*gaji_pokok
elif jam_lembur == 4 :
  upah_lembur = 0.36*gaji_pokok
elif jam_lembur >= 5 :
  upah_lembur = 0.38*gaji_pokok
else:
  upah_lembur = 0


print("-"*30)
print(f"upah lembur: Rp {upah_lembur:,}")
print(f"Gaji pokok: Rp {gaji_pokok:,}")
print(f"Total Gaji: Rp {upah_lembur + gaji_pokok:,}") #jumlah penghasilan






