import tkinter as tk
from tkinter import messagebox
import gspread
from google.oauth2.service_account import Credentials

# IMPORT MODUL SENDIRI
import logika_bilangan
import kalkulator_bangun


# =========================
# KONEKSI GOOGLE SHEETS
# =========================

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open("database").sheet1


# =========================
# MEMBUAT HEADER
# =========================

if sheet.cell(1, 1).value == "":
    sheet.update("A1:B1", [["username", "password"]])


# =========================
# FUNGSI LOGIN
# =========================

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Peringatan",
            "Username dan password harus diisi!"
        )
        return

    data = sheet.get_all_values()

    for baris in data[1:]:
        if len(baris) >= 2:
            if baris[0] == username and baris[1] == password:

                messagebox.showinfo(
                    "Login Berhasil",
                    f"Selamat datang, {username}!"
                )

                tampilkan_halaman_utama(username)
                return

    messagebox.showerror(
        "Login Gagal",
        "Username atau password salah!"
    )


# =========================
# FUNGSI BUAT AKUN
# =========================

def buat_akun():
    username = entry_username.get()
    password = entry_password.get()

    if username == "" or password == "":
        messagebox.showwarning(
            "Peringatan",
            "Username dan password harus diisi!"
        )
        return

    data = sheet.get_all_values()

    for baris in data[1:]:
        if len(baris) >= 1:
            if baris[0] == username:
                messagebox.showerror(
                    "Gagal",
                    "Username sudah digunakan!"
                )
                return

    sheet.append_row([username, password])

    messagebox.showinfo(
        "Berhasil",
        "Akun berhasil dibuat!"
    )

    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)


# =========================
# HALAMAN UTAMA
# =========================

def tampilkan_halaman_utama(username):

    login_frame.pack_forget()

    welcome_frame.pack(
        fill="both",
        expand=True
    )

    label_welcome.config(
        text=f"Selamat Datang, {username}!"
    )


# =========================
# MENU LOGIKA BILANGAN
# =========================

def buka_logika_bilangan():

    window = tk.Toplevel(root)

    window.title("Logika Bilangan")
    window.geometry("400x350")

    window.resizable(False, False)

    tk.Label(
        window,
        text="LOGIKA BILANGAN",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    tk.Label(
        window,
        text="Masukkan angka:",
        font=("Arial", 12)
    ).pack()

    entry_angka = tk.Entry(
        window,
        width=25,
        font=("Arial", 12)
    )

    entry_angka.pack(pady=10)

    label_hasil = tk.Label(
        window,
        text="",
        font=("Arial", 12)
    )

    label_hasil.pack(pady=15)

    def proses():

        try:
            angka = int(entry_angka.get())

            if logika_bilangan.cek_prima(angka):
                prima = "Bilangan Prima"
            else:
                prima = "Bukan Bilangan Prima"

            paritas = logika_bilangan.cek_paritas(angka)

            label_hasil.config(
                text=f"{prima}\n{paritas}"
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        window,
        text="CEK",
        width=20,
        command=proses
    ).pack(pady=10)


# =========================
# MENU KALKULATOR BANGUN
# =========================

def buka_kalkulator_bangun():

    window = tk.Toplevel(root)

    window.title("Kalkulator Bangun Datar")
    window.geometry("450x500")

    window.resizable(False, False)

    tk.Label(
        window,
        text="KALKULATOR BANGUN DATAR",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    # =====================
    # BUJUR SANGKAR
    # =====================

    tk.Label(
        window,
        text="Bujur Sangkar",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    tk.Label(
        window,
        text="Sisi:"
    ).pack()

    entry_sisi = tk.Entry(
        window,
        width=25
    )

    entry_sisi.pack(pady=5)

    def hitung_bujur_sangkar():

        try:
            sisi = float(entry_sisi.get())

            luas = kalkulator_bangun.hitung_luas_bujursangkar(sisi)
            keliling = kalkulator_bangun.hitung_keliling_bujursangkar(sisi)

            label_hasil_bujur.config(
                text=f"Luas: {luas}\nKeliling: {keliling}"
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        window,
        text="HITUNG",
        width=20,
        command=hitung_bujur_sangkar
    ).pack(pady=5)

    label_hasil_bujur = tk.Label(
        window,
        text="",
        font=("Arial", 11)
    )

    label_hasil_bujur.pack(pady=5)


    # =====================
    # LINGKARAN
    # =====================

    tk.Label(
        window,
        text="Lingkaran",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    tk.Label(
        window,
        text="Jari-jari:"
    ).pack()

    entry_radius = tk.Entry(
        window,
        width=25
    )

    entry_radius.pack(pady=5)

    def hitung_lingkaran():

        try:
            r = float(entry_radius.get())

            luas = kalkulator_bangun.luas_lingkaran_custom(r)

            label_hasil_lingkaran.config(
                text=f"Luas: {luas}"
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Masukkan angka yang benar!"
            )

    tk.Button(
        window,
        text="HITUNG",
        width=20,
        command=hitung_lingkaran
    ).pack(pady=5)

    label_hasil_lingkaran = tk.Label(
        window,
        text="",
        font=("Arial", 11)
    )

    label_hasil_lingkaran.pack(pady=5)


# =========================
# LOGOUT
# =========================

def logout():

    welcome_frame.pack_forget()

    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

    login_frame.pack(
        fill="both",
        expand=True
    )


# =========================
# KELUAR PROGRAM
# =========================

def keluar():
    root.destroy()


# =========================
# MEMBUAT WINDOW
# =========================

root = tk.Tk()

root.title("Sistem Login")
root.geometry("500x400")

root.resizable(False, False)


# =========================
# FRAME LOGIN
# =========================

login_frame = tk.Frame(root)

login_frame.pack(
    fill="both",
    expand=True
)


label_judul = tk.Label(
    login_frame,
    text="LOGIN SYSTEM",
    font=("Arial", 24, "bold")
)

label_judul.pack(pady=30)


label_username = tk.Label(
    login_frame,
    text="Username",
    font=("Arial", 12)
)

label_username.pack()


entry_username = tk.Entry(
    login_frame,
    width=30,
    font=("Arial", 12)
)

entry_username.pack(pady=5)


label_password = tk.Label(
    login_frame,
    text="Password",
    font=("Arial", 12)
)

label_password.pack()


entry_password = tk.Entry(
    login_frame,
    width=30,
    font=("Arial", 12),
    show="*"
)

entry_password.pack(pady=5)


button_login = tk.Button(
    login_frame,
    text="LOGIN",
    width=20,
    command=login
)

button_login.pack(pady=15)


button_register = tk.Button(
    login_frame,
    text="BUAT AKUN",
    width=20,
    command=buat_akun
)

button_register.pack(pady=5)


button_exit = tk.Button(
    login_frame,
    text="KELUAR",
    width=20,
    command=keluar
)

button_exit.pack(pady=5)


# =========================
# FRAME HALAMAN UTAMA
# =========================

welcome_frame = tk.Frame(root)


label_welcome = tk.Label(
    welcome_frame,
    text="Selamat Datang!",
    font=("Arial", 24, "bold")
)

label_welcome.pack(pady=40)


# Tombol Logika Bilangan
button_logika = tk.Button(
    welcome_frame,
    text="LOGIKA BILANGAN",
    width=25,
    command=buka_logika_bilangan
)

button_logika.pack(pady=8)


# Tombol Kalkulator Bangun
button_kalkulator = tk.Button(
    welcome_frame,
    text="KALKULATOR BANGUN DATAR",
    width=25,
    command=buka_kalkulator_bangun
)

button_kalkulator.pack(pady=8)


# Tombol Logout
button_logout = tk.Button(
    welcome_frame,
    text="LOGOUT",
    width=25,
    command=logout
)

button_logout.pack(pady=8)


# =========================
# MENJALANKAN PROGRAM
# =========================

root.mainloop()
