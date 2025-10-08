Edlyn Marva - 2406410494
URL = https://edlyn-marva-indoshop.pbp.cs.ui.ac.id/



<p>
<details>
<summary>Tugas 2</summary>


1. penjelasan implementasi checklist secara step-by-step
    1) membuat direktori lokal dengan nama indo-shop
    2) pertama, saya membuat virtual environment dengan menjalankan perintah python -m venv env
    3) mengaktifkan virtual environment dengan perintah env\Scripts\activate
    4) membuat berkas requirements.txt yang berisi beberapa library termasuk django
    5) melakukan instalasi dengan menjalankan perintah pip install -r requirements.txt
    6) membuat proyek Django dengan perintah django-admin startproject indo_shop
   

    7) untuk membuat app main jalankan perintah python manage.py startapp main
    8) kemudian daftarkan aplikasi main di dalam berkas settings.py bagian INSTALLED_APPS
    9) kemudian, pada models.py saya membuat model dengan nama product yang berisi atribut yang telah ditentukan. saya juga menambahkan method __str__ yang mengembalikan nama produk
    10) pada views.py saya membuat fungsi show_main yang berisi dictionary context. fungsi ini mengembalikan request HTTP yang dikirim pengguna, berkas template (main.html) untuk me-render tampilan, dan dictionary context.
    11) buat main/templates/main.html. kemudian saya melakukan penyesuaian tampilan untuk menampilkan nilai yang diterima dari show_main

    12) buat main/urls.py kemudian import show_main dari main/views dan tambahkan daftar aturan URL sehingga ketika user membuka alamat url, Django akan jalankan fungsi show_main. Rute ini dinamakan show_main --> path('', show_main, name='show_main')
    13) setelah itu, untuk melakukan routing di level proyek perlu dilakukan penyesuaian di indo_shop/urls.py. Impor pola rute dari aplikasi main dengan menambahkan path('', include('main.urls')) dalam list urlpatterns
    14) untuk melakukan deployment, saya membuat projek baru di PWS. mengisi kredensial database, dan memasukkan link projek pws ke settings.py
    15) setelah itu saya mengirim perubahan kode dari komputer ke server git PWS

2.  bagan : https://drive.google.com/file/d/1vI4FYW-tt3X2YnKFDUs7_8o-a367fPv3/view?usp=sharing
    1) User mengakses aplikasi lewat browser → misalnya http://localhost:8000/home.
    2) Web server (saat development biasanya pakai server bawaan Django dengan python manage.py runserver) menerima request itu.
    3) Server tersebut lalu meneruskan request ke Django framework, lewat sistem URL routing (urls.py) untuk mencari view yang sesuai.
    4) View memproses request (bisa akses models, jalankan logika, dll.) dan menghasilkan konteks data dari view. 
    5) Mesin ini kemudian merender template HTML yang sesuai 
    5) Response dikirim kembali ke user lewat server.

3. Di project ini, settings.py penting karena berfungsi sebagai pusat konfigurasi Django yang mengatur jalannya aplikasi main, mulai dari mendaftarkannya di INSTALLED_APPS, mengatur environment lewat .env (misalnya PRODUCTION=False untuk development), menyimpan pengaturan keamanan seperti SECRET_KEY dan DEBUG, hingga koneksi ke database, static files, serta template. Tanpa settings.py, project tidak akan tahu aplikasi mana yang aktif, bagaimana cara terhubung ke database, atau mode apa yang sedang dijalankan.

4. pada saat makemigrations, django mengecek perubahan pada models dan membuat file baru yang mencatat perubahan pada database. setelah terbuat, perintah migrate akan mengecek berkas perubahan kemudian mengekusi database sehingga tabel/kolom terbentuk di database sesuai model. Kedua perintah ini dijalankan supaya kode model di models.py sinkron dengan database nyata

5. menurut saya Django layak dijadikan landasan dalam pembelajaran pengembangan perangkat lunak karena framework ini menawarkan ekosistem yang menyeluruh dan terintegrasi melalui filosofi “batteries-included”, sehingga berbagai kebutuhan fundamental—mulai dari manajemen basis data, autentikasi, hingga user admin tersedia secara bawaan dan siap digunakan. Dengan arsitektur Model-View-Template (MVT) yang jelas, Django mendorong penggunaan kode yang terstruktur, serta penerapan prinsip Don’t Repeat Yourself (DRY) yang krusial dalam membangun sistem berskala besar. Selain itu, keamanan yang terjamin melalui perlindungan default terhadap serangan umum, ditambah dengan besarnya komunitas global yang juga menggunakan Django, menjadikan ini tidak hanya efisien untuk mempercepat proses pengembangan, tetapi juga relevan sebagai kerangka konseptual dalam memahami praktik terbaik industri perangkat lunak.

6. Menurut saya, tutorial 1 kemarin sudah sangat baik. Setiap command yang saya tidak pahami dapat saya pelajari lebih lanjut dengan saangat mudah karena asdos memberikan keterangan yang mudah dimengerti untuk setiap bagiannya. Selain itu, petunjuk mengenai apa yang harus dilakukan sudah disusun dengan sangat baik sehingga mudah diikuti
    

</details>
<details>
    <summary> Tugas 3</summary>
postman utl = https://drive.google.com/drive/folders/1GWu1P0OkPzyD2C1SjRl9fKzgSig__-hG?usp=sharing
    
1. Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena platform modern biasanya memisahkan tampilan depan (frontend) seperti website atau aplikasi mobile, dengan logika dan penyimpanan data di belakang (backend). Data delivery berfungsi sebagai jembatan yang menghubungkan kedua bagian ini, memungkinkan mereka untuk saling berkomunikasi dengan bertukar data terstruktur seperti JSON atau XML.

2. Saya pribadi lebih menyukai JSON  karena formatnya sederhana, mudah dibaca. Sintaksnya sederhana tanpa tag pembuka-penutup panjang sehingga ukuran data lebih kecil, sedangkan XML lebih panjang dan rumit sehingga kini jarang dipakai kecuali untuk dokumen atau sistem lama. Json juga lebih cepat di parsing. Hal ini juga yang membuat JSON lebih populer

3. is_valid() pada form Django memeriksa apakah data yang dikirim sesuai aturan field dan validator di form, sekaligus menjalankan proses cleaning. Kita membutuhkannya agar hanya data yang sudah lolos pengecekan (misal  panjang url, format angka ) yang diproses atau disimpan ke database. Kita membutuhkannya untuk mmastikan data yang disimpan ke database konsisten dan mematuhi aturan bisnilogic yang telah ditetapkan

4. Kita membutuhkan csrf_token untuk melindungi form dan request POST kita dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah serangan dimana seorang penyerang menipu korban (yang sudah login) untuk melakukan sebuah tindakan (request) di website target tanpa sepengetahuan korban. Jika form Django tidak menyertakan csrf_token, server akan menolak request POST tersebut karena server membandingkan token yang dikirim dengan token yang disimpan di server. 

5. Berikut langkah yang saya lakukan

    1) pertama saya membuat file base.html pada direktori template root sebagai kerangka layout utama 
    2) kemudian main/forms.py saya membuat class ProductForm untuk membuat Product baru. Di sini saya membuat fields yang perlu diisi oleh user seperti name, price dll.
    3) saya membuat template create_product.html yang  mengextends base.html dan akan generate{% csrf_token %} random. Template ini akan menampilkan ProductForm 
    4) forms tadi diimpor ke views dan saya membuat function create_product yang mengembalikan dict berisi ProductForm dan akan menmpilkannya di create_product.html.
    5) impor function ke main/urls.py dan menambahkan URL ke dalan urlpatterns
    6) Setelah itu saya membuat function show_product di views.py yang akan menampilkan detail produk apabila ditemukan di product_detail.html
    7) kemudian saya mengimpor function tersebut ke urls.py dan menambahkan path URL ke variable urlpatterns
    8) pada berkas views.py saya menambahkan 4 fungsi baru yaitu show_xml, show_json, show_xml_by_id, show_json_by_id yang masing masing sesuai namanya akan mengambil  object Product di database (di filter sesuai uuid apabila show by id) kemudian format objek diubah menjadi xml/json sesuai request dan mengirim string xml ataupun json ke browser klien sehingga tidak dikenali sebagai html biasa
    9) selain itu pada fungsi show_xml_by_id & show_json_by_id saya menambahkan try and except yang akan menghandle apabila tidak ditemukan objek yang memiliki uuid yang di request
    10) untuk melakukan routing saya mengimpor function yang sudah dibuat pada views.py ke ,main/urls.py 
    11) setelah itu saya menambahkan path URL ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi





</details>
<details>
    <summary>Tugas 4</summary>
1. Dalam konteks Django, AuthenticationForm merupakan kelas formulir bawaan yang secara langsung terintegrasi dengan sistem otentikasi Django.
Secara teknis, kelas ini menurunkan sifat dari forms.Form, sehingga tetap mengikuti struktur dan cara kerja form Django pada umumnya, tetapi dengan fokus khusus pada proses login. Kelebihan utamanya yaitu, kita tidak perlu lagi membangun fitur-fitur dasar seperti pendaftaran, login, dan logout dari nol. Django telah menyediakan built-in forms seperti UserCreationForm dan AuthenticationForm yang sudah terintegrasi dengan model User bawaannya. Kekurangannya adalah, kita memiliki keterbatasan dalam menyesuaikan proses otentikasi sesuai kebutuhan spesifik aplikasi kita. Misalnya, jika kita ingin menambahkan lapisan keamanan tambahan atau mengubah cara validasi kredensial, kita mungkin perlu membuat formulir kustom yang lebih kompleks.

2. Autentikasi berfokus pada verifikasi identitas pengguna, yaitu memastikan bahwa pengguna adalah siapa yang mereka klaim, dan ini dicapai melalui proses seperti validasi kredensial (nama pengguna dan kata sandi) saat login. Django mengimplementasikan ini dengan sistem autentikasi bawaan yang mencakup User model, AuthenticationForm, serta fungsi login() dan authenticate(). Setelah pengguna terautentikasi, barulah proses otorisasi dimulai, yang menentukan hak akses atau izin pengguna terhadap berbagai bagian aplikasi. Django mengelola otorisasi melalui sistem izin (permissions) dan grup (groups) yang memungkinkan kita untuk menetapkan hak akses spesifik kepada pengguna atau kelompok pengguna tertentu. Dengan demikian, autentikasi adalah langkah awal untuk mengenali pengguna, sedangkan otorisasi adalah langkah lanjutan untuk mengatur apa yang boleh dan tidak boleh dilakukan oleh pengguna tersebut dalam aplikasi. Misalnya, dengan menggunakan decorator seperti @permission_required, pengembang dapat membatasi akses ke sebuah view atau fungsionalitas

3.Secara umum, cookies menyimpan data langsung di sisi client atau browser pengguna. Keuntungannya adalah sederhana dan tidak membebani server karena data tidak perlu diakses dari sana, bahkan memungkinkan akses secara offline. Namun, kekurangannya terletak pada masalah keamanan karena data cookies dapat dimanipulasi oleh client, serta kapasitas penyimpanannya yang sangat terbatas. Di sisi lain, session menyimpan data di sisi server, dengan ID sesi unik yang disimpan di cookie browser sebagai jembatan. Ini memberikan keunggulan keamanan yang jauh lebih baik karena data sensitif tidak pernah terpapar ke sisi client. Session juga menawarkan kapasitas penyimpanan yang tidak terbatas, hanya dibatasi oleh sumber daya server. Kekurangannya adalah session dapat membebani server, terutama pada aplikasi dengan jutaan pengguna

4. Penggunaan cookies dalam pengembangan web tidak dapat dianggap aman secara default, melainkan memerlukan konfigurasi dan implementasi yang hati-hati untuk memitigasi berbagai risiko keamanan yang melekat. Risiko utama yang harus diwaspadai termasuk kerentanan Cross-Site Scripting (XSS) dimana penyerang dapat mengeksekusi kode JavaScript berbahaya untuk mencuri cookies pengguna, serangan Cross-Site Request Forgery (CSRF) yang memanfaatkan autorisasi dari browser terhadap cookies untuk melakukan aksi tidak sah atas nama pengguna, session hijacking dimana penyerang dapat mengambil alih sesi pengguna dengan mencuri session identifier, dan masih banyak lagi.

Django menangani tantangan keamanan cookies ini melalui beberapa mekanisme built-in yang dirancang untuk melindungi data pengguna. Salah satu fitur utama adalah penggunaan CSRF tokens yang secara otomatis disertakan dalam form HTML untuk mencegah serangan CSRF. Selain itu, Django memungkinkan pengaturan atribut keamanan pada cookies seperti HttpOnly, yang mencegah akses cookies melalui JavaScript, dan Secure, yang memastikan cookies hanya dikirim melalui koneksi HTTPS. Django juga menyediakan opsi untuk mengenkripsi cookies dan mengatur masa berlaku (expiry) yang sesuai untuk mengurangi risiko session hijacking. Dengan menerapkan praktik-praktik ini, Django membantu pengembang membangun aplikasi web yang lebih aman dan melindungi data sensitif pengguna dari potensi ancaman.

5. Berikut langkah yang saya lakukan untuk mengimplementasikan fitur login, logout, dan registrasi di aplikasi Django saya. selain itu saya juga Merestriksi Akses Halaman Main dan produk Detail:


    1) pertama, saya membuat view register di main/views.py yang akan menampilkan SignUpForm. Jika form valid, data user baru disimpan ke database dan user langsung login serta diarahkan ke halaman utama.
    2) setelah itu, saya membuat template register.html yang mengextends base.html dan menampilkan SignUpForm. Template ini juga menyertakan {% csrf_token %} untuk keamanan.
    3) untuk login, saya menggunakan AuthenticationForm bawaan Django. Saya membuat view login_user di main/views.py yang menampilkan form login. Jika valid, user akan diarahkan ke halaman utama.
    4) saya juga membuat template login.html yang mengextends base.html dan menampilkan AuthenticationForm beserta {% csrf_token %}.
    5) untuk logout, saya membuat function logout_user di main/views.py yang memanggil fungsi logout() dari django.contrib.auth dan mengarahkan user ke halaman login setelah logout.
    6) semua view ini saya daftarkan di main/urls.py dengan path masing-masing seperti 'register/', 'login/', dan 'logout/'.
    7) untuk merestriksi akses ke halaman main dan detail produk, saya menggunakan decorator @login_required pada view show_main dan show_product. Ini memastikan bahwa hanya pengguna yang sudah login yang dapat mengakses halaman-halaman tersebut.
    8) untuk menghubungkan model Product dengan User, saya menambahkan field ForeignKey ke model Product yang mengacu pada model User bawaan Django di main/models.py.
    9) pada fungsi create_product di main/views.py, saya memodifikasi agar produk yang dibuat otomatis terkait dengan user yang sedang login (creator).
    10) kemudian untuk menerapkan cookies seperti last_login pada halaman utama aplikasi saya menyimpan informasi last login di cookies dengan menambahkan response.set_cookie('last_login', str(datetime.now())) pada fungsi login_user di main/views.py supaya bisa di simpan di cookies. untuk show di main.html saya menambahkan {{ last_login }} yang diambil dari context di show_main.
    11) untuk Menampilkan detail informasi pengguna yang sedang logged in seperti username dan last login di halaman utama, saya menambahkan 'name': request.user.username di context show_main di main/views.py. Kemudian di main.html saya menampilkan {{ name }} untuk username dan {{ last_login }} untuk sesi terakhir login.

</details>
</p>

<p><details>
<summary>Tugas 5</summary>
1. Urutan prioritas pengambilan CSS selector
CSS memiliki aturan khusus dalam menentukan selector mana yang akan diterapkan ketika terdapat lebih dari satu aturan untuk elemen yang sama. Prioritas CSS ditentukan oleh spesifisitas, di mana urutannya adalah: inline style (paling tinggi), ID selector, class/atribut/pseudo-class selector, dan terakhir element/tag selector.  Jika dua selector memiliki spesifisitas yang sama, maka aturan yang didefinisikan paling akhir di dalam file CSS akan didahulukan. Sebagai pengecualian, terdapat deklarasi !important yang dapat ditambahkan pada sebuah properti CSS (contoh: color: red !important;). Aturan ini akan mengalahkan semua tingkat spesifisitas lainnya.

2. Responsive design adalah sebuah pendekatan dalam pengembangan web yang bertujuan agar tampilan situs web dapat beradaptasi secara optimal pada berbagai ukuran layar perangkat, mulai dari desktop, tablet, hingga smartphone. Konsep ini menjadi sangat penting karena tiga alasan utama. Pertama, dari sisi pengalaman pengguna (User Experience), situs yang responsif memberikan kemudahan navigasi dan keterbacaan tanpa mengharuskan pengguna melakukan pinch-and-zoom atau scroll horizontal, yang dapat membuat frustrasi dan menyebabkan pengguna meninggalkan situs. Kedua, dari sisi SEO (Search Engine Optimization), mesin pencari seperti Google secara aktif memprioritaskan situs yang mobile-friendly dalam hasil pencariannya. Situs yang tidak responsif akan mendapatkan peringkat yang lebih rendah, sehingga mengurangi visibilitas dan trafik organik. Ketiga, dari sisi efisiensi pengembangan, dengan responsive design, pengembang hanya perlu mengelola satu basis kode (codebase) untuk semua perangkat, berbeda dengan zaman dahulu di mana pengembang seringkali harus membuat versi situs terpisah untuk desktop dan mobile (misalnya www.contoh.com dan m.contoh.com).


3. Perbedaan Margin, Border, dan Padding
Dalam CSS, setiap elemen HTML dapat dianggap sebagai sebuah kotak, yang dikenal dengan konsep Box Model. Tiga komponen utama yang mengatur ruang di sekitar konten elemen adalah margin, border, dan padding. Padding adalah ruang transparan yang berada di dalam batas elemen, yaitu di antara konten (seperti teks atau gambar) dan border. Fungsinya adalah untuk memberikan jarak agar konten tidak menempel langsung pada garis batas. Border adalah garis yang mengelilingi padding dan konten. Border memiliki ketebalan, gaya (misalnya solid, putus-putus), dan warna yang dapat diatur. Margin adalah ruang transparan yang berada di luar border. Fungsinya adalah untuk menciptakan jarak atau mendorong elemen lain agar tidak saling menempel.

4. Flexbox dirancang untuk tata letak satu dimensi, artinya ia sangat baik dalam mengatur item-item dalam satu baris (row) atau satu kolom (column). Kegunaan utamanya adalah untuk menyusun, meratakan, dan mendistribusikan ruang di antara item-item dalam sebuah kontainer. Di sisi lain, Grid Layout dirancang untuk tata letak dua dimensi, yaitu mengatur elemen dalam baris dan kolom secara bersamaan. Grid adalah alat yang sangat kuat untuk merancang tata letak halaman web secara keseluruhaan.

5. berikut adalah langkah saya untuk Desain Web menggunakan HTML, CSS dan Framework CSS (tailwind)
    1) pertama saya menambahkan link ke file CSS Tailwind di dalam tag <head> di base.html
    2) saya menambahkan whitelist di settings.py agar file static bisa diakses di mode production
    3) saya membuat static/css/global.css yang berisi beberapa aturan CSS kustom untuk menyesuaikan tampilan aplikasi. file ini dibuat static agar bisa diakses oleh template HTML dan di link di base.html. file ini berisi aturan css yang tidak tersedia di tailwind
    4) Agar style CSS yang ditambahkan di global.css dapat digunakan dalam template Django, kamu perlu menambahkan file tersebut ke base.html
    5) kemudian saya membuat function baru di views yaitu edit_product yang akan menghandle edit produk dan delete_product yang akan menghandle penghapusan produk di main/views.py
    6) setelah itu saya membuat html baru yaitu edit_product.html yang mengextends base.html. di sini saya membuat form yang menampilkan data produk yang akan diedit. 
    7) saya mengimpor function tersebut ke main/urls.py dan menambahkan path URL ke dalam urlpatterns
    8) saya juga membuat card_product.html yang berisi template card produk yang akan di include di main.html
    9) selain itu, saya membuat navbar.html yang berisi template navbar yang akan di include di main.html
    10) pada main.html saya menginclude card_product.html untuk menampilkan setiap produk dalam bentuk card dan include navbar.html untuk menampilkan navbar di bagian atas halaman.
    11) selanjutnya saya menambahkan beberapa class tailwind di setiap elemen HTML di template seperti main.html, base.html, create_product.html, edit_product.html, register.html, login.html, product_detail.html untuk meodifikasi tampilan aplikasi



</details></p>
<p><details>
<summary>Tugas 6</summary>
Apa perbedaan antara synchronous request dan asynchronous request?
 Bagaimana AJAX bekerja di Django (alur request–response)?
 Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
 Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
 Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
 1. Perbedaan utama antara synchronous request dan asynchronous request terletak pada cara mereka menangani komunikasi antara klien (biasanya browser) dan server. Synchronous request mengharuskan klien untuk menunggu hingga server merespons sebelum melanjutkan eksekusi kode berikutnya. Ini berarti bahwa selama permintaan sedang diproses, pengguna tidak dapat berinteraksi dengan halaman web, yang dapat menyebabkan pengalaman pengguna yang buruk jika respons server lambat. Di sisi lain, asynchronous request memungkinkan klien untuk terus menjalankan kode lainnya tanpa harus menunggu respons dari server. Dengan menggunakan AJAX (Asynchronous JavaScript and XML), permintaan dapat dikirim ke server di latar belakang, sehingga pengguna dapat terus berinteraksi dengan halaman web tanpa gangguan.

    2. Alur kerja AJAX di Django dimulai ketika pengguna melakukan aksi di halaman web, seperti mengklik tombol atau mengisi formulir. JavaScript di sisi klien kemudian membuat permintaan HTTP (biasanya GET atau POST) ke server Django menggunakan objek XMLHttpRequest atau metode fetch(). Permintaan ini dikirim secara asynchronous, sehingga tidak mengganggu interaksi pengguna dengan halaman. Di sisi server, Django menerima permintaan tersebut melalui view yang sesuai, memproses data yang diterima (misalnya, menyimpan data ke database atau mengambil data), dan kemudian mengembalikan respons dalam format yang sesuai, seperti JSON atau HTML. Setelah respons diterima oleh JavaScript di klien, kode JavaScript tersebut akan mengeksekusi fungsi callback untuk memperbarui bagian tertentu dari halaman web tanpa perlu memuat ulang seluruh halaman.

    3. Keuntungan utama menggunakan AJAX dibandingkan render biasa di Django adalah peningkatan pengalaman pengguna (User Experience) yang signifikan. Dengan AJAX, hanya bagian tertentu dari halaman web yang diperbarui, sehingga mengurangi waktu tunggu dan membuat interaksi terasa lebih cepat dan responsif. Ini sangat berguna untuk aplikasi web yang memerlukan interaksi dinamis, seperti formulir yang perlu divalidasi secara real-time atau daftar produk yang dapat difilter tanpa memuat ulang halaman. Selain itu, penggunaan AJAX dapat mengurangi beban pada server karena hanya data yang diperlukan yang dikirim dan diterima, bukan seluruh halaman HTML.
    4. Untuk memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django, beberapa langkah penting harus diambil. Pertama, selalu sertakan token CSRF (Cross-Site Request Forgery) dalam setiap permintaan AJAX yang mengubah data di server, seperti login atau registrasi. Django menyediakan mekanisme bawaan untuk menghasilkan dan memverifikasi token CSRF, yang dapat disertakan dalam header permintaan AJAX. Kedua, pastikan bahwa data yang diterima dari klien divalidasi dengan benar di sisi server sebelum diproses atau disimpan ke database. Ini termasuk memeriksa format data, panjang input, dan memastikan bahwa tidak ada injeksi SQL atau serangan XSS (Cross-Site Scripting). Ketiga, gunakan HTTPS untuk mengenkripsi komunikasi antara klien dan server, sehingga data sensitif seperti kata sandi tidak dapat disadap oleh pihak ketiga selama transmisi.

    5. AJAX dapat secara signifikan meningkatkan pengalaman pengguna (User Experience) pada website dengan membuat interaksi lebih cepat dan responsif. Dengan AJAX, pengguna dapat melakukan tindakan seperti mengirim formulir, memuat konten baru, atau memperbarui bagian halaman tanpa harus menunggu seluruh halaman dimuat ulang. Ini mengurangi waktu tunggu dan membuat aplikasi web terasa lebih seperti aplikasi desktop, di mana perubahan terjadi secara instan. Selain itu, AJAX memungkinkan pengembang untuk memberikan umpan balik langsung kepada pengguna, seperti menampilkan pesan kesalahan atau konfirmasi tanpa perlu memuat ulang halaman. Hal ini dapat meningkatkan kepuasan pengguna dan membuat mereka lebih cenderung untuk tetap menggunakan aplikasi web tersebut. Dengan demikian, AJAX tidak hanya meningkatkan kinerja teknis situs web, tetapi juga berkontribusi pada pengalaman pengguna yang lebih baik secara keseluruhan.
</details></p>