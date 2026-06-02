# How to Detect QRCode and BarCode using OpenCV in Python

Project ini mendeteksi QR code dan barcode secara real-time dari webcam menggunakan:
- `opencv-python` untuk akses kamera dan visualisasi
- `pyzbar` untuk decode QR/barcode
- `numpy` untuk manipulasi titik poligon

> Tested on: **Windows 10/11 + Python 3.11.9**.
> Versi Python lain (3.12 / 3.13 / 3.14) bisa menimbulkan error DLL `libzbar` di Windows, jadi **gunakan Python 3.11**.

---

## Prerequisites (Windows)

Pastikan **3 hal** ini sudah terpasang di laptop kamu sebelum menjalankan project:

1. **Python 3.11.x (64-bit)**
   - Cara paling gampang lewat PowerShell:
     ```powershell
     winget install Python.Python.3.11
     ```
     Setelah selesai, **tutup dan buka ulang PowerShell** supaya PATH baru terbaca.
   - Alternatif manual via installer: <https://www.python.org/downloads/release/python-3119/>
     (saat install, **centang** `Add Python 3.11 to PATH`).
   - Verifikasi:
     ```powershell
     py -0p
     ```
     Harus muncul `3.11`.

2. **Microsoft Visual C++ 2013 Redistributable (x64)** — paling sering jadi penyebab error `libzbar-64.dll`.
   - Download: <https://aka.ms/highdpimfc2013x64enu>

3. **Microsoft Visual C++ 2015–2022 Redistributable (x64)**
   - Download: <https://aka.ms/vs/17/release/vc_redist.x64.exe>

> Setelah install ketiganya, **restart laptop** sekali agar runtime DLL terbaca dengan benar.

---

## Project Structure

```text
Project_N2_QRCode/
├── QrBarTest.py
├── QrCodeProject.py
├── myDataFile.text
└── requirements.txt
```

---

## Setup

> Pastikan kamu sudah menyelesaikan bagian **Prerequisites** di atas.

1. Clone / copy project ke folder yang **tidak terlalu dalam** (hindari banyak spasi/karakter aneh kalau bisa).

2. Buka PowerShell di folder project, lalu buat virtual environment pakai **Python 3.11**:
   ```powershell
   py -3.11 -m venv .venv311
   ```

3. Aktifkan virtual environment:
   ```powershell
   .\.venv311\Scripts\Activate.ps1
   ```
   Pastikan keluar `(.venv311)` di awal prompt. Cek versi Python:
   ```powershell
   python -V
   ```
   Harus menampilkan `Python 3.11.x`.

4. Install dependency:
   ```powershell
   pip install -r requirements.txt
   ```

5. Smoke test, pastikan `pyzbar` bisa di-load:
   ```powershell
   python -c "from pyzbar.pyzbar import decode; print('pyzbar OK')"
   ```
   Kalau muncul `pyzbar OK`, environment kamu siap. Kalau error, lihat bagian **Troubleshooting**.

---

## Run

### 1) Basic detector (tampil nilai kode asli)
```powershell
python QrBarTest.py
```

### 2) Authorization detector (Authorized / Un-Authorized)
```powershell
python QrCodeProject.py
```

Tekan `Ctrl+C` di terminal untuk keluar (atau tutup paksa window python).

---

## Customize

- Edit daftar code valid di `myDataFile.text` (satu code per baris, tanpa tanda kutip).
- Ganti resolusi atau indeks kamera: ubah pada script `QrBarTest.py` / `QrCodeProject.py` di bagian `cv2.VideoCapture(0)`. Ubah `0` menjadi `1` atau index lainnya jika ada lebih dari 1 kamera.

---

## Troubleshooting (Windows)

### 1. `FileNotFoundError: Could not find module 'libzbar-64.dll' (or one of its dependencies)`
Penyebab: VC++ runtime belum lengkap.
- Pastikan **VC++ 2013 (x64)** sudah terpasang: <https://aka.ms/highdpimfc2013x64enu>
- Pastikan **VC++ 2015–2022 (x64)** juga terpasang: <https://aka.ms/vs/17/release/vc_redist.x64.exe>
- Restart laptop, ulangi smoke test.

### 2. `No suitable Python runtime found` saat `py -3.11 -m venv ...`
Python 3.11 belum terpasang.
- Install paling cepat lewat PowerShell:
  ```powershell
  winget install Python.Python.3.11
  ```
  Tutup & buka ulang PowerShell setelah install selesai.
- Alternatif: installer manual <https://www.python.org/downloads/release/python-3119/> (centang *Add Python 3.11 to PATH*).
- Cek interpreter yang terdeteksi: `py -0p`.

### 3. `ModuleNotFoundError: No module named 'pyzbar'`
Virtual environment belum aktif atau `pip install` belum dijalankan.
- Aktifkan dulu: `.\.venv311\Scripts\Activate.ps1`
- Lalu: `pip install -r requirements.txt`

### 4. PowerShell menolak menjalankan `Activate.ps1`
Pesan: `running scripts is disabled on this system`.
- Buka PowerShell **Run as Administrator**, jalankan:
  ```powershell
  Set-ExecutionPolicy RemoteSigned
  ```
- Pilih `Y`, lalu ulang aktivasi venv.

### 5. Kamera tidak terbuka / window hitam
- Tutup aplikasi lain yang mungkin pakai webcam (Zoom, OBS, browser, dll).
- Coba index kamera lain dengan mengubah `cv2.VideoCapture(0)` menjadi `cv2.VideoCapture(1)` di `QrBarTest.py` / `QrCodeProject.py`.

### 6. Selalu `Un-Authorized` walau kode sudah didaftarkan
- Pastikan teks di `myDataFile.text` **persis sama** dengan hasil scan (tanpa tanda kutip, tanpa spasi tambahan di awal/akhir).
- Jalankan `python QrBarTest.py` untuk melihat nilai asli yang terbaca, baru paste ke `myDataFile.text`.

---

## Notes for Assignment

- `QrBarTest.py`: versi deteksi standar (menampilkan nilai kode asli).
- `QrCodeProject.py`: versi validasi authorization (Authorized / Un-Authorized).
- Untuk demo, siapkan **dua QR/barcode**:
  - 1 berisi nilai yang sudah ada di `myDataFile.text` → akan jadi hijau **Authorized**.
  - 1 berisi nilai acak / tidak terdaftar → akan jadi merah **Un-Authorized**.
