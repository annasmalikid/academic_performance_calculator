# Fungsi untuk menghitung nilai akhir berdasarkan nilai komponen penilaian
def nilai_akhir(tugas, absen, uts, uas):
    return (tugas * 0.15) + (absen * 0.05) + (uts * 0.35) + (uas * 0.45)

# Fungsi untuk menghitung grade berdasarkan nilai akhir
def nilai_grade(nilai_akhir):
    if nilai_akhir >= 90:
        return 'A'
    elif nilai_akhir >= 85:
        return 'B+'
    elif nilai_akhir >= 80:
        return 'B'
    elif nilai_akhir >= 70:
        return 'C+'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

# Input nilai dari user
tugas = float(input("Masukkan nilai tugas: "))
absen = float(input("Masukkan nilai absen: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Hitung nilai akhir dan grade
nilai_total = nilai_akhir(tugas, absen, uts, uas)
grade = nilai_grade(nilai_total)

# Tampilkan hasil perhitungan
print("\nNilai Tugas: ", tugas)
print("Nilai Absen: ", absen)
print("Nilai UTS: ", uts)
print("Nilai UAS: ", uas)
print("\nNilai Akhir: ", nilai_total)
print("Grade: ", grade)
