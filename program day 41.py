print("fungsi rekursif")
def halo_dunia ():
    print("halo dunia")
halo_dunia()
for i in range(10):
    print(i)
def tampilkan_angka(i):
    print("perulangan ke", {i})
tampilkan_angka(1)
tampilkan_angka(2)
tampilkan_angka(3)
print("perubahan")
def tampilkan_angka(batas,i=1):
    print("perulangan ke", {i})
    if (i < batas):
        tampilkan_angka(batas,i+1)
tampilkan_angka(6)
print("setelah ada tambahan")    
def tampilkan_angka(batas,i=1):
    print(f'perulangan ke {i}')
    if (i < batas):
        tampilkan_angka(batas,i+1)
tampilkan_angka(12,2)

print("proses REKURSIF yang terlebih dahulu baru setelah itu proses print()")
def tampilakan_angka(batas,i=1):
    if (i<batas):
        tampilakan_angka(batas, i+1)
    print("perulangan ke:",i)
tampilakan_angka(10)
print("penjelasan")
def tampilkan_angka(batas,i=1):
    prefix='...'*(i-1)

    print(f'{prefix} sebelum rekursif ({i})')
    if(i < batas):
        tampilkan_angka(batas ,i+1)
    print(f'{prefix} sebelum rekursif ({i})')
tampilakan_angka(5)
