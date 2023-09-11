------------------- Adaptable Project Link -------------------\\
Link = https://rpg-web-tester.adaptable.app

------------------- Implement Checklist Tugas -------------------\\
✅ Membuat project Django baru : Membuat folder baru dan menginisiasi git init di folder tersebut. Lalu membuat repository baru di github lalu menghubungkan repository github tersebut dengan lokal folder. Lalu mengaktifkan Virtual Environment, lalu masuk ke virtual environment tersebut. Lalu membuat file txt yang berisi library, frameworks dam package, lalu menginstall semua itu dengan menjalankan "pip install -r [nama file txt].txt". Lalu menjalankan "django-admin startproject [Nama Project]".
✅ Membuat aplikasi dengan nama main pada proyek tersebut : Setelah masuk ke dalam folder project di terminal lalu masuk ke dalam virtual environment, lalu jalankan perintah "python manage.py startapp [Nama App]".
✅ Melakukan routing pada proyek agar dapat menjalankan aplikasi main : Pada folder project buka file setting.py, lalu masukan nama app dalam bentuk string ke dalam list INSTALLED
_APPS.
✅ Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut : Pada folder app main, buka file models.py dan membuat class baru bernama Item. Lalu di dalam class tersebut buat attribut nama yang berupa CharField, amount yang berupa IntegerField, dan description dalam bentuk TextField, serta sebagai tambahan aku membuat attribute power, item_id, item_type, price dan unique skill dengan berupa field yang cocok dengan masing-masing attribute.
✅ Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu : Didalam file views.py membuat fungsi display_main, dimana didalmnya dibuat directory yang dimana key nya adalah variabel untuk memanggil value, dan valuenya adalah hal hal yang ingin ditampilkan di file htmlnya. Lalu mengengembalikan atau mengoper direktory itu ke dalah file html yang akan ditampilkan dalam hal ini "html.main".
✅ Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py : Pada file urls.py di dalam folder project tambahkan path dengan awal urls '' lalu mengarah ke file urls di main dengan manambahkan main.urls di dalam path tersebut. Lalu di dalam file urls.py di dalam app main,  tambahkan path dan tambahkan nama fungsi yang ada di file views.py pada apps yang memanggil file html yang ingin ditampilkan.
✅ Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet : Melakukan git add, commit, push, lalu mengakses adaptable dengan login pada akun github yang digunakan pada repository lalu mendeploy project yang dibuat.
✅ Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut : Membuat file README.md pada folder tugas lalu menjawab-jawab perintah dan pertanyaan yang diberikan.

------------------- Bagan Request Client -------------------
![Alt text](IMG_20230911_233741.jpg)

------------------- Virtual Environment -------------------
Virtual Environment digunakan agar untuk tiap project Django yang berbeda-beda dapat memiliki libraries, frameworks ataupun package yang berbeda-beda ataupun yang sama dengan versi yang berbeda-beda untuk mendukung pembuatan project dengan fungsi dan kegunaan masing-masing. Dengan begitu maka kita dapat menghindari untuk konflik terjadi pada satu project ke project lain karena penggunaan versi-versi yang berbeda.

Kita tetap dapat membuat project Django tanpa menggunakan Virtual Environment, namun dapat banyak muncul masalah yang terjadi seperti konflik karena versi-versi komponen pendukung yang berbeda-beda, serta project menjadi tidak stabil dan memerlukan konfigurasi pengaturan yang lebih rumit.

------------------- MVC | MVT | MVVM -------------------

--> MVC atau Model, View dan Controller dengan pembagian :
    - Model : Bagian yang bertugas untuk mengelola sistem website dan menghubungkan sistem website dan project dengan database yang digunakan.
    - View : Bagian yang bertugas dalam mengatur tampilan website yang ditunjukan kepada client dalam bentuk informasi-informasi pada website.
    - Controller : Bagian yang bertugas untuk mengatur hubungan antara bagian Model dan bagian View di dalam setiap proses request dari client/user.

--> MVT atau Model, View dan Template dengan pembagian :
    - Model : Bagian yang bertugas dalam mengelola sistem pada website dan menghubungkan sistem website dengan database yang digunakan.
    - View : Bagian yang bertugas untuk mengatur hubungan antara bagian Model dan bagian Template di dalam setiap proses request dari client/user.
    - Template : Bagian yang bertugas dalam mengatur tampilan website yang ditunjukan kepada client dalam bentuk informasi-informasi pada website.

--> MVVM atau Model, View dan ViewModel dengan pembagian :
    - Model : Bagian yang bertugas dalam mengelola sistem pada website dan menerapkan logika sistem di dalam project.
    - View : Bagian yang bertugas dalam mengatur tampilan website yang ditunjukan kepada client dalam bentuk informasi-informasi pada website.
    - ViewModel : Bagian yang bertugas untuk mengatur hubungan antara bagian Model dan bagian View di dalam setiap proses request dari client/user.

Perbedaanya adalah MVC adalah sistem yang bisanya digunakan dalam membuat pengembangan sistem perangkat lunak, sedangkan MVT adalah MVC yang secara spesifik digunakan di dalam pengembangan project Django, lalu MVVM digunakan di dalam pengembangan sebuah sistem aplikasi yang lebih berfokus di dalam penggunaan UI (User Interface).