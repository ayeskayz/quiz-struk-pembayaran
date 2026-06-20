def rupiah(angka):
    return f"Rp {angka:,}".replace(",", ".")


print("SOAL QUIS PYTHON")
print("====================")

id_member = input("ID MEMBER     : ")
nama_barang = input("Nama Barang   : ")
harga_barang = int(input("Harga Barang  : "))
jumlah_beli = int(input("Jumlah Beli   : "))

total = harga_barang * jumlah_beli

if id_member == "":
    diskon = 0
else:
    diskon = total * 10 // 100

sub_total = total - diskon
ppn = sub_total * 10 // 100
total_bayar = sub_total + ppn

print()
print("Total Bayar otomatis:", rupiah(total_bayar))
uang_bayar = int(input("Uang Bayar    : "))

kembalian = uang_bayar - total_bayar

print()
print("====================")
print("....SWALAYAN MAJU BERSAMA....")
print()
print("===== STRUK PEMBELIAN =====")
print("ID Member      :", id_member if id_member != "" else "Tidak Ada")
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
print("Uang Bayar     :", rupiah(uang_bayar))
print("------------------------------")
print("Kembalian      :", rupiah(kembalian))