#number two
#This is extended version, contains more data set fron the book and added a option permanent or rented options.
#Also have syncing date for updated information on payment.
import datetime
print("====================================================")
print("                PROGRAM PERPUSTAKAAN                ")
current_date = datetime.date.today()
formatted_date = current_date.strftime("%A, %B %d %Y")
print("Yazao Von Maximus |", formatted_date)
print("====================================================")
print()
NP = input("Nomor Peminjam/Pembeli Buku :")
NB = input("Nama Peminjam/Pembeli       :")
print("Pilih Opsi :")
print("1. Pembelian Permanen")
print("2. Peminjaman")
opsi = input("Masukkan pilihan (1/2)      :")
KJ = input("Kode Jenis Buku             :")
if KJ == 'N':
  NJ = "Novel"
  HG = 3000
elif KJ == 'M':
  NJ = "Majalah"
  HG = 2000
elif KJ == 'C':
  NJ = "Cerita Pendek"
  HG = 2500
elif KJ == 'D':
  NJ = "Dongeng"
  HG = 4000
elif KJ == 'K':
  NJ = "Komik"
  HG = 6000
elif KJ == 'P':
  NJ = "Pelajaran"
  HG = 5000
elif KJ == 'E':
  NJ = "Ensiklopedia"
  HG = 5500
elif KJ == 'RM':
  NJ = "Resep Masak"
  HG = 4500
elif KJ == 'S':
  NJ = "Sejarah"
  HG = 7000
elif KJ == 'G':
  NJ = "Geografi"
  HG = 7500
elif KJ == 'F':
  NJ = "Filosofi"
  HG = 8000
elif KJ == 'T':
  NJ = "Teknologi"
  HG = 8500
elif KJ == 'H':
  NJ = "Hukum"
  HG = 9000
elif KJ == 'M':
  NJ = "Matematika"
elif KJ == 'B':
  NJ = "Bahasa"
  HG = 9500

else:
  NJ = "404 Not Found"
  HG = "404 Not Found"

JB = float(input("Jumlah Buku                 :"))

if opsi == "2":
  LP = float(input("Lama Pinjam (Hari)          :"))

print("")
print("====================================================")
print("")
print("Jenis Buku                  :", NJ)
print("Harga Sewa/Beli Buku        :", HG)

if HG == "404 Not Found":
  TH = "404 Not Found"
else:
  TH = (HG * JB)
print("Total Harga                 :", TH)

if opsi == "2":
  if HG == "404 Not Found":
    DN = "404 Not Found"
  elif LP <= 3:
    DN = 0
  elif LP > 3:
    DN = (LP - 3) * 500
  print("Denda                       :", DN)
  if isinstance(TH, str) or isinstance(DN, str):
    BY = "404 Not Found"
  else:
    BY = (DN + TH)
else:
    BY = TH
    DN = 0
print("")
print("====================================================")
print("")
print("Bayar                       :", BY)
print("")
print("====================================================")
if opsi == "1":
  print("   Terima Kasih Atas Pembeliannya.     ")
elif opsi == "2":
  print("   Terima Kasih Atas Peminjamannya. Jangan Lupa     ")
  print("           Mengembalikan Buku tepat waktu           ")
print("====================================================")
