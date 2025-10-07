--> TUGAS 2

Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

- Tautan menuju aplikasi PWS yang sudah di-deploy: https://flora-cahaya-elevenkick.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
1) Pertama, saya membuat direktori bernama elevenkick, lalu membuat dan mengaktifkan virtual environment dengan perintah python -m venv env dan env\Scripts\activate. Setelah itu, saya menyiapkan file requirements.txt yang berisi dependencies (seperti Django, gunicorn, whitenoise, psycopg2-binary, dll.) dan menginstalnya menggunakan pip install -r requirements.txt. Selanjutnya, saya membuat proyek Django bernama elevenkick dengan django-admin startproject elevenkick .. Saya juga membuat file .env (untuk database SQLite di lokal) dan .env.prod (untuk PostgreSQL di PWS), lalu menghubungkannya dengan settings.py. Setelah migrasi database dijalankan dan python manage.py runserver berhasil, halaman roket Django tampil di http://localhost:8000/ sebagai tanda proyek berjalan dengan baik.
2) Saya membuat aplikasi baru bernama main dengan python manage.py startapp main, kemudian menambahkannya ke INSTALLED_APPS di settings.py.
3) Di dalam folder main, saya membuat file urls.py yang berisi route ke fungsi show_main.
4) Pada models.py, saya membuat model bernama Product dengan atribut seperti name, price, description, thumbnail, category, dan is_featured, lalu melakukan migrasi database.
5) Di views.py, saya menuliskan fungsi show_main yang mengirim data berupa nama aplikasi, nama saya, dan kelas ke template HTML agar bisa ditampilkan secara dinamis.
6) Pada urls.py di proyek utama, saya menambahkan path('', include('main.urls')), sehingga halaman utama bisadiakses melalui http://localhost:8000/.
7) Untuk deployment ke PWS, saya login dengan SSO, membuat proyek baru, lalu menambahkan environment variables dari .env.prod. Setelah itu, saya memperbarui ALLOWED_HOSTS dengan URL PWS. Terakhir, saya melakukan git add, git commit, dan git push pws master. Jika status sudah Running, maka aplikasi bisadiakses melalui URL PWS yang telah diberikan.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawab:
- Bagan (canva): https://www.canva.com/design/DAGygUExUm4/11zzEH2XBNxg6ds4s6PHPw/edit?utm_content=DAGygUExUm4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
- Penjelasan: Pada bagan tersebut, urls.py berkaitan dengan views.py, karena mengarahkan request dari pengguna ke fungsi view yang sesuai. Selanjutnya, views.py berkaitan dengan models.py untuk mengambil atau mengolah data dari database. Data yang sudah diproses kemudian dikirim oleh views.py ke HTML (template) agar bisaditampilkan. Terakhir, HTML berkaitan dengan pengguna karena menjadi respons akhir yang tampil di browser. Dengan demikian, urls.py, views.py, models.py, dan HTML saling berkaitan dalam memproses request hingga menghasilkan tampilan web.

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

--> TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab:
Data delivery adalah proses pengiriman data dari sumber ke tujuan secara cepat, efisien, dan aman, baik melalui batch maupun real-time. Data delivery diperlukan dalam pengimplementasian sebuah platform, karena menjadi tulang punggung komunikasi antar komponen, misalnya antara frontend dan backend atau antar layanan dalam arsitektur microservices. Dengan adanya mekanisme pengiriman data seperti API yang menggunakan format JSON atau XML, platform bisamemastikan pertukaran informasi berjalan konsisten, terstruktur, dan bisadipahami oleh sistem lain. Selain itu, data delivery juga mendukung skalabilitas, menjaga integritas data, serta memungkinkan integrasi dengan layanan eksternal maupun pihak ketiga. Tanpa adanya proses ini, platform tidak bisaberjalan secara optimal karena data tidak bisaditeruskan dengan lancar untuk mendukung fungsi bisnis maupun pengalaman pengguna.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawab:
JSON (JavaScript Object Notation) dan XML (eXtensible Markup Language) sama-sama digunakan untuk pertukaran data, tetapi keduanya punya kelebihan dan kekurangan masing-masing. JSON lebih ringkas dan mudah dibaca oleh manusia, serta langsung bisa digunakan di JavaScript tanpa konfigurasi tambahan. Karena ukurannya lebih kecil, data yang dikirim lebih cepat sampai dan efisien. Banyak framework dan library modern juga mendukung JSON, sehingga penggunaannya lebih praktis. Kekurangannya, JSON kurang cocok untuk dokumen yang sangat kompleks, karena tidak punya fitur, seperti namespace atau mixed content, meskipun ada JSON Schema untuk membantu validasi. XML lebih kuat untuk dokumen yang kompleks karena mendukung namespace, atribut, dan bisa divalidasi dengan skema yang ketat (XSD). Namun, XML biasanya lebih panjang, lebih berat saat diproses, dan tidak sepraktis JSON di web modern.

-> Kesimpulan:
JSON lebih baik untuk kebanyakan aplikasi modern, karena lebih ringan, cepat, mudah dibaca, dan langsung kompatibel dengan JavaScript, sehingga membuat pengembangan web lebih efisien. XML masih berguna di beberapa kasus khusus, seperti dokumen kompleks atau sistem lama, tetapi secara umum JSON jauh lebih populer dibandingkan XML di era web dan API modern.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawab:
Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang di-submit pengguna sudah sesuai dengan aturan validasi yang ditentukan. Jika is_valid() mengembalikan nilai True, berarti seluruh field telah diisi dengan benar (misalnya field angka diisi dengan angka, field wajib tidak kosong, atau format email sesuai). Jika False, Django akan menyimpan pesan error pada form sehingga bisa ditampilkan kembali kepada pengguna. Method ini penting, karena memastikan hanya data yang valid yang boleh diproses lebih lanjut atau disimpan ke database, sehingga menjaga integritas data sekaligus mencegah error maupun potensi kerusakan pada aplikasi.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang bisaterjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut bisadimanfaatkan oleh penyerang?
Jawab:
csrf_token dibutuhkan dalam form Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), yaitu serangan di mana penyerang membuat pengguna yang sedang login tanpa sadar mengirimkan request berbahaya ke aplikasi, misalnya transfer uang, penghapusan data, atau pembelian barang. Jika form tidak menggunakan csrf_token, penyerang bisamembuat form palsu di website lain dan memanfaatkan sesi login pengguna agar request tersebut dianggap sah oleh server. Dengan adanya csrf_token, setiap form akan memiliki kode unik yang terikat pada session pengguna, sehingga request palsu yang tidak memiliki token valid akan otomatis ditolak. Hal ini membuat aplikasi lebih aman dari eksploitasi yang memanfaatkan identitas pengguna.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
1) Pertama, aku membuat empat fungsi baru di views.py. Tujuannya supaya data produk yang tersimpan di database bisa diakses dalam format XML dan JSON. Ada dua jenis untuk masing-masing format: satu untuk menampilkan semua data, dan satu lagi untuk menampilkan data berdasarkan ID tertentu. Jadi misalnya kalau aku buka /products/json/, maka semua produk keluar dalam format JSON. Sedangkan kalau aku buka /products/json/1/, maka hanya produk dengan ID = 1 saja yang ditampilkan dalam format JSON. Hal yang sama berlaku juga untuk XML. Fungsi ini dibuat dengan memanfaatkan serializers dari Django.
2) Setelah fungsi views selesai, aku sambungkan ke routing di urls.py pada direktori main. Di sana aku tambahkan path:
path('products/json/', products_json, name='products_json'),
path('products/json/<int:pk>/', product_json_by_id, name='product_json_by_id'),
path('products/xml/', products_xml, name='products_xml'),
path('products/xml/<int:pk>/', product_xml_by_id, name='product_xml_by_id'),
Dengan begitu, setiap fungsi yang ada di views.py bisa dipanggil lewat browser atau Postman menggunakan URL tertentu. Jadi lebih jelas dan terstruktur.
3) Berikutnya, aku membuat halaman untuk menampilkan daftar produk. Halaman ini berupa template product_list.html yang berisi semua produk dalam bentuk list. Di setiap produk ada tombol Detail untuk melihat informasi lengkap produk tersebut, dan di bagian atas ada tombol Add untuk menambahkan produk baru. Dengan begitu, user bisa melihat data yang sudah ada sekaligus menambahkan data baru.
4) Supaya user bisa menambahkan data, aku membuat file forms.py yang berisi ProductForm. Form ini mengambil field-field dari model Product (seperti name, price, description, thumbnail, category, dan is_featured). Lalu aku buat template product_form.html untuk menampilkan form input. Ketika tombol Add diklik, user akan diarahkan ke halaman form ini. Setelah data diisi dan disubmit, produk otomatis tersimpan ke database. Jangan lupa sebelumnya dilakukan makemigrations dan migrate supaya model benar-benar tersimpan di database.
5) Untuk detail produk, aku membuat fungsi product_detail di views.py. Fungsinya mengambil data produk berdasarkan pk menggunakan get_object_or_404(Product, pk=pk). Kemudian data produk tersebut dikirimkan ke template product_detail.html. Di halaman detail, aku menampilkan informasi lengkap seperti nama produk, harga, deskripsi, kategori, thumbnail, dan status unggulan. Di bagian bawah halaman detail, aku tambahkan tombol Back to Product List supaya user bisa kembali ke daftar produk.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Jawab:
Tidak ada. Tutorial sudah memiliki intruksi yang jelas dan arahan dari tim asdos juga sudah sangat membantu.

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
Jawab:
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)

--> TUGAS 4

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Jawab:
AuthenticationForm adalah form bawaan dari Django yang dipakai untuk proses autentikasi (login) pengguna. Form ini otomatis menyediakan input username dan password, lalu melakukan pemeriksaan, seperti apakah akun benar-benar ada, password sesuai, dan status user masih aktif. Karena sudah terintegrasi langsung dengan sistem autentikasi Django (django.contrib.auth), developer tidak perlu membuat logika login dasar dari nol.
- Kelebihan:
1) Sudah menyiapkan validasi umum (cek username, password, status user aktif) tanpa perlu kode tambahan.
2) Mengikuti standar Django, sehingga gampang dipakai bareng sistem session, middleware, dan view login bawaan.
3) Mengurangi duplikasi kode, karena logika login dasar sudah ditangani otomatis.
- Kekurangan:
1) Cara inisialisasi form sedikit membingungkan bagi pemula (harus diberikan request dan data dengan benar).
2) Pesan error bawaan cenderung generik, misalnya hanya bilang “username atau password salah” tanpa detail. Kalau butuh pesan khusus, perlu di-override.
3) Tidak fleksibel untuk kebutuhan tertentu, misalnya login pakai email atau sistem autentikasi kustom. Pada kasus itu form perlu dimodifikasi agar cocok dengan model user yang digunakan.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?
Jawab:
Autentikasi adalah proses untuk memastikan identitas seorang pengguna, apakah benar orang tersebut adalah pemilik akun yang sah. Contohnya, login dengan username dan password atau verifikasi identitas. Di Django, autentikasi ditangani oleh modul django.contrib.auth yang menyediakan model User serta fungsi, seperti authenticate(), login(), dan logout(). Selain itu, AuthenticationMiddleware akan otomatis mengaitkan setiap request dengan user yang sedang login, atau menganggapnya sebagai anonymous user jika belum masuk. Otorisasi, di sisi lain, merupakan langkah lanjutan setelah autentikasi. Tahap ini menentukan apakah pengguna yang sudah diverifikasi punya izin buat melakukan tindakan tertentu. Misalnya, apakah seorang user diperbolehkan menghapus postingan, mengakses dashboard admin, atau mengubah data. Django menyediakan sistem permissions dan groups untuk atur hal ini. Permissions atur aksi yang bisa dilakukan pengguna (tambah, ubah, hapus), sedangkan groups memudahkan pengelolaan izin untuk banyak user sekaligus. Untuk membatasi akses pada view, Django juga menyediakan dekorator, seperti login_required dan mixin, seperti PermissionRequiredMixin.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Jawab:
- Cookies adalah potongan data kecil yang ditempatkan di browser pengguna untuk menyimpan informasi tentang status aplikasi web. Keunggulan cookies, yaitu tidak menambah beban penyimpanan di server karena datanya ada di sisi klien, bisa tetap tersimpan walaupun browser ditutup jika ada pengaturan masa berlaku, serta praktis untuk menyimpan preferensi sederhana seperti pilihan bahasa, tema, atau login otomatis. Meski begitu, kapasitas cookies sangat terbatas (umumnya hanya beberapa KB), rentan diubah atau dicegat jika tidak diamankan, dan juga bisa dihapus/blokir pengguna sehingga tidak selalu bisa dijadikan sumber utama.
- Session adalah metode penyimpanan data di sisi server, sementara browser hanya memegang session ID untuk menghubungkan dengan data user di server. Kelebihannya, data sensitif lebih terlindungi karena tidak berada di browser, kapasitas penyimpanan bisa lebih besar, serta sesuai untuk kebutuhan kompleks seperti autentikasi login, keranjang belanja, atau pengaturan hak akses. Kekurangannya, server jadi punya beban ekstra untuk menyimpan data semua pengguna, performa bisa menurun kalau jumlah user banyak, dan data session bisa hilang jika server restart atau sesi kedaluwarsa bila tidak ada konfigurasi khusus untuk mempertahankannya.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Jawab:
Secara default, cookies dalam web development tidak bisa dianggap sepenuhnya aman karena penyimpanannya berada di sisi klien (browser). Hal ini membuatnya rentan terhadap serangan, misalnya pencurian data atau modifikasi langsung oleh pengguna. Jika atribut keamanan, seperti HttpOnly, Secure, atau SameSite tidak diaktifkan, maka cookie bisa terekspos pada skrip berbahaya atau bahkan terkirim lewat koneksi yang tidak terenkripsi. Karena itu, informasi penting, seperti session ID atau token login harus selalu dilindungi dengan konfigurasi keamanan yang tepat. Di Django, framework ini sudah menambahkan perlindungan dasar secara otomatis. Sebagai contoh, cookie sesi ditandai dengan flag HttpOnly sehingga tidak bisa diakses oleh JavaScript. Django juga menyediakan opsi konfigurasi, seperti SESSION_COOKIE_SECURE agar cookie hanya dikirim lewat HTTPS, dan SESSION_COOKIE_SAMESITE untuk mencegah pengiriman cookie dalam permintaan lintas domain yang berpotensi menimbulkan serangan CSRF. Dengan adanya pengaturan ini, Django membantu meminimalisir risiko penggunaan cookies, meskipun developer tetap perlu menyesuaikan konfigurasi tambahan sesuai kebutuhan aplikasinya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab:
1) Proses autentikasi di Django dimulai dari fungsi register, yang memanfaatkan UserCreationForm untuk membuat akun baru. Jika form lolos validasi, akun akan disimpan lalu pengguna dialihkan ke halaman login. Pada fungsi login_user, AuthenticationForm digunakan untuk memverifikasi kombinasi username dan password. Jika benar, maka login(request, user) dijalankan sehingga Django membuat session sekaligus menyimpan cookie, seperti last_login dan username, yang kemudian bisa ditampilkan di halaman utama. Untuk keluar dari akun, fungsi logout_user memanggil logout(request) agar session terhapus, lalu cookie terkait juga dihapus sebelum pengguna diarahkan kembali ke halaman login. Agar hanya pengguna terautentikasi yang bisa mengakses halaman tertentu, dekorator @login_required(login_url='/login') ditambahkan pada view (misalnya show_main atau show_product), sehingga pengguna yang belum login otomatis diarahkan ke halaman login.
2) Jalankan aplikasi dengan perintah python manage.py runserver dan akses melalui localhost. Pada halaman login, pilih opsi registrasi untuk buat dua akun baru, lalu kembali ke halaman login. Selanjutnya, login menggunakan akun pertama, kemudian tambahkan tiga produk berbeda melalui tombol Add Product. Setelah itu, logout dari akun pertama dan ulangi proses login dengan akun kedua untuk melakukan hal serupa.
3) Relasi antara produk dan pengguna dibangun dengan menambahkan field user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) pada models.py. Field ini menyatakan bahwa setiap produk terhubung dengan satu objek User, yaitu pemilik produk tersebut. Karena memakai ForeignKey, maka relasi yang terbentuk adalah many-to-one, artinya satu pengguna bisa punya banyak produk. Argumen on_delete=models.CASCADE memastikan bahwa apabila pengguna dihapus, seluruh produk miliknya juga akan ikut terhapus, sehingga integritas data tetap terjaga.
4) Untuk menampilkan informasi pengguna yang sedang login sekaligus memanfaatkan cookie, beberapa langkah dilakukan. Pertama, tambahkan data username ke dalam context, dengan nilai diambil dari cookie username, atau fallback ke request.user.username jika cookie belum ada. Kedua, setelah login berhasil, simpan username ke dalam cookie menggunakan response.set_cookie('username', user.username), agar bisa dipanggil kembali di halaman utama. Ketiga, saat logout, cookie tersebut dihapus dengan response.delete_cookie('username'). Terakhir, di template utama, tampilkan sapaan personal dengan menggunakan {{ username }}. Dengan mekanisme ini, aplikasi bisa memberikan pengalaman lebih interaktif dan memastikan cookie dikelola sesuai status login maupun logout.

--> TUGAS 5
1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jawab:
CSS selector untuk suatu elemen HTML adalah aturan yang digunakan untuk memilih elemen tertentu dalam halaman web agar bisa diberikan style. Satu elemen HTML bisa dipengaruhi oleh banyak selector sekaligus, misalnya melalui tag name, class, ID, atau bahkan inline style. Ketika ada beberapa aturan yang bertabrakan (misalnya sama-sama mengatur warna teks), browser akan menentukan prioritas berdasarkan CSS specificity. Urutan Prioritas CSS Selector (dari paling rendah ke paling tinggi), yaitu:
1) Selector universal (*), nilai specificity paling rendah (sering dianggap 0).
2) Element selector / pseudo-elemen, bobotnya rendah, seperti div, p, atau h1, dan nilai specificity-nya adalah 0, 0, 1.
3) Class selector, attribute selector, dan pseudo-class, contohnya seperti .container, :hover, atau [type="text"] yang punya nilai specificity 0, 1, 0.
4) ID selector,  contohnya #header punya nilai specificity 1, 0, 0.
5) Inline style, style yang ditulis langsung dalam atribut style pada elemen HTML, contohnya <h1 style="color: red;">, nilai specificity-nya adalah 1, 0, 0, 0. 
6) !important, bukan bagian dari specificity, tapi akan mengalahkan semua aturan lain kecuali ada aturan lain juga dengan !important.

Sumber: https://www.easycoding.id/blog/urutan-prioritas-selector-css-specificity-panduan-lengkap-untuk-memahami-dan-menggunakan

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Jawab:
Responsive design penting dalam pengembangan aplikasi web karena mampu meningkatkan pengalaman pengguna (user experience). Menurut WebFX, responsive design membuat tampilan konten otomatis menyesuaikan ukuran layar sehingga pengguna tidak perlu melakukan zoom atau scroll horizontal. Designmodo juga menegaskan bahwa desain yang responsif membuat interaksi lebih nyaman dan intuitif. Selain itu, responsive design memungkinkan penyesuaian terhadap berbagai perangkat dan resolusi layar tanpa harus membuat versi terpisah, sehingga satu website bisa fleksibel digunakan di HP, tablet, laptop, hingga layar besar. Dari sisi teknis, WebFX menjelaskan bahwa desain responsif mendukung mobile-friendliness yang menjadi salah satu faktor peringkat Google, serta menghemat biaya pengembangan karena hanya membutuhkan satu basis desain yang dapat digunakan lintas perangkat.

Designmodo menambahkan bahwa responsive design membantu menjaga konsistensi merek di berbagai perangkat, sehingga identitas visual tetap kuat dan pengguna tidak bingung saat berpindah perangkat. Selain itu, desain yang responsif juga dapat menurunkan tingkat bounce dan meningkatkan konversi, karena pengguna merasa lebih nyaman, bertahan lebih lama di website, dan terdorong melakukan interaksi seperti membeli atau mendaftar. Dengan demikian, responsive design bukan hanya penting untuk kenyamanan pengguna, tetapi juga memberikan keuntungan nyata bagi keberlangsungan dan pertumbuhan aplikasi web.

Contoh aplikasi atau website yang sudah menerapkan responsive design adalah The Boston Globe. Situs berita ini berhasil menyesuaikan tata letak konten, ukuran gambar, dan navigasi sehingga tetap nyaman diakses baik melalui desktop maupun perangkat mobile. Begitu juga dengan Dropbox, yang tampilannya sederhana dan fleksibel, membuat pengguna mudah mengakses layanan di berbagai perangkat. Penerapan responsive design ini membantu menjaga konsistensi merek sekaligus meningkatkan keterlibatan pengguna.

Di sisi lain, masih ada aplikasi atau website yang belum sepenuhnya menerapkan responsive design, misalnya beberapa situs institusi pemerintah yang ketika diakses melalui smartphone menampilkan teks terlalu kecil, gambar meluber, atau navigasi yang sulit digunakan. Hal ini biasanya disebabkan penggunaan template lama yang tidak mendukung desain adaptif, keterbatasan anggaran, atau kurangnya perhatian terhadap pengalaman pengguna mobile. Akibatnya, website menjadi sulit digunakan, meningkatkan kemungkinan pengunjung keluar lebih cepat (bounce rate), dan menurunkan efektivitas tujuan dari aplikasi atau website tersebut.

Sumber: https://www.webfx.com/web-design/learn/why-responsive-design-important/ https://designmodo.com/responsive-design-examples/

3.  Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Jawab:
Margin, border, dan padding adalah tiga bagian penting dalam CSS box model yang mengatur ruang di sekitar elemen. Margin adalah ruang di luar border elemen yang berfungsi mengatur jarak antar elemen, sehingga jika ingin memberi jarak antar elemen, digunakanlah margin. Border merupakan garis tepi yang mengelilingi elemen, membatasi area padding dan konten, dan posisinya berada di antara margin dan padding. Sementara itu, padding adalah ruang di dalam border, yaitu jarak antara isi elemen dan garis tepinya, sehingga konten tidak menempel langsung pada border.

Dalam analoginya, konten digambarkan sebagai panda, border sebagai pillowcase, padding sebagai ruang antara panda dan pillowcase, sedangkan margin adalah ruang di luar pillowcase. Dengan demikian, urutannya dari dalam ke luar adalah: konten → padding → border → margin.

Cara mengimplementasikan margin, border, dan padding, yaitu:
/* Mengatur margin */
.element {
  margin: 20px;           /* semua sisi margin = 20px */
  margin-top: 10px;       /* margin atas */
  margin-right: 15px;     /* margin kanan */
  margin-bottom: 10px;    /* margin bawah */
  margin-left: 5px;       /* margin kiri */
}

/* Mengatur padding */
.element {
  padding: 20px;           /* semua sisi padding = 20px */
  padding-top: 10px;       /* padding atas */
  padding-right: 15px;     /* padding kanan */
  padding-bottom: 10px;    /* padding bawah */
  padding-left: 5px;       /* padding kiri */
}

/* Mengatur border */
.element {
  border: 2px solid black;       /* border dengan ketebalan 2px, garis padat, warna hitam */
  border-top: 1px dashed red;    /* contoh border sisi atas khusus */
  border-radius: 5px;            /* contoh membuat sudut melengkung */
}
Dalam penerapannya, margin dan padding dapat dituliskan dengan 1 hingga 4 nilai sekaligus. Jika hanya satu nilai, maka berlaku untuk semua sisi. jika dua nilai, maka nilai pertama untuk atas & bawah, dan nilai kedua untuk kiri & kanan. jika tiga nilai, maka urutannya atas, kanan & kiri, lalu bawah, sedangkan empat nilai ditulis urut searah jarum jam: atas, kanan, bawah, kiri. Selain itu, margin dan padding juga bisa diatur secara spesifik menggunakan properti, seperti margin-top, margin-right, margin-bottom, margin-left, maupun padding- untuk sisi tertentu. Sementara itu, border dapat disesuaikan dengan gaya (misalnya solid, dashed, atau dotted), warna, dan ketebalan. Semua implementasi ini bisa ditulis dalam file CSS terpisah, di dalam tag <style> pada HTML, atau menggunakan inline style langsung pada elemen HTML, meskipun penggunaan inline style umumnya kurang disarankan karena menyulitkan proses pemeliharaan kode.

Sumber: https://www.howtocanvas.com/create-amazing-pages-in-canvas/margins-and-padding

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Jawab:
Flexbox (Flexible Box) adalah sistem layout satu dimensi yang dirancang untuk menyusun elemen-elemen dalam suatu kontainer baik secara horizontal (baris) maupun vertikal (kolom). Dengan Flexbox, setiap item dalam sebuah kontainer bisa diatur perataan (alignment)-nya, distribusi ruang kosong, hingga kemampuan item untuk tumbuh (grow) atau menyusut (shrink) agar menyesuaikan ukuran kontainer. Kelebihan utama Flexbox adalah fleksibilitas dalam mengatur elemen-elemen kecil atau komponen yang biasanya ditampilkan secara linear. Contoh kegunaannya termasuk menyusun navigasi horizontal, menata tombol dalam satu baris, atau membuat daftar kartu produk yang ukurannya dapat menyesuaikan ruang layar.

Sedangkan, Grid Layout adalah sistem layout dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom sekaligus. Grid menyediakan kerangka kerja yang lebih terstruktur untuk membuat tata letak halaman yang kompleks, seperti mengatur posisi header di atas, sidebar di samping, area konten utama di tengah, dan footer di bawah. Grid memudahkan developer untuk mendesain layout modular dengan kontrol penuh atas ukuran baris/kolom, jarak antar elemen, hingga penggabungan sel (cell spanning). Kelebihannya ada pada kemampuannya menciptakan layout besar yang rapi, konsisten, dan mudah diskalakan untuk berbagai ukuran layar.

Karena sifatnya berbeda, masing-masing sistem punya kegunaannya sendiri. Flexbox paling efektif dipakai untuk tata letak yang sederhana dan mengalir dalam satu arah, sedangkan Grid unggul untuk tata letak yang lebih besar, terstruktur, dan melibatkan baris sekaligus kolom. Dalam praktiknya, banyak pengembang menggabungkan keduanya, Grid digunakan untuk kerangka utama halaman, lalu di dalam setiap area Grid, Flexbox dipakai untuk menyusun elemen internal secara lebih fleksibel. Dengan begitu, halaman web bisa mendapatkan manfaat terbaik dari kedua sistem layout ini.

Sumber: https://zerotomastery.io/blog/css-grid-vs-flexbox/


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawab:

1) Integrasi Tailwind ke Proyek
- Buka file base.html pada folder templates di root project.
- Tambahkan link Tailwind CDN di dalam tag <head>.

<head>
  {% block meta %}
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1">
  {% endblock meta %}
  <script src="https://cdn.tailwindcss.com"></script>
</head>

2) Buat Fitur Edit Product
- Di file views.py (subdirektori main), tambahin fungsi baru namanya edit_product yang menerima parameter request dan id.
- Buat template baru namanya edit_product.html di main/templates/.
- Buka urls.py dalam direktori main, lalu import fungsi edit_product yang udah dibuat.
- Tambahin route baru pada urlpatterns untuk menghubungkan URL dengan fungsi tersebut.
- Pada file main.html, perbarui looping product_list agar tiap produk nampilin tombol Edit, yang hanya terlihat oleh user yang login dan merupakan pemilik produk.

3) Buat Fitur Delete Product
- Tambahin fungsi delete_product di views.py (folder main) untuk menghapus data produk berdasarkan id.
- Import fungsi ini ke dalam urls.py.
- Tambahin path baru pada urlpatterns untuk manggil fungsi delete.
- Pada main.html, tambahin tombol Delete di dalam loop product_list untuk tiap produk.

4) Tambahin Navigation Bar
- Buat file baru namanya navbar.html pada folder templates/ di root project.
- Isi dengan struktur HTML untuk navigasi.
- Hubungin ke main.html (dalam main/templates/) pakai tag {% include %} agar navbar muncul di setiap halaman yang diinginkan.

5) Konfigurasi Static Files
- Tambahin WhiteNoise Middleware pada settings.py agar file statis bisa dilayani dengan baik.
- Pastiin konfigurasi variabel statis sudah sesuai:
STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
else:
    STATIC_ROOT = BASE_DIR / 'static'

6) Styling Aplikasi dengan Tailwind + CSS Eksternal
- Buat file global.css di folder /static/css/ pada root project.
- Hubungin global.css dan Tailwind ke dalam base.html.
- Tambahin custom styling ke dalam static/css/global.css.
- Lakuin kustomisasi tampilan di beberapa bagian aplikasi:
    - Navbar → perbarui desain di navbar.html.
    - Login Page → edit login.html di main/templates/.
    - Register Page → ubah register.html di main/templates/.
    - Halaman Home →
        - Buat card_product.html di main/templates/.
        - Siapin gambar default no-product.png di /static/image/.
        - Pakai card_product.html dan no-product.png pada main.html.
    - Detail Product → update product_detail.html.
    - Create Product → update create_product.html.
    - Edit Product → ganti desain pada edit_product.html.

7) Menjalankan Aplikasi
Jalankan server lokal dengan: python manage.py runserver

8) Push ke GitHub dan PWS
Simpan perubahan lalu masukan ke repository dan PWS:
git add .
git commit -m "<pesan commit>"
git push origin master
git push pws master

--> TUGAS 6
1. Apa perbedaan antara synchronous request dan asynchronous request?
Jawab:
Dalam JavaScript, objek XMLHttpRequest (XHR) mendukung dua jenis komunikasi dengan server, yaitu synchronous dan asynchronous. Namun, secara umum, asynchronous request lebih disarankan, karena memberikan performa yang lebih baik dan pengalaman pengguna yang lebih responsif. Pada synchronous request, proses pengiriman dan penerimaan data dilakukan secara berurutan dan saling menunggu. Artinya, saat permintaan dikirim ke server, JavaScript akan berhenti mengeksekusi kode lainnya sampai respons diterima sepenuhnya. Hal ini menyebabkan halaman web tampak “membeku” (freezing) atau tidak responsif selama proses berlangsung. synchronous XHR ditandai sebagai fitur yang deprecated (tidak direkomendasikan lagi), karena dapat menyebabkan lag terutama saat jaringan lambat atau server memerlukan waktu lama untuk merespons. Fitur-fitur baru, seperti timeout dan abort juga tidak dapat digunakan dalam mode synchronous.

Sebaliknya, asynchronous request memungkinkan browser melanjutkan eksekusi kode lain sambil menunggu respons dari server. JavaScript tidak akan berhenti, dan fungsi callback akan dijalankan secara otomatis setelah data diterima.
Contohnya, dengan menggunakan xhr.open("GET", "/data.txt", true);, nilai true pada parameter ketiga menunjukkan bahwa request tersebut dilakukan secara asynchronous. Dalam mode ini, browser tetap responsif, pengguna masih bisa berinteraksi dengan halaman sementara proses komunikasi dengan server berlangsung di latar belakang. Pendekatan asynchronous inilah yang jadi dasar dari teknologi AJAX (Asynchronous JavaScript and XML), yang memungkinkan halaman web melakukan operasi, seperti create, update, atau delete data tanpa perlu memuat ulang (reload) seluruh halaman.

Sumber: https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Synchronous_and_Asynchronous_Requests?utm_source=chatgpt.com

2. Bagaimana AJAX bekerja di Django (alur request–response)?
Jawab:
Alur kerja AJAX di Django dimulai dari JavaScript di sisi klien yang ngirim permintaan HTTP, seperti GET, POST, PUT, atau DELETE pakai fetch() atau XMLHttpRequest. Permintaan ini dikirim secara asynchronous ke server Django, biasanya dengan header X-Requested-With: XMLHttpRequest untuk nandain bahwa request berasal dari AJAX. Di sisi server, Django menerima request ini melalui view. View akan memeriksa apakah permintaan tersebut merupakan AJAX request, kemudian memproses data, misalnya mengambil, menambah, memperbarui, atau menghapus data di database, dan mengembalikan respons dalam bentuk JSON pakai JsonResponse. Data JSON ini kemudian diterima kembali oleh JavaScript di browser, yang akan memperbarui tampilan halaman (DOM) tanpa perlu memuat ulang seluruh halaman.

Selain itu, dalam alur AJAX di Django, URL routing juga berperan penting untuk ngarahin permintaan dari JavaScript ke view yang sesuai. Django memetakan endpoint, seperti /add-product/ atau /delete-item/ melalui urls.py. Jika request menggunakan metode POST, biasanya juga disertakan CSRF token agar Django dapat memverifikasi bahwa permintaan berasal dari sumber yang sah dan aman.

Alur ini menggambarkan siklus penuh request–response AJAX di Django:
(1) client mengirim request async → (2) Django view memproses → (3) server mengirim JSON response → (4) browser memperbarui tampilan secara dinamis.

Sumber: https://testdriven.io/blog/django-ajax-xhr/?utm_source=chatgpt.com

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Jawab:
Penggunaan AJAX dalam Django memberikan beberapa keuntungan dibandingkan dengan render biasa, antara lain:
1) Meningkatkan performa aplikasi, AJAX memungkinkan pengambilan data dari server tanpa perlu me-refresh seluruh halaman. Hal ini mempercepat waktu loading dan membuat pengalaman pengguna lebih lancar tanpa gangguan.
2) Mempercepat waktu respons, karena hanya data yang dibutuhkan yang dikirim ke server, penggunaan bandwidth jadi lebih efisien dan proses pengambilan informasi berlangsung lebih cepat.
3) Mengurangi beban server, karena AJAX hanya memperbarui bagian tertentu dari halaman secara asynchronous, sehingga jumlah data yang dikirim antara client dan server berkurang. Ini membuat penggunaan sumber daya server jadi lebih ringan dan efisien.
4) Mendukung pemanggilan asynchronous, dengan AJAX, pengguna tetap bisa berinteraksi dengan aplikasi sementara data sedang diproses di latar belakang, tanpa harus nunggu halaman selesai dimuat.
5) Meningkatkan pengalaman pengguna (User Experience), AJAX memungkinkan pembaruan konten secara dinamis pada bagian tertentu halaman, seperti saat ngirim form atau nampilin data baru, tanpa perlu reload halaman penuh. Hasilnya, aplikasi terasa cepat, responsif, dan lebih menyerupai aplikasi desktop.

Sumber: https://www.mageplaza.com/blog/advantages-and-disadvantages-of-ajax.html?utm_source=chatgpt.com

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Jawab:
Untuk memastikan keamanan saat menggunakan AJAX pada fitur Login dan Register di Django, penting untuk nerapin mekanisme CSRF (Cross-Site Request Forgery) Protection yang disediakan oleh Django. Mekanisme ini mastiin kalau setiap permintaan POST, PUT, atau DELETE yang dikirim lewat JavaScript benar-benar berasal dari situs yang sah dan bukan dari pihak luar yang berusaha mengeksploitasi pengguna. Django secara otomatis nambahin token CSRF pada halaman HTML melalui tag {% csrf_token %}, dan token ini perlu disertakan dalam setiap permintaan AJAX melalui header X-CSRFToken. Token tersebut biasanya diambil dari cookie browser bernama csrftoken pakai JavaScript sebelum dikirim ke server. Selain itu, middleware CsrfViewMiddleware di settings.py harus tetap aktif agar Django bisa memverifikasi validitas token tersebut. Untuk nambah lapisan keamanan, seluruh komunikasi antara klien dan server sebaiknya dilakukan melalui HTTPS, sehingga data sensitif seperti kredensial login tidak mudah disadap. Dengan menerapkan langkah-langkah ini, proses login dan register menggunakan AJAX di Django dapat berjalan secara aman dan terlindung dari serangan CSRF.

Sumber: https://docs.djangoproject.com/en/3.1/ref/csrf/?utm_source=chatgpt.com

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
Jawab:
AJAX memengaruhi pengalaman pengguna (User Experience) dengan membuat interaksi di website jadi lebih cepat, halus, dan responsif. Teknologi ini memungkinkan halaman web mengirim dan menerima data dari server tanpa perlu memuat ulang seluruh halaman, sehingga pengguna dapat melihat pembaruan konten secara langsung di bagian tertentu tanpa gangguan. Dengan proses yang berjalan secara asynchronous, pengguna tetap bisa berinteraksi dengan elemen lain di halaman sambil menunggu respons dari server. Hasilnya, website terasa lebih dinamis dan interaktif, serupa dengan aplikasi desktop modern yang memberikan pengalaman yang efisien dan menyenangkan bagi pengguna.

Sumber: https://2stallions.com/blog/ajax/?utm_source=chatgpt.com 