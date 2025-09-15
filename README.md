Edlyn Marva - 2406410494
URL = https://edlyn-marva-indoshop.pbp.cs.ui.ac.id/



<p>
<details>
<summary>Cool Dropdown #1</summary>


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
</p>
