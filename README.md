# backlink_click_url

Repository ini berisi kode Python untuk mengklik tautan (link) pada halaman web menggunakan Selenium. Kode ini dapat membantu Anda secara otomatis mengklik tautan dengan kata kunci tertentu pada halaman web yang ditentukan.

## Penggunaan

1. Pastikan Anda telah menginstal Python di komputer Anda.
2. Instal library yang diperlukan dengan menjalankan perintah berikut di terminal atau command prompt:
   ```pip install openpyxl selenium```
3. Unduh file backlink_click_url.py dari repository ini.
4. Ubah nilai variabel file_path dengan path file Excel yang berisi URL yang ingin diklik.
5. Ubah nilai variabel url_column dengan nama kolom yang berisi URL pada file Excel.
6. Ubah daftar anchor_text_list sesuai dengan kata kunci tautan yang ingin Anda klik.
7. Jalankan skrip Python dengan menjalankan perintah berikut di terminal atau command prompt:
   ```python backlink_click_url.py```
   
Script akan membuka browser dalam mode headless (tanpa tampilan grafis) dan mengklik tautan yang sesuai dengan kata kunci yang telah Anda tentukan. Hasil dari klik tautan akan ditulis ke dalam file report.txt. Jika tautan tidak ditemukan atau gagal diklik, URL tersebut akan ditulis ke dalam file report_gagal.txt.

## Tambahan
Dalam repository ini, saya juga menyertakan file dataset.xlsx yang merupakan contoh file Excel dengan data URL untuk diuji. Anda dapat menggunakan file ini untuk mencoba skrip dengan cepat. Selain itu, skrip ini juga menggunakan Selenium untuk mengendalikan browser dan melakukan klik tautan secara otomatis.

Selamat mencoba! Jika Anda memiliki pertanyaan atau masalah, jangan ragu untuk mengajukan pertanyaan atau membuat issue di repository ini. Terima kasih!
