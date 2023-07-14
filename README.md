## Backlink Klik URL

Repository ini berisi kode Python untuk mengklik tautan (link) pada halaman web menggunakan Selenium. Kode ini dapat membantu Anda secara otomatis mengklik tautan dengan kata kunci tertentu pada halaman web yang ditentukan.

## *Requirement*

* Python 3.9
* openpyxl
* requests
* BeautifulSoup
* selenium
* Chrome WebDriver (sesuai dengan versi browser Chrome Anda)

## Fitur

* Mode *Headless*

## *Installation*

Via Git

``` git clone https://github.com/dzulfikarsa/backlink_click_url ```

## *Download ZIP*

[Link](https://github.com/dzulfikarsa/backlink_click_url/archive/refs/heads/main.zip)

Buka terminal atau *command prompt*
Arahkan ke direktori *project* dengan menjalankan perintah berikut :

``` cd backlink_click_url ```

Install requirement 

``` pip install -r requirements.txt ```


## Penggunaan

1. Pastikan Anda telah menginstal Python di komputer Anda.
2. Instal library yang diperlukan dengan menjalankan perintah berikut di terminal atau command prompt :

   ```pip install openpyxl requests BeautifulSoup selenium```
   
4. Unduh file backlink_click_url.py dari repository ini.
5. Ubah nilai variabel file_path dengan path file Excel yang berisi URL yang ingin diklik.
6. Ubah nilai variabel url_column dengan nama kolom yang berisi URL pada file Excel.
7. Ubah daftar anchor_text_list sesuai dengan kata kunci tautan yang ingin Anda klik.
8. Jalankan skrip Python dengan menjalankan perintah berikut di terminal atau command prompt :
   
   ```python backlink_click_url.py```
   
Skrip akan membuka browser dalam mode headless dan mengklik tautan yang sesuai dengan kata kunci yang telah Anda tentukan. Hasil dari klik tautan akan ditulis ke dalam file Excel output.

## Tambahan
Dalam repository ini, saya juga menyertakan file Link V1_24.xlsx yang merupakan contoh file Excel dengan data URL untuk diuji. Anda dapat menggunakan file ini untuk mencoba skrip dengan cepat. Selain itu, skrip ini juga menggunakan Selenium untuk mengendalikan browser dan melakukan klik tautan secara otomatis.

Selamat mencoba! Jika Anda memiliki pertanyaan atau masalah, jangan ragu untuk mengajukan pertanyaan atau membuat issue di repository ini. Terima kasih!
