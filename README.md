# QR Code and Barcode Detection with OpenCV

Project ini mendeteksi QR code dan barcode secara real-time dari webcam menggunakan:
- `opencv-python` untuk akses kamera dan visualisasi
- `pyzbar` untuk decode QR/barcode
- `numpy` untuk manipulasi titik poligon

> Tested on: **Windows 10/11 + Python 3.11.9**.
> Versi Python lain seperti 3.12, 3.13, atau 3.14 bisa menimbulkan error DLL `libzbar` di Windows, jadi disarankan menggunakan **Python 3.11**.

---

## Prerequisites

Pastikan komponen berikut sudah terpasang sebelum menjalankan project:

1. **Python 3.11.x (64-bit)**

   Install lewat PowerShell:
   ```powershell
   winget install Python.Python.3.11
   ```

   Setelah selesai, tutup dan buka ulang PowerShell supaya PATH baru terbaca.

   Alternatif manual: <https://www.python.org/downloads/release/python-3119/>

   Saat install manual, centang `Add Python 3.11 to PATH`.

   Verifikasi:
   ```powershell
   py -0p
   ```

   Pastikan ada Python `3.11` yang terdeteksi.

2. **Microsoft Visual C++ 2013 Redistributable (x64)**

   Download: <https://aka.ms/highdpimfc2013x64enu>

   Komponen ini sering dibutuhkan oleh `pyzbar` untuk membaca `libzbar-64.dll`.

3. **Microsoft Visual C++ 2015-2022 Redistributable (x64)**

   Download: <https://aka.ms/vs/17/release/vc_redist.x64.exe>

Setelah install komponen di atas, restart laptop agar runtime DLL terbaca dengan benar.

---

## Setup

1. Buka PowerShell di folder project, lalu buat virtual environment menggunakan Python 3.11:
   ```powershell
   py -3.11 -m venv .venv311
   ```

2. Aktifkan virtual environment:
   ```powershell
   .\.venv311\Scripts\Activate.ps1
   ```

   Pastikan muncul `(.venv311)` di awal prompt. Cek versi Python:
   ```powershell
   python -V
   ```

   Output harus menampilkan `Python 3.11.x`.

3. Install dependency:
   ```powershell
   pip install -r requirements.txt
   ```

4. Smoke test untuk memastikan `pyzbar` bisa di-load:
   ```powershell
   python -c "from pyzbar.pyzbar import decode; print('pyzbar OK')"
   ```

   Kalau muncul `pyzbar OK`, environment sudah siap. Kalau error, lihat bagian **Troubleshooting**.

---

## Run

### Basic detector

Menampilkan nilai asli QR code atau barcode yang terbaca.

```powershell
python QrBarTest.py
```

### Authorization detector

Menampilkan status `Authorized` atau `Un-Authorized` berdasarkan daftar kode valid di `myDataFile.text`.

```powershell
python QrCodeProject.py
```

Tekan `q` atau `Esc` untuk keluar dari window kamera.

---

## Customize

- Edit daftar kode valid di `myDataFile.text`.
- Isi satu kode per baris, tanpa tanda kutip.
- Jika ada lebih dari satu kamera, ubah `cv2.VideoCapture(0)` menjadi `cv2.VideoCapture(1)` atau index kamera lain di `QrBarTest.py` / `QrCodeProject.py`.
- Resolusi kamera dapat diubah pada bagian:
  ```python
  cap.set(3, 640)
  cap.set(4, 480)
  ```

---

## Troubleshooting

### 1. `FileNotFoundError: Could not find module 'libzbar-64.dll'`

Penyebab paling umum: VC++ runtime belum lengkap.

- Install VC++ 2013 (x64): <https://aka.ms/highdpimfc2013x64enu>
- Install VC++ 2015-2022 (x64): <https://aka.ms/vs/17/release/vc_redist.x64.exe>
- Restart laptop, lalu ulangi smoke test.

### 2. `No suitable Python runtime found`

Error ini biasanya muncul saat menjalankan:

```powershell
py -3.11 -m venv .venv311
```

Artinya Python 3.11 belum terpasang atau belum terdeteksi oleh launcher Python.

- Install lewat PowerShell:
  ```powershell
  winget install Python.Python.3.11
  ```
- Tutup dan buka ulang PowerShell.
- Cek interpreter yang terdeteksi:
  ```powershell
  py -0p
  ```

### 3. `ModuleNotFoundError: No module named 'pyzbar'`

Virtual environment belum aktif atau dependency belum di-install.

```powershell
.\.venv311\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 4. PowerShell menolak menjalankan `Activate.ps1`

Jika muncul pesan `running scripts is disabled on this system`, buka PowerShell dengan **Run as Administrator**, lalu jalankan:

```powershell
Set-ExecutionPolicy RemoteSigned
```

Pilih `Y`, lalu aktifkan ulang virtual environment.

### 5. Kamera tidak terbuka atau window hitam

- Tutup aplikasi lain yang sedang memakai webcam, seperti Zoom, OBS, browser, atau aplikasi meeting.
- Coba ubah index kamera dari `0` menjadi `1` di `cv2.VideoCapture(0)`.

### 6. Selalu `Un-Authorized` walaupun kode sudah didaftarkan

- Pastikan teks di `myDataFile.text` persis sama dengan hasil scan.
- Jangan tambahkan tanda kutip.
- Jangan tambahkan spasi di awal atau akhir kode.
- Jalankan `python QrBarTest.py` untuk melihat nilai asli yang terbaca, lalu masukkan nilai tersebut ke `myDataFile.text`.

---

## Notes for Assignment

- `QrBarTest.py`: versi deteksi standar yang menampilkan nilai kode asli.
- `QrCodeProject.py`: versi validasi authorization yang menampilkan `Authorized` atau `Un-Authorized`.
- Untuk demo, siapkan dua QR/barcode:
  - satu berisi nilai yang sudah ada di `myDataFile.text`, hasilnya hijau `Authorized`
  - satu berisi nilai acak atau tidak terdaftar, hasilnya merah `Un-Authorized`
