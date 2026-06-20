def rupiah(angka):
    return f"{angka:,}".replace(",", ".")


print("SOAL QUIS PYTHON")
print("====================")

id_member = input("ID MEMBER     : ")
nama_barang = input("Nama Barang   : ")
harga_barang = int(input("Harga Barang  : "))
jumlah_beli = int(input("Jumlah Beli   : "))

total = harga_barang * jumlah_beli

# Diskon 10% jika ada ID member
if id_member != "":
    diskon = total * 10 // 100
else:
    diskon = 0

sub_total = total - diskon
ppn = sub_total * 10 // 100
total_bayar = sub_total + ppn

print()
print("===========================")
print()
print("....SWALAYAN MAJU BERSAMA....")
print()
print("===== STRUK PEMBELIAN =====")
print("Kasir          :", id_member)
print("Barang         :", nama_barang)
print("Harga          :", rupiah(harga_barang))
print("Jumlah         :", jumlah_beli)
print("==============================")
print("Total          :", rupiah(total))
print("Diskon         :", rupiah(diskon))
print("------------------------------ -")
print("Sub Total      :", rupiah(sub_total))
print("PPN 10%        :", rupiah(ppn))
print("------------------------------ +")
print("Total Bayar    :", rupiah(total_bayar))