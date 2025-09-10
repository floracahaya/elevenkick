Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

- Tautan menuju aplikasi PWS yang sudah di-deploy: https://flora-cahaya-elevenkick.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
1) Pertama, saya membuat direktori bernama elevenkick, lalu membuat dan mengaktifkan virtual environment dengan perintah python -m venv env dan env\Scripts\activate. Setelah itu, saya menyiapkan file requirements.txt yang berisi dependencies (seperti Django, gunicorn, whitenoise, psycopg2-binary, dll.) dan menginstalnya menggunakan pip install -r requirements.txt. Selanjutnya, saya membuat proyek Django bernama elevenkick dengan django-admin startproject elevenkick .. Saya juga membuat file .env (untuk database SQLite di lokal) dan .env.prod (untuk PostgreSQL di PWS), lalu menghubungkannya dengan settings.py. Setelah migrasi database dijalankan dan python manage.py runserver berhasil, halaman roket Django tampil di http://localhost:8000/ sebagai tanda proyek berjalan dengan baik.
2) Saya membuat aplikasi baru bernama main dengan python manage.py startapp main, kemudian menambahkannya ke INSTALLED_APPS di settings.py.
3) Di dalam folder main, saya membuat file urls.py yang berisi route ke fungsi show_main.
4) Pada models.py, saya membuat model bernama Product dengan atribut seperti name, price, description, thumbnail, category, dan is_featured, lalu melakukan migrasi database.
5) Di views.py, saya menuliskan fungsi show_main yang mengirim data berupa nama aplikasi, nama saya, dan kelas ke template HTML agar bisa ditampilkan secara dinamis.
6) Pada urls.py di proyek utama, saya menambahkan path('', include('main.urls')), sehingga halaman utama dapat diakses melalui http://localhost:8000/.
7) Untuk deployment ke PWS, saya login dengan SSO, membuat proyek baru, lalu menambahkan environment variables dari .env.prod. Setelah itu, saya memperbarui ALLOWED_HOSTS dengan URL PWS. Terakhir, saya melakukan git add, git commit, dan git push pws master. Jika status sudah Running, maka aplikasi dapat diakses melalui URL PWS yang telah diberikan.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
- Bagan (canva): https://www.canva.com/design/DAGygUExUm4/11zzEH2XBNxg6ds4s6PHPw/edit?utm_content=DAGygUExUm4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
- Penjelasan: Pada bagan tersebut, urls.py berkaitan dengan views.py, karena mengarahkan request dari pengguna ke fungsi view yang sesuai. Selanjutnya, views.py berkaitan dengan models.py untuk mengambil atau mengolah data dari database. Data yang sudah diproses kemudian dikirim oleh views.py ke HTML (template) agar dapat ditampilkan. Terakhir, HTML berkaitan dengan pengguna karena menjadi respons akhir yang tampil di browser. Dengan demikian, urls.py, views.py, models.py, dan HTML saling berkaitan dalam memproses request hingga menghasilkan tampilan web.

3. Jelaskan peran settings.py dalam proyek Django!
Jawab:
settings.py adalah pusat konfigurasi proyek Django. Hampir semua perilaku aplikasi (database, template, static files, keamanan, dll.) dikontrol dari settings.py. Berikut penjelasan fungsi-fungsi utamanya, antara lain:
- Keamanan (SECRET_KEY, DEBUG, ALLOWED_HOSTS) → ngatur kunci rahasia, apakah error detail ditampilkan, dan siapa saja yang boleh akses aplikasi.
- INSTALLED_APPS → daftar aplikasi yang dipakai di project (misalnya main, admin, dll.).
- MIDDLEWARE → lapisan “pengawas” yang ngecek request & response (kayak login session, CSRF, dll.).
- ROOT_URLCONF & WSGI_APPLICATION → ngatur pintu masuk URL ke views dan cara aplikasi dijalankan di server.
- TEMPLATES → ngatur di mana Django cari file HTML buat ditampilkan.
- DATABASES → ngatur database yang dipakai (SQLite di laptop, PostgreSQL di server).
- STATIC_URL → ngatur file statis kayak CSS, JS, gambar.
- Bahasa & waktu (LANGUAGE_CODE, TIME_ZONE) → ngatur bahasa & zona waktu.
- Validasi password & default primary key → ngatur aturan keamanan password dan tipe ID di database.

4. Bagaimana cara kerja migrasi database di Django?
Jawab:
Migrasi database di Django adalah proses untuk nyamain struktur database dengan model yang kita buat di kode Python. Cara kerjanya, yaitu ketika kita buat atau ubah model di models.py, Django mencatat perubahan itu dalam bentuk file migrasi dengan perintah makemigrations. File migrasi ini berisi instruksi bagaimana database harus diubah. Setelah itu, perintah migrate bakal ngejalanin instruksi tersebut ke database, misalnya buat tabel baru, nambah kolom, atau ubah struktur tabel. Django juga simpan riwayat migrasi agar tiap perubahan tercatat dan tidak dijalankan dua kali. Dengan cara ini, kita gaperlu nulis perintah SQL manual, karena Django yang menerjemahkannya ke dalam perubahan di database.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawab:
Django dijadikan permulaan pembelajaran pengembangan perangkat lunak, karena framework ini terstruktur, lengkap, dan “batteries included”. Django sudah menyediakan banyak fitur dasar, seperti autentikasi, manajemen database, dan routing, sehingga kita bisa fokus memahami konsep inti pengembangan perangkat lunak tanpa harus membangun semuanya dari nol. Selain itu, Django menerapkan pola MVC (Model-View-Controller) yang membantu memahami pemisahan logika, data, dan tampilan serta memiliki dokumentasi yang baik.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawab:
Masih ada beberapa step yang kurang jelas dan terkadang membuat salah paham. Tetapi, secara keseluruhan, sudah bagus dan membantu saya dalam melaksanakan tutorial.