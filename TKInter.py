import tkinter as tk

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("500x700")
top.configure(bg="#292765")

judul = tk.Label(
    top,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Times New Roman", 16, "bold"),
    bg="#292765",
    fg="white"
)
judul.pack(pady=20)


frame = tk.Frame(top, bg="#292765")
frame.pack()

input_nilai = []

for i in range(10):
    label = tk.Label(
        frame,
        text="Nilai Mata Pelajaran " + str(i + 1) + ":",
        bg="#292765",
        fg="white",
        width=23,
        anchor="w"
    )
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(frame, width=15)
    entry.grid(row=i, column=1, padx=5, pady=5)

    input_nilai.append(entry)

# Label pilihan jurusan
label_jurusan = tk.Label(
    top,
    text="Pilihan Jurusan Anda:",
    bg="#292765",
    fg="white"
)
label_jurusan.pack(pady=(25, 5))

# Pilihan jurusan menggunakan OptionMenu
jurusan = tk.StringVar()
jurusan.set("Teknologi Informasi")

pilihan = tk.OptionMenu(
    top,
    jurusan,
    "Teknologi Informasi",
    "Teknik Sipil",
    "Teknik Elektro",
    "Teknik Mesin",
    "Teknik Elektro Medis",
    "Teknik Rekayasa Otomotif"
)
pilihan.pack()

# Fungsi hasil prediksi
def hasil_prediksi():
    hasil.config(
        text="Prediksi Prodi: Teknologi Informasi"
    )

# Tombol hasil prediksi
button = tk.Button(
    top,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
button.pack(pady=25)

# Label hasil prediksi
hasil = tk.Label(
    top,
    text="",
    bg="#292765",
    fg="#66FFFF",
    font=("Times New Roman", 12, "bold")
)
hasil.pack(pady=5)

# Menjalankan aplikasi
top.mainloop()
